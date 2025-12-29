Stock News Alert System (Python)

An intermediate-level Python automation project that tracks daily stock price movements and fetches related news when a significant change occurs.

---

Project Overview

This project monitors a selected stock’s daily closing price and calculates the percentage change between the last two trading days.  
If the price movement exceeds a predefined threshold (±5%), the system fetches the latest related news articles and displays them.

---

Technologies Used

- Python 3
- Alpha Vantage API (Stock Market Data)
- GNews API (Latest News Headlines)
- Requests Library

---

How It Works

1. Fetches daily stock price data
2. Extracts the last two closing prices
3. Calculates percentage change
4. Checks if the change is ≥ ±5%
5. If true, fetches top 3 related news articles
6. Displays results in the terminal

---



