import requests

def kanye_handler():
    '''Gives a random Kanye West quote.'''

    url="https://api.kanye.rest/"

    r = requests.get(url)
    if r.status_code == 200:
        quote = r.json()['quote']
        return f"'{quote}' - Kanye West"
    else:
        return f"Error {r.status_code} - could not retrieve quote"


