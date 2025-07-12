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
