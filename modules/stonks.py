#!/usr/bin/env python3
import requests
import re
import json
#from bs4 import BeautifulSoup


def stonks_handler(message):
    '''Pork Chop gives you stock info by scraping yahoo finance'''

    url = 'https://finance.yahoo.com/quote/'
    symbol = message.split()[1]

    if symbol:
        url += symbol
    else:
        return '!stonks <symbol>'
    response  = requests.get(url)
    if url != response.url:
        return 'Could not get ' + symbol + ' price' 
    stock_html = response.text
    price = re.search(r'regularMarketPrice.*?({.*?})', stock_html)
    change = re.search(r'regularMarketChangePercent.*?({.*?})', stock_html)
    if price:
        price = json.loads(price.group(1))['raw']
        change = json.loads(change.group(1))['raw']
        reply = '$' + str(price) + ' / ' + ('' if change < 0 else '+') + '{:.2f}'.format(change) + '%'
        if change < 0:
            return reply + ' 📉'
        return reply + ' 📈'
    return 'Could not get ' + symbol + ' price'
