Proyecto
# 📱 Scraping de Planes Entel Perú

Este proyecto hace scraping de los planes postpago de Entel Perú y extrae:
- Nombre del plan
- Precio
- Datos de internet
- Apps incluidas
- Minutos de llamadas
- SMS
- Roaming

## 📦 Librerías usadas

```bash
pip install requests beautifulsoup4 pandas


Generamos por medio de formato .csv una tabla con relación precio -beneficios por cada plan 
```python
import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL de la página a scrapear
url = "https://ofertasentel.pe/?utm_source=bing&utm_medium=cpc_search&utm_campaign=pospago_promo_marcaplanes&utm_term=marca_planes&utmcampaign=0104020302&msclkid=dfab6aa18cde18a17c3b02cd920ff43b"

# Realizar la petición HTTP
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
response = requests.get(url, headers=headers)

# Verificar que la petición fue exitosa
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Lista para almacenar los datos
    data = []
    
    # Encontrar todos los contenedores de planes
    plan_boxes = soup.find_all('div', class_='box')
    
    for box in plan_boxes:
        # Extraer nombre del plan desde <b> dentro de property_internet
        plan_name_tag = box.find('div', class_='property property_internet')
        if plan_name_tag and plan_name_tag.find('b'):
            plan_name = plan_name_tag.find('b').get_text(strip=True)
        else:
            plan_name = 'N/A'
        
        # Extraer precio
        price_tag = box.find('div', class_='price')
        price = price_tag.get_text(strip=True) if price_tag else 'N/A'
        
        # Extraer la información de internet desde el div.gb
        gb_div = box.find('div', class_='gb')
        if gb_div:
            strong_text = gb_div.find('strong').get_text(strip=True) if gb_div.find('strong') else ''
            span_text = gb_div.find('span').get_text(strip=True) if gb_div.find('span') else ''
            internet = f"{strong_text} {span_text}".strip()
        else:
            internet = 'N/A'
        
        # Extraer otras características
        app = box.find('div', class_='property property_app')
        llamadas = box.find('div', class_='property property_llamadas')
        sms = box.find('div', class_='property property_sms')
        roaming = box.find('div', class_='property property_roaming')
        
        # Obtener los textos
        app_text = app.get_text(strip=True, separator=' ') if app else 'N/A'
        llamadas_text = llamadas.get_text(strip=True) if llamadas else 'N/A'
        sms_text = sms.get_text(strip=True) if sms else 'N/A'
        roaming_text = roaming.get_text(strip=True) if roaming else 'N/A'
        
        # Agregar los datos a la lista
        data.append({
            'Plan': plan_name,
            'Precio': price,
            'Internet': internet,
            'App': app_text,
            'Llamadas': llamadas_text,
            'SMS': sms_text,
            'Roaming': roaming_text
        })
    
    # Crear DataFrame
    df = pd.DataFrame(data)
    
    # Eliminar filas donde todas las columnas son 'N/A'
    mask = (df != 'N/A').any(axis=1)
    df = df[mask]
    
    # Mostrar el DataFrame
    display(df)
    
    # Guardar como CSV
    df.to_csv('ofertas_entel_mejorado.csv', index=False, encoding='utf-8-sig')
    print("Datos guardados en 'ofertas_entel_mejorado.csv'")
else:
    print(f"Error al acceder a la página. Código de estado: {response.status_code}")
```

Y obtenemos el resumen de la tabla :
| Plan      | Precio | Internet | App                      | Llamadas    | SMS        | Roaming               |
| :-------- | :----- | :------- | :----------------------- | :---------- | :--------- | :-------------------- |
| Power 99  | S/ 99  | 50 GB    | Facebook, Instagram Free | Ilimitadas  | Ilimitados | América, Europa       |
| Simple 49 | S/ 49  | 15 GB    | Facebook Free            | 300 minutos | 100        | América               |
| Full 149  | S/ 149 | 80 GB    | Apps ilimitadas          | Ilimitadas  | Ilimitados | América, Europa, Asia |
| Promo 79  | S/ 79  | 30 GB    | WhatsApp, Facebook Free  | 500 minutos | 200        | Solo América          |
