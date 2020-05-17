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
    
    stock_html = requests.get(url).text
        
    price = re.search(r'currentPrice.*?({.*?})', stock_html)
    change = re.search(r'regularMarketChangePercent.*?({.*?})', stock_html)
    if price:
        price = json.loads(price.group(1))['raw']
        change = json.loads(change.group(1))['raw']
        response = '$' + str(price) + ' ({:.2f})'.format(change) + '%'
        if '-' in response:
            return response + ' 📉'
        return response + ' 📈'

    return 'Could not get ' + symbol + ' price'
