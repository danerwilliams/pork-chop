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


# Globals

bot_name = 'Pork Chop'
app = Flask(__name__)
bot = ChatBot(bot_name)
prev_message = None
message_count = 0

f = open("custom_training.json", "r")
training_data = json.loads(f.read())

f = open(".secrets", "r")
secrets = json.loads(f.read())
bot_id = secrets['bot_id']


# Flask Setup

@app.route('/bot', methods=['POST'])
def Pork_Chop():
    
    global message_count
    global prev_message

    post_req = request.get_json()
    
    sender = post_req['name']
    message = post_req['text']
    
    print(message)

    # Reply if not from another bot and name is mentioned
    if (not bot_message(post_req)) & (bot_name.lower() in message.lower()):
        reply(message)
        
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



# HTTP Reqs
def reply(message: str):
    
    url = 'https://api.groupme.com/v3/bots/post'

    post = {
        'bot_id': bot_id,
        'text': bot.get_response(message)
    }

    request = Request(url, urlencode(post).encode())
    json = urlopen(request).read().decode()


# Utilities
def bot_message(post_req):
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
    parser.add_argument('-t', '--train', help='Train bot from data', action = 'store_true')
    parser.add_argument('-d', '--deploy', help='Deploy bot with flask on port 80', action = 'store_true')
    args = parser.parse_args()

    # Training
    if args.train:
        #train_bot_corpus()
        train_bot_csv('coderquadszn2.csv', args.cores)
        train_bot_csv('eboard.csv', args.cores)

    # Run with flask
    if args.deploy:
        app.run(host='0.0.0.0', port=80)


# Run Main

if __name__ == '__main__':
    main()
