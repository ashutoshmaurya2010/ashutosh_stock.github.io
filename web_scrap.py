# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 11:38:15 2022

@author: Ashutosh
"""

import pandas as pd
import requests
from bs4 import BeautifulSoup

page  = requests.get("https://www.fool.com/investing/top-stocks-to-buy.aspx")
page
page.content


soup = BeautifulSoup(page.content, 'html.parser')
soup.prettify()


stocks = soup.find(class_='related-tickers')
stocks

stock_picks = stocks.find_all(class_='ticker-text-wrap')
stock_picks


# Get stock names
stock_names = []
for stock in stock_picks:
    stock_names.append(stock.h3.get_text())

stock_names





# Get stock symbol
stock_symbol = []
for stock in stock_picks:
    stock_symbol.append(stock.a.span.get_text())

stock_symbol


# Get Current Price
#stock names and symbols with prices



current_price = []
stock_symbol = []
stock_names = []
for stock in stock_picks:
    try:
        price = stock.aside.h4.get_text()
        current_price.append(price.strip())
        stock_symbol.append(stock.a.span.get_text())
        stock_names.append(stock.h3.get_text())
    except:
        next

current_price


price_change = stocks.find_all(class_='price-change-amount')
# Get Change Price
change_price = []
for change in price_change:
    price = change.get_text()
    change_price.append(price.strip())

change_price



percent_change = stocks.find_all(class_='price-change-percent')
# Get Change Percent
change_pct = []
for pct in percent_change:
    price = pct.get_text()
    change_pct.append(price.strip())

change_pct




data = {'Symbol':stock_symbol, 'Company':stock_names, 'Price':current_price, 'PriceChange':change_price, 'PercentChange':change_pct}
df = pd.DataFrame(data)










