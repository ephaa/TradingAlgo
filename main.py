import yfinance as yf
from datetime import datetime, timedelta
import pytz


def get_stock_data(ticker):
    today = datetime.now(pytz.UTC).date()
    one_year_ago = today - timedelta(days=365)
    three_months_ago = today - timedelta(days=90)
    one_day_ago = today - timedelta(days=1)

    stock = yf.Ticker(ticker)
    data = stock.history(period="1y")

    data.index = data.index.tz_convert(None)

    data_past_year = data.loc[one_year_ago:]
    data_past_3_months = data.loc[three_months_ago:]
    data_past_day = data.loc[one_day_ago:]

    return data_past_year, data_past_3_months, data_past_day


ticker = "AAPL"
data_year, data_3_months, data_day = get_stock_data(ticker)

print("Past Year Data:")
print(data_year)
print("\nPast 3 Months Data:")
print(data_3_months)
print("\nPast Day Data:")
print(data_day)
