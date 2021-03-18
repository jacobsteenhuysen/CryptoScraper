import pandas as pd
from cryptocmd import CmcScraper

df = pd.read_excel('C:/Users/Jacob Steenhuysen/Downloads/Crypto Tickers.xlsx', sheet_name='Sheet1')

tickers_list = df['Ticker'].tolist()
data = pd.DataFrame(columns=tickers_list)

for ticker in tickers_list:
    data[ticker] = CmcScraper(ticker, "17-03-2020", "17-03-2021",).get_dataframe()["Close"]

export_excel = data.to_excel(r'C:/Users/Jacob Steenhuysen/Downloads/CryptoReturns.xlsx', sheet_name='Sheet1', index= True)
