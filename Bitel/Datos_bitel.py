
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
