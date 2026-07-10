import pandas as pd
from playwright.sync_api import sync_playwright

def get_data(url, csv_name):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        # انتظار الجدول ليظهر (قد تحتاج لزيادة وقت الانتظار حسب سرعة الموقع)
        page.wait_for_selector('table')
        
        # استخراج محتوى الـ HTML للجدول
        html = page.content()
        df = pd.read_html(html)[0]
        
        df.to_csv(csv_name, index=False)
        print(f"Saved {csv_name}")
        browser.close()

# الروابط التي أرسلتها
get_data('https://sa.investing.com/commodities/gold-historical-data', 'gold.csv')
get_data('https://sa.investing.com/commodities/brent-oil-historical-data', 'oil.csv')
# بالنسبة للبنك المركزي، الرابط قد يحتاج معالجة إضافية بسبب الفلتر
get_data('https://www.cbe.org.eg/ar/economic-research/statistics/cbe-exchange-rates/historical-data', 'cbe.csv')
