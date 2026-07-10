import pandas as pd
from playwright.sync_api import sync_playwright

def get_data(url, csv_name):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        page.wait_for_selector('table')
        
        html = page.content()
        df = pd.read_html(html)[0]
        
        df.to_csv(csv_name, index=False)
        print(f"Saved {csv_name}")
        browser.close()

get_data('https://sa.investing.com/commodities/gold-historical-data', 'gold.csv')
get_data('https://sa.investing.com/commodities/brent-oil-historical-data', 'oil.csv')
get_data('https://www.cbe.org.eg/ar/economic-research/statistics/cbe-exchange-rates/historical-data', 'cbe.csv')
