#!/usr/bin/env python3
# author: conor murphy, github.com/cnrmrphy

import requests
import os
import json

def reddit_handler(message):

    search = '+'.join(message.split()[1:])
    if not search:
        return('Usage: !reddit <search>')
    
    api_url = 'https://www.reddit.com/subreddits/search.json'
    api_params = {
        'include_over_18': 'on',
        'q': search,
    }
    headers = {
        'User-agent': 'pork-chop v1.0'
    }

    response = requests.get(api_url, params=api_params, headers=headers)
    if response.status_code != 200:
        return(f'Error {response.status_code}!')
    response = json.loads(response.text)

    sub_template = 'https://reddit.com'
    try:
        sub_link = response["data"]["children"][0]["data"]["url"]
    except IndexError:
        return(f'No results found :( please try a different query') 

    return(sub_template + sub_link)
