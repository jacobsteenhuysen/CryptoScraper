import pandas as pd
# import datetime as datetime
# from datetime import date, timedelta
from cryptocmd import CmcScraper

df = pd.read_excel('C:/Users/Jacob Steenhuysen/Downloads/Crypto Tickers.xlsx', sheet_name='Sheet1')

tickers_list = df['Ticker'].tolist()
data = pd.DataFrame(columns=tickers_list)

# import yfinance as yf
# #for ticker in tickers_list:
# #    data[ticker] = yf.download(ticker, period="5d", interval="1d") ["Close"]

# for ticker in tickers_list:
#     data[ticker] = yf.download(ticker, start=datetime.date(2020, 3, 17), end=datetime.date(2021, 3, 17), actions = True) ["Adj Close"]


# headers, data = scraper.get_data()
for ticker in tickers_list:
    data[ticker] = CmcScraper(ticker, "17-03-2020", "17-03-2021",).get_dataframe()["Close"]

#print(data)
export_excel = data.to_excel(r'C:/Users/Jacob Steenhuysen/Downloads/Top 100 Crypto Returns For Volatility3.xlsx', sheet_name='Sheet1', index= True)
