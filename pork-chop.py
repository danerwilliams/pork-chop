#!/usr/bin/env python3


# Imports

import os
import json
import requests
import re
import csv
import hashlib
import string
import sys
import argparse
import concurrent.futures

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import UbuntuCorpusTrainer
from chatterbot.trainers import ListTrainer

from importlib import reload
from modules.usage import usage_handler


# Globals

bot_name = 'Pork Chop'
app = Flask(__name__)
bot = ChatBot(bot_name)

f = open(".secrets", "r")
secrets = json.loads(f.read())
bot_id = secrets['bot_id']


# Flask Setup

@app.route('/bot', methods=['POST'])
def Pork_Chop():

    post_req = request.get_json()
    
    sender = post_req['name']
    message = post_req['text']

    # Conversation
    # Reply if not from another bot and name is mentioned
    if (not is_bot_message(post_req)) & (bot_name.lower() in message.lower()):
        filtered_message = message.lower().replace(bot_name.lower(), '') #filters out pork chop's name for more accurate responses
        reply(filtered_message)

    # handle command if not conversation
    elif message.rstrip()[0] == '!':
        command_handler(message)

    return "ok", 200


# Functions

# Training
def train_bot_corpus():

    trainer = ChatterBotCorpusTrainer(bot)
    trainer.train('chatterbot.corpus.english')

def train_bot_csv(path: str, cores: int):

    csvfile = open(path)
    conversation = list(flatten(csv.reader(csvfile)))
    trainer = ListTrainer(bot)
    
    if cores > 1:
        with concurrent.futures.ProcessPoolExecutor(cores) as executor:
            executor.map(trainer.train, conversation)
    else:
        trainer.train(conversation)

def train_bot_ubuntu():

    trainer = UbuntuCorpusTrainer(bot)
    trainer.train()


# HTTP Reqs
def reply(message: str):
    
    url = 'https://api.groupme.com/v3/bots/post'

    post = {
        'bot_id': bot_id,
        'text': bot.get_response(message)
    }

    request = Request(url, urlencode(post).encode())
    json = urlopen(request).read().decode()


# handle modules
def command_handler(message):

    command = message.split()[0]

    modules = {
        '!usage': usage_handler
    }

    # Exclude modules based on config.json
    

    handler = modules[command]

    if handler:
        return handler(message, bot_id)
    else:
        return None


# Utilities
def is_bot_message(post_req):
    return post_req['sender_type'] == 'bot'

def flatten(sequence):
    for iterable in sequence:
        for element in iterable:
            yield element


# Main Function

def main():

    # Parse Args
    parser = argparse.ArgumentParser(prog='hulk')
    parser.add_argument('-c', '--cores', help='Number of CPU cores to use', type=int, default=1)
    parser.add_argument('-t', '--train', help='Train bot from csv data files', type=list, default=[])
    parser.add_argument('-d', '--deploy', help='Deploy bot with flask on port 80 (requires sudo)', action = 'store_true')
    parser.add_argument('-u', '--ubuntu', help='Train bot from ubuntu corpus', action = 'store_true')
    parser.add_argument('-e', '--english', help='Train bot from english corpus', action = 'store_true')
    args = parser.parse_args()

    # Training
    if args.train:
        for file in args.train:
            train_bot_csv(file, args.cores)
    if args.english:
        train_bot_corpus()
    if args.ubuntu:
        train_bot_ubuntu()

    # Run with flask
    if args.deploy:
        app.run(host='0.0.0.0', port=80)


# Run Main

if __name__ == '__main__':
    main()
