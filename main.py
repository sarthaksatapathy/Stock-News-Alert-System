import requests
from config import ALPHA_VANTAGE_API_KEY, NEWS_API_KEY

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://gnews.io/api/v4/search"

#---------Stock Data----------

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": ALPHA_VANTAGE_API_KEY
}

stock_response = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_response.raise_for_status()
stock_data = stock_response.json()

daily_data = stock_data["Time Series (Daily)"]

data_list = [value for (key, value) in daily_data.items()]

yesterday_close = float(data_list[0]["4. close"])
day_before_close = float(data_list[1]["4. close"])

difference = yesterday_close - day_before_close
percentage_change = (difference / day_before_close) * 100

print(f"Stock Change: {abs(percentage_change):.2f}%")


# -------------------- NEWS DATA -------------------- #
if abs(percentage_change) >= 5:
    news_params = {
        "q": COMPANY_NAME,
        "lang": "en",
        "max": 3,
        "apikey": NEWS_API_KEY
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    articles = news_response.json()["articles"]

    for article in articles:
        print(article["title"])
        print(article["description"])
        print()
else:
    print("No significant stock movement. No news fetched.")