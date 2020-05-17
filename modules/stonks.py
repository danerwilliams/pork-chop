import requests
import re


def stonks_handler(message):
    '''Pork Chop gives you stock info by scraping yahoo finance'''

    url = 'https://finance.yahoo.com/quote/'
    symbol = message.split()[1]

    if symbol:
        url += symbol
    else:
        return '!stonks <symbol>'
    
    stock_html = requests.get(url).text
    price = re.search(r'data-reactid="50">([0-9]+\.[0-9]{2})</span>', stock_html)
    change = re.search(r'data-reactid="51">(.*?)</span>', stock_html)
    print(price) 
    if price:
        return '$' + price.group(1) + ' / ' + change.group(1)

    return 'Could not find stock info'
        
