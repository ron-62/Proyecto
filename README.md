Proyecto
# 📱Web scraping de Planes Entel Perú

Este proyecto hace scraping de los planes postpago de Entel Perú y extrae:
- Nombre del plan
- Precio
- Datos de internet
- Apps incluidas
- Minutos de llamadas
- SMS


## 📦 Librerías usadas
```python
import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL de la página a scrapear
url = "https://ofertasentel.pe/?utm_source=bing&utm_medium=cpc_search&utm_campaign=pospago_promo_marcaplanes&utm_term=marca_planes&utmcampaign=0104020302&msclkid=dfab6aa18cde18a17c3b02cd920ff43b"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    
    data = []
    plan_boxes = soup.find_all('div', class_='box')
    
    for box in plan_boxes:
        plan_name_tag = box.find('div', class_='property property_internet')
        plan_name = plan_name_tag.find('b').get_text(strip=True) if plan_name_tag and plan_name_tag.find('b') else 'N/A'
        
        price_tag = box.find('div', class_='price')
        price = price_tag.get_text(strip=True) if price_tag else 'N/A'
        
        gb_div = box.find('div', class_='gb')
        if gb_div:
            strong_text = gb_div.find('strong').get_text(strip=True) if gb_div.find('strong') else ''
            span_text = gb_div.find('span').get_text(strip=True) if gb_div.find('span') else ''
            internet = f"{strong_text} {span_text}".strip()
        else:
            internet = 'N/A'
        
        app = box.find('div', class_='property property_app')
        llamadas = box.find('div', class_='property property_llamadas')
        sms = box.find('div', class_='property property_sms')
        
        app_text = app.get_text(strip=True, separator=' ') if app else 'N/A'
        llamadas_text = llamadas.get_text(strip=True) if llamadas else 'N/A'
        sms_text = sms.get_text(strip=True) if sms else 'N/A'
        
        data.append({
            'Plan': plan_name,
            'Precio': price,
            'Internet': internet,
            'App': app_text,
            'Llamadas': llamadas_text,
            'SMS': sms_text
        })
    
    df = pd.DataFrame(data)
    mask = (df != 'N/A').any(axis=1)
    df = df[mask]
    
    display(df)
    df.to_csv('ofertas_entel_sin_roaming.csv', index=False, encoding='utf-8-sig')
    print("✅ Datos guardados en 'ofertas_entel_sin_roaming.csv'")
else:
    print(f"Error al acceder a la página. Código de estado: {response.status_code}")

```

Y obtenemos el resumen de la tabla :

| Plan               | Precio                                  | Internet                         | App                | Llamadas                                | SMS            |
|:------------------|:----------------------------------------|:----------------------------------|:-------------------|:-----------------------------------------|:----------------|
| Power Ilim 69.90   | S/34.95/mes a partir del mes 7 a s/69.90 | Ilimitado 100 GB en alta velocidad | Internet Ilimitado | Llamadas ilimitadas Chile, USA, Canadá | 500 SMS        |
| Plan Power 29.90   | S/29.90/mes                              | 10 GB en alta velocidad           | Apps Ilimitadas     | Llamadas ilimitadas Chile, USA, Canadá | 500 SMS        |
| Plan power 39.90   | S/39.90/mes                              | 25 GB en alta velocidad           | Apps Ilimitadas     | Llamadas ilimitadas Chile, USA, Canadá | 500 SMS        |
| Plan power 49.90   | S/49.90/mes                              | 40 GB en alta velocidad           | Apps Ilimitadas     | Llamadas ilimitadas Chile, USA, Canadá | 500 SMS        |
| Plan power 59.90   | S/59.90/mes                              | 75 GB en alta velocidad           | Apps Ilimitadas     | Llamadas ilimitadas Chile, USA, Canadá | 500 SMS        |
| Power Ilim 79.90 SD| S/63.92/mes luego s/79.90/mes            | TODO ILIMITADO GB, llamadas y SMS | Internet Ilimitado | Llamadas ilimitadas Chile, USA, Canadá | SMS Ilimitados |




# 📱 Scraping de Planes Bitel Perú

Este proyecto hace scraping de los planes postpago de Bitel Perú y extrae:
- Nombre del plan
- Precio
- Datos de internet
- Apps incluidas
- Minutos de llamadas
- SMS
- Roaming

## 📦 Librerías usadas

```bash
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import json
import pandas as pd  # ✅ Para tabla y CSV

def configurar_driver():
    opciones = Options()
    opciones.add_argument("--headless")  # Ejecutar sin abrir ventana
    opciones.add_argument("--no-sandbox")
    opciones.add_argument("--disable-dev-shm-usage")
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opciones)

def extraer_tabla_postpago(driver):
    planes = []
    filas = driver.find_elements(By.CSS_SELECTOR, "table.eael-data-table tbody tr")
    print(f"🔎 Se encontraron {len(filas)} filas en la tabla")

    for fila in filas:
        celdas = fila.find_elements(By.CSS_SELECTOR, "td .td-content")
        if not celdas:
            continue

        nombre = celdas[0].text.strip()
        beneficios = [celda.text.strip() for celda in celdas[1:] if celda.text.strip()]

        planes.append({
            "plan": nombre,
            "beneficios": beneficios
        })

    return planes

def scrape_postpago():
    urls = {
        "Flash (postpago)": "https://bitelportabilidad.com.pe/movil/postpago-flash/",
        "Ilimitado (postpago)": "https://bitelportabilidad.com.pe/movil/postpago-ilimitado/"
    }

    driver = configurar_driver()
    planes_totales = []

    for categoria, url in urls.items():
        print(f"\n🌐 Cargando {categoria}: {url}")
        driver.get(url)
        time.sleep(4)  # Esperar carga completa
        planes = extraer_tabla_postpago(driver)

        for plan in planes:
            plan["categoria"] = categoria
        planes_totales.extend(planes)

    driver.quit()

    # Guardar en JSON
    with open("postpago_bitel.json", "w", encoding="utf-8") as f:
        json.dump(planes_totales, f, indent=2, ensure_ascii=False)
    print("\n✅ Datos guardados en 'postpago_bitel.json'")

    # Mostrar en tabla con pandas
    df = pd.DataFrame(planes_totales)
    print("\n📊 Tabla de planes postpago:")
    print(df.to_markdown(index=False))

    # Guardar en CSV para abrir en Excel
    df.to_csv("planes_postpago_bitel.csv", index=False, encoding="utf-8-sig")
    print("\n💾 CSV guardado como 'planes_postpago_bitel.csv'")

if __name__ == "__main__":
    scrape_postpago()


```
Y obtenemos el resumen de la tabla :

| plan            |   precio_inicial |   gb_inicial | apps_incluidas                                                           | categoria            |
|:----------------|-----------------:|-------------:|:-------------------------------------------------------------------------|:---------------------|
| Flash 29.90     |             29.9 |           50 | ['Instagram', 'WhatsApp', 'Spotify', 'Facebook']                         | Flash (postpago)     |
| Flash 39.90     |             39.9 |           50 | ['Instagram', 'WhatsApp', 'Spotify', 'Facebook']                         | Flash (postpago)     |
| Flash 49.90     |             49.9 |           70 | ['Instagram', 'WhatsApp', 'Spotify', 'Facebook']                         | Flash (postpago)     |
| Flash 109.90    |             54.9 |          200 | ['Instagram', 'Facebook', 'Paramount+', 'WhatsApp', 'TikTok', 'Spotify'] | Flash (postpago)     |
| 39.90 ilimitado |             39.9 |           80 | ['Spotify', 'TV360Bitel']                                                | Ilimitado (postpago) |
| 49.90 ilimitado |             24.9 |           45 | ['Spotify', 'TikTok', 'TV360Bitel']                                      | Ilimitado (postpago) |
| 55.90 ilimitado |             39.1 |           60 | ['Paramount+', 'Spotify', 'TikTok', 'TV360Bitel']                        | Ilimitado (postpago) |
| 65.90 ilimitado |             46.1 |          100 | ['Paramount+', 'Spotify', 'TikTok', 'TV360Bitel']                        | Ilimitado (postpago) |
| 69.90 ilimitado |             34.9 |          110 | ['Paramount+', 'Spotify', 'TikTok', 'TV360Bitel']                        | Ilimitado (postpago) |
| 79.90 ilimitado |             39.9 |          125 | ['Paramount+', 'Spotify', 'TikTok', 'TV360Bitel']                        | Ilimitado (postpago) |
| 5G              |            nan   |          nan |                                                                          | Ilimitado (postpago) |
| 4G-LTE          |            nan   |          nan |                                                                          | Ilimitado (postpago) |
| 3G              |            nan   |          nan |                                                                          | Ilimitado (postpago) |
