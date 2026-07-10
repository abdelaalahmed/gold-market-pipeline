import requests
import pandas as pd
from io import StringIO

# هذه الهوية تجعل الموقع يظن أننا متصفح حقيقي وليست أداة برمجية
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'Accept-Language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7'
}

def fetch_data(url, filename):
    print(f"Trying to fetch from: {url}")
    try:
        # 1. محاولة السحب
        response = requests.get(url, headers=headers)
        
        # 2. تحويل النص لجدول
        # ملاحظة: سنستخدم html5lib لأنه الأقوى في التعامل مع الجداول المعقدة
        dfs = pd.read_html(StringIO(response.text), flavor='html5lib')
        
        if dfs:
            df = dfs[0]
            df.to_csv(filename, index=False)
            print(f"Success! Data saved to {filename}")
        else:
            print(f"Failed to find tables in {url}")
            
    except Exception as e:
        print(f"Error fetching {url}: {e}")

# تنفيذ السحب للمواقع الثلاثة
# الذهب
fetch_data('https://sa.investing.com/commodities/gold-historical-data', 'gold_data.csv')
# النفط
fetch_data('https://sa.investing.com/commodities/brent-oil-historical-data', 'oil_data.csv')
# البنك المركزي
fetch_data('https://www.cbe.org.eg/ar/economic-research/statistics/cbe-exchange-rates/historical-data', 'cbe_data.csv')
