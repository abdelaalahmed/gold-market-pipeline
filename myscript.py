import requests
import pandas as pd
from io import StringIO

# محاكاة متصفح حقيقي جداً
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Referer': 'https://www.google.com/',
    'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8'
}

def get_data(url, filename):
    print(f"--- جاري السحب من: {url} ---")
    try:
        response = requests.get(url, headers=headers, timeout=20)
        # نستخدم html5lib لأنه الأكثر قدرة على قراءة الجداول المعقدة
        tables = pd.read_html(StringIO(response.text), flavor='html5lib')
        
        if tables:
            df = tables[0]
            df.to_csv(filename, index=False)
            print(f"تم بنجاح حفظ: {filename}")
        else:
            print(f"تحذير: لم يتم العثور على جداول في الرابط: {url}")
            
    except Exception as e:
        print(f"خطأ أثناء السحب من {url}: {e}")

# تنفيذ السحب من مواقعك
get_data('https://sa.investing.com/commodities/gold-historical-data', 'gold_data.csv')
get_data('https://sa.investing.com/commodities/brent-oil-historical-data', 'oil_data.csv')
get_data('https://www.cbe.org.eg/ar/economic-research/statistics/cbe-exchange-rates/historical-data', 'cbe_data.csv')
