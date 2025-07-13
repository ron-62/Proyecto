<div align="center">

##  Proyecto de Lenguaje de Programación 2

##  Web Scraping de Planes Postpago Perú
<img width="500" height="8000" alt="image" src="https://github.com/user-attachments/assets/9d05e835-b0ce-4667-816b-5ab488106015" />


</div>

# Integrantes:

|Nombres y Apellidos      | Codigo     |
|:------------------------|:-----------|
| Nicole Alva Aquino      |  20221388    |
|   Alejandra Arroyo            |    20211805     |
|  Alonso coronado de la Vega  |     20221395      |


### 📚 Curso: Lenguaje de Programación 2  
### 👩‍💻 Docente: Ana Vargas  
### 📅 Ciclo: 2025-I


# 📖 Introducción
El avance de la tecnología y la digitalización de los servicios han hecho posible acceder a información en línea de manera rápida y automatizada. En este contexto, el web scraping se presenta como una herramienta fundamental para la recolección eficiente de datos desde páginas web. Este proyecto tiene como finalidad aplicar conocimientos técnicos de lenguaje de programación Python y herramientas complementarias como Selenium, BeautifulSoup, pandas y Dash, para obtener, procesar y visualizar información relevante de los planes postpago ofrecidos por operadoras móviles en Perú, como Entel y Bitel.

El presente trabajo se enmarca dentro del curso Lenguaje de Programación 2, cuyo objetivo es fortalecer las competencias técnicas en el uso de plataformas y entornos de desarrollo para la automatización de procesos, análisis de datos y creación de dashboards interactivos. Mediante este proyecto, se busca recolectar datos sobre las tarifas y beneficios de los planes móviles, estructurarlos en archivos CSV y JSON, y presentarlos de forma clara y dinámica a través de dashboards, facilitando su análisis y comparación.

# 🎯 Objetivo General
Desarrollar un sistema de scraping y visualización de datos de planes postpago de operadoras móviles en Perú, aplicando herramientas de programación en Python para automatizar la recolección, almacenamiento y representación de información, permitiendo comparar tarifas y beneficios mediante dashboards interactivos.

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

## 📦 Dependencias
```bash
# Instalar Selenium, BeautifulSoup, Pandas y Webdriver Manager
!pip install selenium beautifulsoup4 pandas webdriver-manager

# --- INSTALACIÓN DE GOOGLE CHROME EN COLAB ---
# 1. Descargar la clave GPG de Google Chrome
!wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | sudo gpg --dearmor -o /usr/share/keyrings/google-chrome-archive-keyring.gpg

# 2. Añadir el repositorio de Google Chrome a las fuentes de apt
!echo "deb [arch=amd64 signed-by=/usr/share/keyrings/google-chrome-archive-keyring.gpg] http://dl.google.com/linux/chrome/deb/ stable main" | sudo tee /etc/apt/sources.list.d/google-chrome.list

# 3. Actualizar los listados de paquetes apt para incluir el nuevo repositorio
!sudo apt-get update

# 4. Instalar Google Chrome estable
!sudo apt-get install -y google-chrome-stable

# Opcional: Verificar la versión de Chrome instalada
!google-chrome --version

print("\n--- Instalación de Chrome y dependencias completada ---")
```
## Código Web Scrapping Bitel
```bash
# --- PASO 1: INSTALAR LAS LIBRERÍAS NECESARIAS EN GOOGLE COLAB ---
# ¡IMPORTANTE!: Ejecuta esta celda al inicio de tu notebook.
# Esto intentará suprimir la mayoría de los mensajes de instalación.
!pip install selenium webdriver-manager > /dev/null 2>&1

# --- PASO 2: IMPORTAR LAS LIBRERÍAS ---
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import pandas as pd
import re

# Importar para mostrar HTML en Colab
from IPython.display import display, HTML

def extraer_planes_bitel_colab():
    """
    Extrae la información de los planes postpago de Bitel Perú desde su página web.
    Usa Selenium para manejar el contenido dinámico y BeautifulSoup para parsear el HTML.
    Retorna una lista de diccionarios, con los planes extraídos.
    """
    url = "https://bitel.com.pe/planes/control/ilimitado"
    planes_data = []

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--window-size=1990,1080') # Aumentado ligeramente el tamaño de la ventana
    options.add_argument('--log-level=3') # Suprime la mayoría de los logs del navegador
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = None
    wait = None # Inicializar 'wait' aquí para asegurar que siempre esté definido

    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        driver.get(url)

        wait = WebDriverWait(driver, 45) # Ahora 'wait' se define aquí, antes de cualquier uso

        # --- MANEJO DE POP-UP DE COOKIES O SIMILAR ---
        try:
            common_close_xpaths = [
                "//button[contains(., 'Aceptar') or contains(., 'Entendido') or contains(., 'Cerrar') or contains(., 'OK')]",
                "//a[contains(., 'Aceptar') or contains(., 'Entendido') or contains(., 'Cerrar') or contains(., 'OK')]",
                "//div[contains(@class, 'close-button') or contains(@class, 'modal-close') or contains(@class, 'btn-close') or contains(@class, 'close-popup')]",
                "//span[contains(text(), 'x') or contains(text(), 'X') or @class='close-icon']",
                "//button[contains(@id, 'cookie') or contains(@id, 'modal') or contains(@class, 'cookie') or contains(@class, 'modal')][contains(., 'Aceptar') or contains(., 'Entendido') or contains(., 'OK')]",
                "//div[@role='dialog']//button[contains(., 'Aceptar') or contains(., 'Entendido') or contains(., 'OK')]"
            ]

            found_and_clicked = False
            for xpath_str in common_close_xpaths:
                try:
                    btn = WebDriverWait(driver, 5).until(
                        EC.element_to_be_clickable((By.XPATH, xpath_str))
                    )
                    if btn.is_displayed() and btn.is_enabled():
                        btn.click()
                        time.sleep(2)
                        found_and_clicked = True
                        break
                except:
                    pass

        except Exception as e:
            pass # No imprimir errores de pop-up para mantener la salida limpia

        # --- ESPERAR A QUE EL CONTENIDO PRINCIPAL CARGUE ---
        try:
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'cont-package')))
        except Exception as e:
            # Intentar scroll y reintentar la espera si el elemento no es visible inicialmente
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")
            time.sleep(3)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(5)

            try:
                wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'cont-package')))
            except Exception as e:
                # Este es el único ERROR FATAL que se imprimirá si no se encuentra el elemento clave
                print(f"ERROR FATAL: 'cont-package' no se hizo visible incluso después de scroll. {e}")
                print("La estructura de la página o la forma en que carga el contenido ha cambiado significativamente o hay un bloqueo persistente.")
                return []

        time.sleep(5) # Tiempo adicional para asegurar la carga completa

        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')

        plan_elements = soup.find_all('div', class_='cont-package')

        if not plan_elements:
            print("ERROR: Después de la carga, no se encontraron elementos con la clase 'cont-package' en BeautifulSoup.")
            print("Esto podría indicar que la clase ha cambiado o el contenido no está en el HTML parseado.")
            return []

        for i, plan_element in enumerate(plan_elements):
            nombre_plan = 'N/A'
            precio = 'N/A'
            gigas = 'N/A'
            apps_ilimitadas = 'No especificado'
            minutos_llamadas = 'No especificado'
            sms = 'No especificado'
            detalles_gigas = 'N/A' # Nuevo campo para detalles de gigas

            full_plan_text_raw = plan_element.get_text(separator=' ', strip=True)
            full_plan_text_lower = full_plan_text_raw.lower()

            # 2. Extraer Precio
            match_precio = re.search(r's/\s*(\d+\.\d+)', full_plan_text_lower)
            if match_precio:
                precio = f"S/ {match_precio.group(1)}"
            else:
                price_element_a = plan_element.find('a', href="javascript:void(0);")
                if price_element_a:
                    title_attr = price_element_a.get('title')
                    if title_attr:
                        match_price_title = re.search(r'(\d+\.\d+)', title_attr)
                        if match_price_title:
                            precio = f"S/ {match_price_title.group(1)}"

                if precio == 'N/A':
                    match_precio_simple = re.search(r'(\d+\.\d+)', full_plan_text_lower)
                    if match_precio_simple:
                        precio_val = float(match_precio_simple.group(1))
                        if 10.00 <= precio_val <= 200.00:
                            precio = f"S/ {match_precio_simple.group(1)}"

            # 1. Modificar Nombre del Plan para ser "Ilimitado - [Precio del Plan]"
            if precio != 'N/A':
                nombre_plan = f"Ilimitado - {precio.replace('S/ ', '')}"
            else:
                name_span_element = plan_element.find('span', class_='color-white text-bold title-1g')
                if name_span_element:
                    span_text = name_span_element.get_text(strip=True)
                    cleaned_span_text = re.sub(r'\s*S/\s*\d+\.\d+', '', span_text, flags=re.IGNORECASE).strip()
                    cleaned_span_text = re.sub(r'\s*\d+\.\d+$', '', cleaned_span_text, flags=re.IGNORECASE).strip()
                    if cleaned_span_text:
                        nombre_plan = f"Ilimitado - {cleaned_span_text}"
                    else:
                        nombre_plan = "Ilimitado - Precio No Disponible"
                else:
                    nombre_plan = "Ilimitado - Precio No Disponible"

            # 3. Extraer Gigas y Detalles de Gigas
            gigas_element = plan_element.find('p', class_='capa')

            if gigas_element:
                gigas_text = gigas_element.get_text(strip=True)
                gigas_text_lower = gigas_text.lower()

                period_element = plan_element.find('p', class_='period')
                period_text_lower = period_element.get_text(strip=True).lower() if period_element else ''

                if 'ilimitados' in gigas_text_lower:
                    gigas = 'Ilimitados'
                    match_gigas_alta_velocidad = re.search(r'(\d+)\s*GB(?:\s*en\s*alta\s*velocidad)?', gigas_text, re.IGNORECASE)
                    if match_gigas_alta_velocidad:
                        detalles_gigas = f"{match_gigas_alta_velocidad.group(1)} GB en Alta Velocidad"
                    elif 'alta velocidad' in period_text_lower:
                        detalles_gigas = "Velocidad reducida después de cierto consumo"
                    else:
                        detalles_gigas = "Datos ilimitados sin restricciones de velocidad explícitas"
                else:
                    match_gigas = re.search(r'(\d+)\s*GB', gigas_text, re.IGNORECASE)
                    if match_gigas:
                        gigas = f"{match_gigas.group(1)} GB"
                        if 'alta velocidad' in period_text_lower:
                            detalles_gigas = "En Alta Velocidad"
                    else:
                        gigas = gigas_text
                        if 'alta velocidad' in period_text_lower:
                            detalles_gigas = "En Alta Velocidad"
            else:
                gigas = 'N/A'
                detalles_gigas = 'Elemento de gigas no encontrado'


            # 4. Extraer Apps Ilimitadas
            app_keywords_patterns = {
                'WhatsApp': r'whatsapp ilimitado',
                'Facebook': r'facebook ilimitado',
                'Instagram': r'instagram ilimitado',
                'TikTok': r'tiktok ilimitado',
                'Spotify': r'spotify ilimitado',
                'Waze': r'waze ilimitado',
                'YouTube': r'youtube ilimitado',
                'Apps ilimitadas x meses': r'apps ilimitadas (x \d+ meses)?',
                'Internet + Llamadas ilimitadas': r'internet \+\s*llamadas ilimitadas'
            }
            found_apps = []
            for app_name, pattern in app_keywords_patterns.items():
                if re.search(pattern, full_plan_text_lower):
                    if 'x \d+ meses' in pattern and re.search(r'x \d+ meses', full_plan_text_lower):
                        promo_match = re.search(r'x \d+ meses', full_plan_text_lower).group(0)
                        found_apps.append(f"{app_name.replace(' x meses', '')} {promo_match}")
                    else:
                        found_apps.append(app_name)

            app_image_elements = plan_element.find_all('li', class_='app-item')
            for app_li in app_image_elements:
                img_tag = app_li.find('img')
                if img_tag and 'alt' in img_tag.attrs:
                    app_name_from_alt = img_tag['alt'].strip()
                    if app_name_from_alt and app_name_from_alt.lower() not in [app.lower() for app in found_apps]:
                        found_apps.append(app_name_from_alt)

            apps_ilimitadas = ", ".join(sorted(list(set(found_apps)))) if found_apps else 'No especificado'

            # Minutos/Llamadas y SMS
            minutos_llamadas = "No especificado"
            sms = "No especificado"

            todo_ilimitado_element = plan_element.find('p', class_=re.compile(r'title.*Todo ilimitado'))
            if todo_ilimitado_element and "todo ilimitado" in todo_ilimitado_element.get_text(strip=True).lower():
                minutos_llamadas = 'Llamadas ilimitadas'
                sms = 'SMS ilimitados'
            else:
                if 'llamadas ilimitadas perú' in full_plan_text_lower:
                    minutos_llamadas = 'Llamadas ilimitadas Perú'
                    match_usa_canada = re.search(r'(\d+)\s*minutos\s*(?:para|a)\s*(?:usa|eeuu)\s*(?:y|e)\s*canadá', full_plan_text_lower)
                    if match_usa_canada:
                        minutos_llamadas += f", {match_usa_canada.group(1)} minutos para Usa y Canadá"
                elif 'llamadas ilimitadas' in full_plan_text_lower:
                    minutos_llamadas = 'Llamadas ilimitadas'

                if 'sms ilimitados' in full_plan_text_lower:
                    sms = 'SMS ilimitados'
                else:
                    match_sms = re.search(r'(\d+)\s*sms', full_plan_text_lower)
                    if match_sms:
                        sms = f"{match_sms.group(1)} SMS"

            benefit_period_element = plan_element.find('p', class_='benefit-period')
            if benefit_period_element and "internet, llamadas y sms" in benefit_period_element.get_text(strip=True).lower():
                if minutos_llamadas == "No especificado":
                    minutos_llamadas = 'Llamadas incluidas'
                if sms == "No especificado":
                    sms = 'SMS incluidos'

            planes_data.append({
                'Nombre del Plan': nombre_plan,
                'Precio (S/)': precio,
                'Gigas': gigas,
                'Detalles de Gigas': detalles_gigas, # Añadir el nuevo campo
                'Apps Ilimitadas': apps_ilimitadas,
                'Minutos/Llamadas': minutos_llamadas,
                'SMS': sms
            })

    except Exception as e:
        print(f"Ocurrió un error crítico durante la ejecución: {e}")
        return []
    finally:
        if driver:
            driver.quit()

    return planes_data

if __name__ == "__main__":
    planes = extraer_planes_bitel_colab()
    if planes:
        df = pd.DataFrame(planes)

        # Ordenar por precio, asegurando que los valores 'N/A' vayan al final
        df['Precio_Sort'] = df['Precio (S/)'].apply(lambda x: float(str(x).replace('S/ ', '')) if isinstance(x, str) and 'S/' in x else (x if isinstance(x, (int, float)) else float('inf')))
        df_sorted = df.sort_values(by='Precio_Sort').drop(columns='Precio_Sort')

        # Estilos CSS personalizados para la tabla HTML (colores de Bitel)
        html_style = """
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; background-color: #f4f4f4; color: #333; }
            h1 { color: #007bff; text-align: center; margin-bottom: 20px; }
            table {
                width: 100%;
                border-collapse: collapse;
                margin-top: 20px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.15);
                background-color: #fff;
                border-radius: 8px;
                overflow: hidden;
            }
            th, td {
                padding: 15px 20px;
                text-align: left;
                border-bottom: 1px solid #eee;
            }
            th {
                background-color: #00AEEF; /* Azul Bitel */
                color: white;
                text-transform: uppercase;
                font-size: 0.95em;
                letter-spacing: 0.5px;
            }
            tr:nth-child(even) {
                background-color: #f8f8f8;
            }
            tr:hover {
                background-color: #e0f7fa; /* Un azul claro al pasar el mouse */
            }
            /* Estilo para la línea del encabezado */
            .header-line {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                font-size: 1.2em;
                font-weight: bold;
                color: #555;
                text-align: center;
                margin-bottom: 25px;
                padding-bottom: 10px;
                border-bottom: 2px solid #ddd;
            }
        </style>
        """

        # Generar la tabla HTML desde el DataFrame ordenado
        html_table = df_sorted.to_html(index=False, escape=False, classes='bitel-plans-table')

        # Combinar todas las partes en un documento HTML completo
        full_html_output = f"""
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Planes y Beneficios Bitel Perú</title>
            {html_style}
        </head>
        <body>
            <div class="header-line">--- Planes y Beneficios (ordenados por precio) ---</div>
            {html_table}
        </body>
        </html>
        """

        # Mostrar el HTML directamente en la celda de salida de Colab
        display(HTML(full_html_output))
    else:
        # Si no se extraen planes, el mensaje de error ya habrá sido impreso por la función.
        pass

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
