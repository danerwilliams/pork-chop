import requests

def joke_handler(message):
    '''Gives a random joke.'''

    url="https://official-joke-api.appspot.com/jokes/random"
    r = requests.get(url)

    if r.status_code == 200:
        joke = r.json()
        return f">{joke['setup']} . . . {joke['punchline']}"
    else:
        return f"Error {r.status_code}: could not retrieve joke"


