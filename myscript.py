from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

# إعدادات المتصفح ليعمل في GitHub Actions
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

def download_data():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    
    # 1. الذهب
    print("Downloading Gold...")
    driver.get("https://sa.investing.com/commodities/gold-historical-data")
    time.sleep(10) # انتظار تحميل الصفحة
    # هنا قد تحتاج لإضافة كود النقر على زر التحميل (Download) إذا لزم الأمر
    
    # 2. النفط
    print("Downloading Oil...")
    driver.get("https://sa.investing.com/commodities/brent-oil-historical-data")
    time.sleep(10)
    
    # 3. البنك المركزي
    print("Downloading CBE Data...")
    driver.get("https://www.cbe.org.eg/ar/economic-research/statistics/cbe-exchange-rates/historical-data")
    time.sleep(10)
    
    driver.quit()
    print("Download process completed.")

if __name__ == "__main__":
    download_data()
