import yfinance as yf
tsla=yf.Ticker("TSLA")
tesla_data=tsla.history(period="max")
tesla_data.reset_index(inplace=True)
print(tesla_data.head(100))