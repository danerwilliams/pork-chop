#!/usr/bin/env python3
import requests
import re
import json
from bs4 import BeautifulSoup


def stonks_handler(message):
    '''Pork Chop gives you stock info by scraping yahoo finance'''

    url = 'https://finance.yahoo.com/quote/'
    symbol = message.split()[1]

    if symbol:
        url += symbol
    else:
        return '!stonks <symbol>'
    
    stock_html = requests.get(url).text
    price = re.search(r'data-reactid="50">[0-9]+\.[0-9]{2}</span>', stock_html)
    change = re.search(r'data-reactid="51">(.*?)</span>', stock_html)
    print(price) 
    if price.group():
        return '$' + price.group(1) + ' / ' + change.group(1)

    return 'Could not find stock info'
        

def steemer_stonks(message):
    url = 'https://finance.yahoo.com/quote/aapl'
    
    stock_html = requests.get(url).text
    price = re.search(r'currentPrice.*?({.*?})', stock_html)
    change = re.search(r'regularMarketChangePercent.*?({.*?})', stock_html)
    if price.group():
        price = json.loads(price.group(1))['raw']
        change = json.loads(change.group(1))['raw']
        print('$' + str(price) + ' / ' + '{:.2f}'.format(change) + '%')
    # scripts = json.loads(re.search(r'currentPrice.*?({.*?})', stock_html).group(1))


    # scheme = scripts[0].json()
steemer_stonks('conor')