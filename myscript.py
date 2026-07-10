import yfinance as yf
import pandas as pd

def scrape_all():
    # جدول البيانات (الرموز العالمية المعتمدة للأسعار)
    # GC=F : الذهب
    # BZ=F : نفط برنت
    # USDEGP=X : الدولار مقابل الجنيه المصري
    assets = {
        "gold_data.csv": "GC=F",
        "oil_data.csv": "BZ=F",
        "dollar_egp.csv": "USDEGP=X"
    }
    
    for filename, ticker in assets.items():
        try:
            print(f"Fetching {ticker}...")
            # تحميل بيانات آخر شهر
            df = yf.download(ticker, period="1mo", interval="1d")
            
            if not df.empty:
                df.to_csv(filename)
                print(f"Successfully saved {filename}")
            else:
                print(f"No data found for {ticker}")
        except Exception as e:
            print(f"Error fetching {ticker}: {e}")

    # بخصوص البنك المركزي (CBE):
    # الموقع محمي جداً ضد البوتات ولا يعطي جداول مباشرة للـ Python
    # يفضل الاعتماد على USDEGP=X فهي تعطي سعر السوق الحقيقي والمحدث
    print("Market data collection complete.")

if __name__ == "__main__":
    scrape_all()
