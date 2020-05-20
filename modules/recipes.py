import requests
import os
import json

def recipes_handler(message):
    message = message.split(' ',1)[1]

    print(message)
    
    # MANWICH (real ones know)
    if message.strip() == 'manwich':
        return 'https://open.spotify.com/playlist/1zLerOR4qEd25bOhcbE8V8?si=gXEYgWZvQd-UGZ_HAPShxw'

    # try loading from .secrets file
    if os.path.isfile('.secrets'):
        with open('.secrets', 'r') as f:
            secrets = json.loads(f.read())
            try:
                bot_id = secrets['SPOONACULAR_API_KEY']
            except KeyError:
                return 'Spoonacular API key not present in .secrets'
    else: # otherwise try environment variables
        try:
            key=os.environ['SPOONACULAR_API_KEY']
        except KeyError:
            return "Spoonacular API key not present in environment"

    #get recipe id
    url = "https://api.spoonacular.com/recipes/search"
    params = {"apiKey":key,
            "query":message,
            "number":1,
            "diet":"vegan",
            "limitLicense": True,
            "instructionsRequired": True
            }
    r = requests.get(url, params = params)
    if r.status_code != 200:
        return f"Error {r.status_code}. Could not retrieve recipie"

    data = r.json()['results'][0]
    if data:
        id = data['id']
        title = data['title']
    else:
        return "No results found :( please try a different query"

    #get recipe info
    url = f"https://api.spoonacular.com/recipes/{id}/information"
    r = requests.get(url, params = {"apiKey":key})
    if r.status_code != 200:
        return f"Error {r.status_code}. Could not retrieve recipie"

    data =r.json()

    recipe = [
            f"How to cook {title}.",
            f"by {data['creditsText']}",
            "\n"
            "You will need:"]

    ingredient_dict = data['extendedIngredients']
    recipe = recipe + [item['original'] for item in ingredient_dict] + ["\n"]
    step_dict = data["analyzedInstructions"][0]['steps']
    recipe = recipe + [f"{item['number']}) {item['step']}" for item in step_dict]

    return "\n".join(recipe)



