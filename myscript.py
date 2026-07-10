import requests
import pandas as pd
from datetime import datetime

# إعدادات المتصفح للتمويه
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

def scrape_data():
    # 1. سحب بيانات الذهب
    try:
        print("Scraping Gold data...")
        url_gold = 'https://sa.investing.com/commodities/gold-historical-data'
        df_gold = pd.read_html(requests.get(url_gold, headers=headers).text)[0]
        df_gold[['التاريخ', 'الأخير']].to_csv('gold_data.csv', index=False)
        print("Gold saved!")
    except Exception as e: print(f"Gold Error: {e}")

    # 2. سحب بيانات النفط
    try:
        print("Scraping Oil data...")
        url_oil = 'https://sa.investing.com/commodities/brent-oil-historical-data'
        df_oil = pd.read_html(requests.get(url_oil, headers=headers).text)[0]
        df_oil[['التاريخ', 'الأخير']].to_csv('oil_data.csv', index=False)
        print("Oil saved!")
    except Exception as e: print(f"Oil Error: {e}")

    # 3. سحب بيانات الدولار (البنك المركزي)
    try:
        print("Scraping Dollar data...")
        url_cbe = 'https://www.cbe.org.eg/ar/economic-research/statistics/cbe-exchange-rates/historical-data'
        df_cbe = pd.read_html(requests.get(url_cbe, headers=headers).text)[0]
        # ملاحظة: تأكد من اسم العمود بدقة كما يظهر في موقع البنك
        df_cbe[['التاريخ', 'سعر البيع']].to_csv('cbe_exchange_rate.csv', index=False)
        print("Dollar saved!")
    except Exception as e: print(f"Dollar Error: {e}")

if __name__ == "__main__":
    scrape_data()
