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
from webdriver_manager.chrome import ChromeDriverManager
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

| Plan            | Precio/mes | Internet en Alta Velocidad | Apps Ilimitadas                                                            | Llamadas y SMS |
| --------------- | ---------- | -------------------------- | -------------------------------------------------------------------------- | -------------- |
| Ilimitado 27.90 | S/27.90    | 75 GB                      | Facebook, Instagram, WhatsApp, Paramount+, Spotify, TV360 *(12 meses)*     | Incluidas      |
| Ilimitado 34.90 | S/34.90    | 110 GB                     | Paramount+, Spotify, TV360                                                 | Incluidas      |
| Ilimitado 39.90 | S/39.90    | 125 GB                     | Facebook, Instagram, WhatsApp, Paramount+, Spotify, TV360 *(12 meses)*     | Incluidas      |
| Ilimitado 46.10 | S/46.10    | 100 GB                     | Facebook, Instagram, Paramount+, Spotify, TV360 *(6 meses)*                | Incluidas      |
| Ilimitado 49.90 | S/49.90    | 45 GB                      | Facebook, Instagram, WhatsApp, Spotify, TV360 *(duración no especificada)* | Incluidas      |
| Ilimitado 52.90 | S/52.90    | 160 GB                     | Facebook, Instagram, WhatsApp, Paramount+, Spotify, TV360 *(12 meses)*     | Incluidas      |
| Ilimitado 79.90 | S/79.90    | 30 GB                      | Facebook, Instagram, WhatsApp, Spotify, TV360 *(duración no especificada)* | Incluidas      |


# 📱Web scraping de Planes Movistar Perú
Este proyecto hace scraping de los planes postpago de Movistar Perú y extrae:
- Nombre del plan
- Precio
- Datos de internet
- Apps incluidas
- Minutos de llamadas
- SMS

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
## Código Web Scrapping Movistar
```bash
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import pandas as pd
import re
from webdriver_manager.chrome import ChromeDriverManager

# Importar para mostrar HTML en Colab
from IPython.display import display, HTML

def extraer_planes_movistar_colab():
    url = "https://www.movistar.com.pe/movil/postpago/planes-postpago"
    planes_data = []

    # --- CONFIGURACIÓN DE SELENIUM PARA COLAB ---
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev_shm_usage')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--log-level=3')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = None

    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        driver.get(url)

        # --- ESPERAR A QUE EL CONTENIDO DINÁMICO CARGUE ---
        wait = WebDriverWait(driver, 30)
        try:
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'p-plan__slide__soles')))
        except:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(5)
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'p-plan__slide__soles')))

        time.sleep(5)

        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')

        plan_elements = soup.find_all('div', class_='p-plan__slide__shadow')

        if not plan_elements:
            print("ERROR: No se encontraron elementos con la clase 'p-plan__slide__shadow'.")
            print("Esto podría indicar que la clase ha cambiado nuevamente o el contenido no se cargó como se esperaba.")
            return []

        for i, plan_element in enumerate(plan_elements):
            nombre_plan = 'N/A'
            precio = 'N/A'
            gigas = 'N/A'
            apps_ilimitadas_text = 'N/A'
            otros_beneficios = {}
            llamadas_encontradas = None
            sms_encontrados = None

            # 1. Extraer Precio
            precio_tag = plan_element.find('span', class_='p-plan__slide__soles')
            if precio_tag:
                precio = precio_tag.get_text(strip=True)

            # 2. Extraer Nombre del Plan (Limpieza Mejorada)
            head_tag = plan_element.find('div', class_='p-plan__slide__head')
            if head_tag:
                name_tag = head_tag.find(['h3', 'h4', 'span', 'p'], class_=lambda x: x and ('p-plan__slide__name' in x or 'title' in x or 'plan-name' in x))
                if name_tag:
                    nombre_plan = name_tag.get_text(strip=True)
                else:
                    nombre_plan = ' '.join(head_tag.get_text(separator=' ', strip=True).split())

                nombre_plan = re.sub(r'Plan Postpago\s*', '', nombre_plan, flags=re.IGNORECASE)
                nombre_plan = re.sub(r'S/\s*\d+\.\d+', '', nombre_plan, flags=re.IGNORECASE)
                nombre_plan = re.sub(r'al mes', '', nombre_plan, flags=re.IGNORECASE)
                nombre_plan = re.sub(r'x \d+ meses', '', nombre_plan, flags=re.IGNORECASE)
                nombre_plan = re.sub(r'Precio regular:.*?(Ahorra \d+%)?', '', nombre_plan, flags=re.IGNORECASE)
                nombre_plan = re.sub(r'Bono \d+ GB', '', nombre_plan, flags=re.IGNORECASE)
                nombre_plan = re.sub(r'Exclusivo online', '', nombre_plan, flags=re.IGNORECASE)
                nombre_plan = re.sub(r'\*', '', nombre_plan).strip()
                nombre_plan = re.sub(r'\s{2,}', ' ', nombre_plan).strip()

                if not nombre_plan:
                    nombre_plan = f"Plan Postpago {precio}" if precio != 'N/A' else 'Plan Postpago Desconocido'


            # 3. Extraer Gigas / Datos
            gigas_cantidad_tag = plan_element.find('span', class_='p-plan__slide__cantidad')
            if gigas_cantidad_tag:
                extracted_gigas = gigas_cantidad_tag.get_text(strip=True).replace('\n', ' ').strip()
                if "GB" in extracted_gigas.upper() or re.match(r'^\d+(\.\d+)?\s*GB$', extracted_gigas, re.IGNORECASE):
                    gigas = extracted_gigas
                elif "Bono" in extracted_gigas and "GB" in extracted_gigas:
                    gigas = extracted_gigas

            if gigas == 'N/A':
                ilimitado_tag = plan_element.find(['span', 'div', 'h3', 'p'], class_=lambda x: x and ('p-plan__slide__gigas' in x or 'gigas-text' in x or 'data-info' in x))
                if ilimitado_tag and ("ilimitado" in ilimitado_tag.get_text().lower() or "sin límites" in ilimitado_tag.get_text().lower()):
                    gigas = "Ilimitados"
                else:
                    text_content_lower = plan_element.get_text(separator=' ', strip=True).lower()
                    if "ilimitado" in text_content_lower and ("datos" in text_content_lower or "gigas" in text_content_lower):
                        gigas = "Ilimitados"
                    else:
                        match_gb = re.search(r'(\d+)\s*gb', text_content_lower)
                        if match_gb:
                            gigas = f"{match_gb.group(1)} GB"
                        else:
                            match_bono_gb = re.search(r'(bono\s*\d+\s*gb\s*x\s*\d+\s*meses)', text_content_lower)
                            if match_bono_gb:
                                gigas = match_bono_gb.group(1).replace('x', 'x ')

            # 4. Extraer Apps Ilimitadas
            apps_ttl_tag = plan_element.find('p', class_='p-plan__slide__apps__ttl')
            if apps_ttl_tag:
                apps_ilimitadas_text = apps_ttl_tag.get_text(strip=True)
                apps_ilimitadas_text = re.sub(r'\s*\n\s*', ' ', apps_ilimitadas_text).strip()
            else:
                apps_ilimitadas_list_temp = []
                apps_container = plan_element.find('div', class_='p-plan__slide__apps')
                if apps_container:
                    app_elements = apps_container.find_all(['img', 'span', 'i', 'p'], class_=lambda x: x and ('app-icon' in x or 'unlimited-app-icon' in x or 'logo-app' in x or 'app-name' in x))
                    for app_el in app_elements:
                        app_name = app_el.get('alt') or app_el.get('title') or app_el.get_text(strip=True)
                        if app_name and app_name.strip():
                            apps_ilimitadas_list_temp.append(re.sub(r'\s*\n\s*', ' ', app_name).strip())

                if not apps_ilimitadas_list_temp:
                    text_content_full = plan_element.get_text(separator=' ', strip=True)
                    match_apps_text = re.search(r'(?:Apps|Redes Sociales)\s+Ilimitadas(?::\s*(.*?))?(?=[.\n]|$)', text_content_full, re.IGNORECASE | re.DOTALL)
                    if match_apps_text:
                        if match_apps_text.group(1):
                            apps_ilimitadas_list_temp.extend([re.sub(r'\s*\n\s*', ' ', app.strip()).strip() for app in match_apps_text.group(1).split(',') if app.strip()])
                        else:
                            apps_ilimitadas_list_temp.append(re.sub(r'\s*\n\s*', ' ', match_apps_text.group(0).replace(":", "").strip()).strip())

                    keywords = ["WhatsApp", "Facebook", "Instagram", "TikTok", "Spotify", "Netflix", "Youtube", "Waze", "Twitter"]
                    for keyword in keywords:
                        if f"{keyword} Ilimitado" in text_content_full or f"Acceso ilimitado a {keyword}" in text_content_full:
                            if keyword.lower() not in [a.lower() for a in apps_ilimitadas_list_temp]:
                                apps_ilimitadas_list_temp.append(keyword)

                if apps_ilimitadas_list_temp:
                    apps_ilimitadas_text = ", ".join(sorted(list(set(apps_ilimitadas_list_temp))))

            # 5. Extraer Otros Beneficios (Minutos/Llamadas, SMS y otros) - LÓGICA MEJORADA Y MÁS GRANULAR
            all_benefit_texts_raw = []

            # Priorizar la clase específica que mostraste para llamadas/SMS
            benefit_text_tags_specific = plan_element.find_all('p', class_='stefa-parrilla_blanco--body-texto')
            for tag in benefit_text_tags_specific:
                all_benefit_texts_raw.append(tag.get_text(strip=True))

            # Buscar en el contenedor general de detalles por si hay más beneficios
            details_container = plan_element.find('div', class_='p-plan__slide__details')
            if details_container:
                general_benefit_tags = details_container.find_all(['li', 'p', 'span', 'div'], class_=lambda x: x and ('benefit-item' in x or 'feature-row' in x or 'text-benefit' in x or 'item-detail' in x or 'body-text' in x or 'plan-detail' in x))
                for tag in general_benefit_tags:
                    all_benefit_texts_raw.append(tag.get_text(strip=True))

            # También considerar el texto completo del plan si no se encontró nada más específico
            full_plan_text = plan_element.get_text(separator=' ', strip=True)
            all_benefit_texts_raw.append(full_plan_text)

            processed_texts = set()

            for raw_text in all_benefit_texts_raw:
                cleaned_text = re.sub(r'\s*\n\s*', ' ', raw_text).strip()
                if not cleaned_text or cleaned_text in processed_texts:
                    continue
                processed_texts.add(cleaned_text)

                text_lower = cleaned_text.lower()

                # --- Extracción granular de Minutos/Llamadas ---
                if llamadas_encontradas is None: # Solo si no se ha encontrado una frase específica de llamadas
                    # Patrones para llamadas ilimitadas o con minutos específicos
                    match_calls = re.search(r'(llamadas ilimitadas Perú(?:,)?(?: \d+ minutos para Usa y Canadá)?|minutos ilimitados Perú(?:,)?(?: \d+ para Usa y Canadá)?|llamadas ilimitadas a todo destino nacional|minutos ilimitados a todo destino nacional)', text_lower, re.IGNORECASE)
                    if match_calls:
                        llamadas_encontradas = match_calls.group(0).replace('perú,', 'Perú,').replace('usa y canadá', 'Usa y Canadá').replace('minutos para', 'minutos para ').strip()
                    elif 'llamadas ilimitadas' in text_lower: # Captura general si no hay patrón específico
                           llamadas_encontradas = 'Llamadas ilimitadas'
                    elif re.search(r'(\d+)\s*minutos\s*para\s*(usa|canadá|internacionales)', text_lower, re.IGNORECASE):
                        llamadas_encontradas = "Minutos internacionales (especificar cantidad)" # Placeholder para refinar si es necesario

                # --- Extracción granular de SMS ---
                if sms_encontrados is None: # Solo si no se ha encontrado una frase específica de SMS
                    # Patrones para SMS
                    match_sms = re.search(r'(\d+)\s*sms|(sms ilimitados)', text_lower, re.IGNORECASE)
                    if match_sms:
                        if match_sms.group(1): # Si encontró un número de SMS
                            sms_encontrados = f"{match_sms.group(1)} SMS"
                        else: # Si encontró "SMS ilimitados"
                            sms_encontrados = "SMS ilimitados"

                # Otros beneficios generales que no sean llamadas ni SMS y que tengan contenido significativo
                if len(cleaned_text) > 10 and \
                   not (llamadas_encontradas and llamadas_encontradas in cleaned_text) and \
                   not (sms_encontrados and sms_encontrados in cleaned_text) and \
                   "gb" not in text_lower and "gigas" not in text_lower and \
                   "apps" not in text_lower and "precio" not in text_lower and \
                   "plan" not in text_lower and "bono" not in text_lower:

                    is_duplicate_or_classified = False
                    for existing_benefit_key, existing_benefit_value in otros_beneficios.items():
                        if cleaned_text == existing_benefit_value or cleaned_text in existing_benefit_value or existing_benefit_value in cleaned_text:
                            is_duplicate_or_classified = True
                            break

                    if not is_duplicate_or_classified:
                        otros_beneficios[f'Otro Beneficio {len([k for k in otros_beneficios if k.startswith("Otro Beneficio")]) + 1}'] = cleaned_text

            # Post-procesamiento para apps_ilimitadas_text que contiene información de llamadas
            if "llamadasilimitadas" in apps_ilimitadas_text.lower() and llamadas_encontradas is None:
                llamadas_encontradas = "Llamadas ilimitadas"
                apps_ilimitadas_text = re.sub(r'Internet \+ llamadasilimitadas', 'Internet', apps_ilimitadas_text, flags=re.IGNORECASE).strip()
                if apps_ilimitadas_text == 'Internet' or not apps_ilimitadas_text:
                    apps_ilimitadas_text = 'N/A'

            # Asignar los valores finales a otros_beneficios
            if llamadas_encontradas:
                otros_beneficios['Minutos/Llamadas'] = llamadas_encontradas
            if sms_encontrados:
                otros_beneficios['SMS'] = sms_encontrados


            # --- AGREGAR LOS DATOS DEL PLAN A LA LISTA ---
            planes_data.append({
                'Nombre del Plan': nombre_plan,
                'Precio (S/)': precio,
                'Gigas': gigas,
                'Apps Ilimitadas': apps_ilimitadas_text,
                **otros_beneficios
            })

    except Exception as e:
        # LÍNEA CORREGIDA
        print(f"Ocurrió un error en la ejecución: {e}")
    finally:
        if driver:
            driver.quit()

    return planes_data

if __name__ == "__main__":
    planes = extraer_planes_movistar_colab()
    if planes:
        df = pd.DataFrame(planes)
        df.to_csv("planes_movistar_postpago.csv", index=False)
        print("Datos guardados en planes_movistar_postpago.csv (puedes descargarlo desde el panel de archivos).")

        # --- GENERAR SALIDA HTML ---
        html_output = """
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Planes Postpago Movistar Perú</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 20px; background-color: #f4f4f4; color: #333; }
                h1 { color: #007bff; text-align: center; }
                table { width: 100%; border-collapse: collapse; margin-top: 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); background-color: #fff; }
                th, td { padding: 12px 15px; text-align: left; border-bottom: 1px solid #ddd; }
                th { background-color: #007bff; color: white; text-transform: uppercase; font-size: 0.9em; }
                tr:nth-child(even) { background-color: #f9f9f9; }
                tr:hover { background-color: #f1f1f1; }
                .note { margin-top: 30px; font-size: 0.9em; color: #666; text-align: center; }
            </style>
        </head>
        <body>
            <h1>Planes Postpago Movistar Perú</h1>
            <table>
                <thead>
                    <tr>
        """

        # Generar los encabezados de la tabla a partir de las columnas del DataFrame
        for col in df.columns:
            html_output += f"<th>{col}</th>\n"

        html_output += """
                    </tr>
                </thead>
                <tbody>
        """

        # Generar las filas de la tabla
        for index, row in df.iterrows():
            html_output += "<tr>\n"
            for col in df.columns:
                # Asegúrate de que los valores sean strings para evitar errores en HTML
                html_output += f"<td>{str(row[col])}</td>\n"
            html_output += "</tr>\n"

        html_output += """
                </tbody>
            </table>
            <p class="note">Datos extraídos de la web de Movistar Perú.</p>
        </body>
        </html>
        """

        # Mostrar el HTML directamente en la salida de Colab
        display(HTML(html_output))

        # Guarda el archivo HTML también, por si lo necesitas descargar
        with open("planes_movistar_postpago.html", "w", encoding="utf-8") as f:
            f.write(html_output)
        print("El reporte HTML también se guardó en 'planes_movistar_postpago.html' (puedes descargarlo).")

    else:
        print("No se pudieron extraer los planes. Revisa si la página de Movistar ha cambiado.")
```
Y obtenemos el resumen de la tabla :

| Plan                       | Precio/mes              | Internet  | Apps Ilimitadas    | Llamadas                         | SMS     |
| -------------------------- | ----------------------- | --------- | ------------------ | -------------------------------- | ------- |
| Plan Postpago 69.90        | S/69.90                 | Ilimitado | Internet Ilimitado | Ilimitadas Perú                  | 500 SMS |
| Plan Postpago 39.90        | S/39.90                 | Ilimitado | Apps x 12 meses    | Ilimitadas Perú, 350 min USA/CAN | 500 SMS |
| Plan Postpago 49.90        | S/49.90                 | Ilimitado | Apps x 12 meses    | Ilimitadas Perú, 400 min USA/CAN | 500 SMS |
| Plan Postpago 59.90        | S/59.90                 | Ilimitado | Apps x 12 meses    | Ilimitadas Perú                  | 500 SMS |
| Plan Postpago 79.90        | S/79.90                 | Ilimitado | Internet Ilimitado | Ilimitadas Perú                  | 500 SMS |
| Plan Postpago 99.90        | S/99.90                 | Ilimitado | Internet Ilimitado | Ilimitadas Perú                  | 500 SMS |
| Ahorra 50% 49.95           | S/49.95 (antes S/99.90) | 135 GB    | Internet Ilimitado | Ilimitadas Perú                  | 500 SMS |
| Ahorra 50% 39.95           | S/39.95 (antes S/79.90) | 120 GB    | Internet Ilimitado | Ilimitadas Perú                  | 500 SMS |
| Ahorra 50% 34.95           | S/34.95 (antes S/69.90) | 100 GB    | Internet Ilimitado | Ilimitadas Perú                  | 500 SMS |
| Plan Postpago 59.90 (30GB) | S/59.90                 | 30 GB     | Apps x 12 meses    | Ilimitadas Perú                  | 500 SMS |
| Plan Postpago 49.90 (30GB) | S/49.90                 | 30 GB     | Apps x 12 meses    | Ilimitadas Perú, 400 min USA/CAN | 500 SMS |
| Plan Postpago 39.90 (30GB) | S/39.90                 | 30 GB     | Apps x 12 meses    | Ilimitadas Perú, 350 min USA/CAN | 500 SMS |
| Ahorra 20% 55.92           | S/55.92 (antes S/69.90) | Ilimitado | Internet Ilimitado | Ilimitadas Perú, 350 min USA/CAN | 500 SMS |
| Ahorra 20% 63.92           | S/63.92 (antes S/79.90) | Ilimitado | Internet Ilimitado | Ilimitadas Perú                  | 500 SMS |
| Ahorra 20% 79.92           | S/79.92 (antes S/99.90) | Ilimitado | Internet Ilimitado | Ilimitadas Perú                  | 500 SMS |


# 📱Web scraping de Planes Claro Perú
Este proyecto hace scraping de los planes postpago de Claro Perú y extrae:
- Nombre del plan
- Precio
- Datos de internet
- Apps incluidas
- Minutos de llamadas
- SMS

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
## Código Web Scrapping Claro
```bash
# --- PASO 1: INSTALAR LAS LIBRERÍAS NECESARIAS EN GOOGLE COLAB ---
# ¡IMPORTANTE!: Ejecuta esta celda al inicio de tu notebook.
# Esto intentará suprimir los mensajes de instalación.
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
from webdriver_manager.chrome import ChromeDriverManager

# Importar para mostrar HTML en Colab
from IPython.display import display, HTML

def extract_claro_plans_colab():
    """
    Extracts post-paid plan information from Claro Peru's website.
    It uses Selenium for dynamic content and BeautifulSoup for HTML parsing.
    Returns a list of dictionaries, with plans sorted by price and without duplicates.
    """
    url = "https://www.claro.com.pe/personas/movil/postpago/"
    plans_data = []
    processed_plans = set()  # To store (name, price) tuples to prevent duplicates

    # --- SELENIUM CONFIGURATION FOR COLAB ---
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')           # Runs Chrome without a visible window
    options.add_argument('--no-sandbox')         # Necessary for Linux environments like Colab
    options.add_argument('--disable-dev-shm-usage') # Prevents memory issues in some environments
    options.add_argument('--window-size=1920,1080') # Common resolution for better element loading
    options.add_argument('--log-level=3')        # Suppresses most Chrome browser log messages

    driver = None

    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        driver.get(url)

        # --- WAIT FOR DYNAMIC CONTENT TO LOAD ---
        wait = WebDriverWait(driver, 20)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'cA1PEBodyCardWrap')))
        time.sleep(5) # Give extra time for full content rendering

        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')

        plan_elements = soup.find_all('div', class_='cA1PEBodyCardWrap')

        if not plan_elements:
            # This is the only error message that will appear if no plan elements are found.
            print("ERROR: No plan elements found on the page. The HTML structure might have changed.")
            return []

        for plan_element in plan_elements:
            name = plan_element.get('data-badge', 'N/A')
            price_str = plan_element.get('data-price', 'N/A')
            try:
                price = float(price_str)
            except ValueError:
                price = 'N/A'

            plan_key = (name, price)
            if plan_key in processed_plans:
                continue
            processed_plans.add(plan_key)

            gigas = 'N/A'
            unlimited_apps = 'N/A'
            calls_sms = 'N/A'

            # --- GIGAS EXTRACTION ---
            gigas_tag = plan_element.find('span', class_='number')
            if gigas_tag:
                gigas_text = gigas_tag.get_text(strip=True)
                if gigas_text.upper().endswith('GB'):
                    gigas = gigas_text
                else:
                    gigas = gigas_text + ' GB'

            # --- SPECIFIC HANDLING FOR "MAX ILIMITADO" PLANS ---
            is_max_ilimitado_promo = False
            promo_div = plan_element.find('div', class_='cardPePromo')
            if promo_div:
                promo_text_span = promo_div.find('span', string=lambda text: text and 'Gigas, Minutos y SMS' in text)
                if promo_text_span:
                    is_max_ilimitado_promo = True
                    calls_sms = "Ilimitadas"
                    unlimited_apps = "Incluidas en Todo Ilimitado"

            # --- GENERAL EXTRACTION (if not a specific "Max Ilimitado" promo plan) ---
            if not is_max_ilimitado_promo:
                apps_list = []
                app_icon_tags = plan_element.find_all('i', class_=lambda x: x and 'cIco-rs-' in x)
                for icon_tag in app_icon_tags:
                    for cls in icon_tag.get('class', []):
                        if 'cIco-rs-' in cls:
                            app_name = cls.replace('cIco-rs-', '')
                            apps_list.append(app_name.capitalize())
                unlimited_apps = ", ".join(apps_list) if apps_list else 'N/A'

                span_element_with_text = plan_element.find('span', string=lambda text: text and 'Llamadas y SMS' in text.strip())
                if span_element_with_text:
                    dt_parent = span_element_with_text.find_parent('dt')
                    if dt_parent:
                        dd_element = dt_parent.find_next_sibling('dd')
                        if dd_element:
                            calls_sms = dd_element.get_text(strip=True)

            plans_data.append({
                'Nombre del Plan': name,
                'Precio (S/)': price,
                'Gigas': gigas,
                'Apps Ilimitadas': unlimited_apps,
                'Llamadas y SMS': calls_sms
            })

    except Exception as e:
        # This is the only place a critical error message will be printed.
        print(f"An unexpected error occurred during extraction: {e}")
        return []
    finally:
        if driver:
            driver.quit()

    sorted_plans = sorted(plans_data, key=lambda x: x['Precio (S/)'] if isinstance(x['Precio (S/)'], (int, float)) else float('inf'))
    return sorted_plans

if __name__ == "__main__":
    plans = extract_claro_plans_colab()

    if plans:
        df = pd.DataFrame(plans)

        # Custom CSS for the HTML table
        html_style = """
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; background-color: #f4f4f4; color: #333; }
            h1 { color: #E4002B; text-align: center; margin-bottom: 20px; } /* Claro red */
            table {
                width: 100%;
                border-collapse: collapse;
                margin-top: 20px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.15); /* More pronounced shadow */
                background-color: #fff;
                border-radius: 8px; /* Rounded corners for the table */
                overflow: hidden; /* Ensures rounded corners apply to content */
            }
            th, td {
                padding: 15px 20px; /* More padding */
                text-align: left;
                border-bottom: 1px solid #eee; /* Lighter border */
            }
            th {
                background-color: #E4002B; /* Claro red for headers */
                color: white;
                text-transform: uppercase;
                font-size: 0.95em;
                letter-spacing: 0.5px;
            }
            tr:nth-child(even) {
                background-color: #f8f8f8; /* Slightly different shade for even rows */
            }
            tr:hover {
                background-color: #f0f0f0; /* Subtle hover effect */
            }
            /* Style for the header line */
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

        # Generate the HTML table from the DataFrame
        # Using escape=False to allow HTML entities if any, but generally good for plain text
        html_table = df.to_html(index=False, escape=False, classes='claro-plans-table')

        # Combine all parts into a full HTML document
        full_html_output = f"""
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Planes y Beneficios Claro Perú</title>
            {html_style}
        </head>
        <body>
            <div class="header-line">--- Planes y Beneficios (ordenados por precio, sin duplicados) ---</div>
            {html_table}
        </body>
        </html>
        """

        # Display the HTML directly in the Colab output cell
        display(HTML(full_html_output))
    else:
        # This message will only appear if the extraction function returns an empty list
        # (meaning an error occurred and was printed by the function itself).
        pass # No additional print here to keep output clean if error already printed
```
Y obtenemos el resumen de la tabla :
| Plan                 | Precio/mes | Internet en Alta Velocidad | Apps Ilimitadas                                   | Llamadas y SMS |
| -------------------- | ---------- | -------------------------- | ------------------------------------------------- | -------------- |
| Max 29.90            | S/29.90    | 10 GB                      | Facebook, Instagram, Threads, WhatsApp            | Ilimitadas     |
| Max 39.90            | S/39.90    | 25 GB                      | Facebook, Instagram, Threads, WhatsApp            | Ilimitadas     |
| Max 49.90            | S/49.90    | 45 GB                      | Facebook, Instagram, Messenger, Threads, WhatsApp | Ilimitadas     |
| Max 55.90            | S/55.90    | 75 GB                      | Facebook, Instagram, Messenger, Threads, WhatsApp | Ilimitadas     |
| Max Ilimitado 69.90  | S/69.90    | 110 GB                     | Incluidas en Todo Ilimitado                       | Ilimitadas     |
| Max Ilimitado 79.90  | S/79.90    | 125 GB                     | Incluidas en Todo Ilimitado                       | Ilimitadas     |
| Max Ilimitado 95.90  | S/95.90    | 135 GB                     | Incluidas en Todo Ilimitado                       | Ilimitadas     |
| Max Ilimitado 109.90 | S/109.90   | 160 GB                     | Incluidas en Todo Ilimitado                       | Ilimitadas     |
| Max Ilimitado 159.90 | S/159.90   | 175 GB                     | Incluidas en Todo Ilimitado                       | Ilimitadas     |
| Max Ilimitado 189.90 | S/189.90   | 185 GB                     | Incluidas en Todo Ilimitado                       | Ilimitadas     |
| Max Ilimitado 289.90 | S/289.90   | 200 GB                     | Incluidas en Todo Ilimitado                       | Ilimitadas     |


---

## Colaboradores

¡Agradecemos a todos los que han contribuido a este proyecto!

* [ron-62](https://github.com/ron-62) (Alonso Coronado de la Vega)
* [@usuario2](https://github.com/usuario2) (Nombre Real 2)
* [@usuario3](https://github.com/usuario3) (Nombre Real 3)
