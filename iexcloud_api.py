import requests

url = 'https://cloud.iexapis.com/stable/stock/aapl/chart/3m?token=pk_1cd4889a6bbd49d8a8c3576f0c0e3fcf'

response = requests.get(url)

data = response.json()