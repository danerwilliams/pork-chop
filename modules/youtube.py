#!/usr/bin/env python3

import requests
import os
import json


def youtube_handler(message):

    if os.path.isfile('.secrets'):
        with open('.secrets', 'r') as f:
            secrets = json.loads(f.read())
            try:
                API_KEY = secrets['YOUTUBE_API_KEY']
            except KeyError:
                return 'YouTube API key not present in .secrets'
    else: # otherwise try environment variables
        try:
            API_KEY = os.environ['YOUTUBE_API_KEY']
        except KeyError:
            return "YouTube API key not present in environment"

    search = '+'.join(message.split()[1:])
    if not search:
        return('Usage: !yt <search>')

    api_url = f'https://www.googleapis.com/youtube/v3/search'
    api_params = {
        'key': API_KEY,
        'type': 'video',
        'part': 'snippet',
        'q': search
    }

    results = requests.get(api_url, params=api_params)
    if results.status_code != 200:
        return(f'Error {results.status_code}!')
    results = json.loads(results.text)

    video_url = 'https://www.youtube.com/watch' 
    video_id = results["items"][0]["id"]["videoId"] 
    
    if not video_id:
        return(f'No results found :( please try a different query')

    return(video_url + '?v=' + video_id)
