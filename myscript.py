from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import os

# إعدادات المتصفح للعمل بدون واجهة (Headless)
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
# تحديد مسار تحميل الملفات ليكون مجلد العمل الحالي
prefs = {"download.default_directory": os.getcwd()}
chrome_options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(options=chrome_options)

def download_files():
    try:
        # 1. الذهب والنفط (Investing)
        # ملاحظة: زر التحميل في Investing يتطلب أحياناً تسجيل دخول، 
        # لذا سنقوم بسحب الجدول مباشرة إذا تعذر النقر
        for url in [
            "https://sa.investing.com/commodities/gold-historical-data",
            "https://sa.investing.com/commodities/brent-oil-historical-data"
        ]:
            driver.get(url)
            time.sleep(15) # انتظار تحميل الجدول
            # سحب الجدول وتحويله لـ CSV
            table = driver.find_element(By.TAG_NAME, "table")
            with open("data_" + url.split('/')[-2] + ".csv", "w", encoding="utf-8") as f:
                f.write(table.text)
            print(f"تم حفظ بيانات من {url}")

        # 2. البنك المركزي (CBE)
        driver.get("https://www.cbe.org.eg/ar/economic-research/statistics/cbe-exchange-rates/historical-data")
        time.sleep(15)
        # البحث عن زر التحميل (بناءً على التنسيق المعتاد للموقع)
        download_button = driver.find_element(By.LINK_TEXT, "تحميل بواسطة Excel")
        download_button.click()
        time.sleep(5)
        print("تم بدء تحميل ملف البنك المركزي")

    finally:
        driver.quit()

if __name__ == "__main__":
    download_files()
