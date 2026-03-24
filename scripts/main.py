import pandas as pd
import requests

# Extact datas from API
url = "https://dummyjson.com/products"
response = requests.get(url)

data = response.json()

#Take datas from API
products = data['products']

#Change data frame
df = pd.DataFrame(products) 



print("=== DATA FROM API ===")
print(df.head())