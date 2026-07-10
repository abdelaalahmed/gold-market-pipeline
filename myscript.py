import sys
print("Python is working perfectly!")
try:
    import bs4
    import requests
    import pandas
    print("All libraries are installed and ready!")
except ImportError as e:
    print(f"Error: {e}")