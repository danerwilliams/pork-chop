#!/usr/bin/env python3


# Imports

import os
import json
import requests
import re
import csv

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

with open("custom_training.json", "r") as f:
    training_data = json.loads(f.read())

with open(".secrets", "r") as f:
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

def train_bot_list(data: list):

    trainer = ListTrainer(bot)

    for conversation in data:
        trainer.train(conversation)


def train_bot_corpus():

    trainer = ChatterBotCorpusTrainer(bot)
    trainer.train('chatterbot.corpus.english')


def train_bot_csv(path: str):

    csvfile = open(path)
    conversation = flatten(csv.reader(csvfile))
    train_bot_list(list(conversation))


def flatten(sequence):
    for iterable in sequence:
        for element in iterable:
            yield element


def reply(message: str):
    
    url = 'https://api.groupme.com/v3/bots/post'

    post = {
        'bot_id': bot_id,
        'text': bot.get_response(message)
    }

    request = Request(url, urlencode(post).encode())
    json = urlopen(request).read().decode()


def bot_message(post_req):
    return post_req['sender_type'] == 'bot'


# Main Function

def main():
    
    # Training
    train_bot_corpus()
    train_bot_list(training_data)
    train_bot_csv('coderquadszn2.csv')
    train_bot_csv('eboard.csv')

    # Run with flask
    app.run(host='0.0.0.0', port=80)


# Run Main

if __name__ == '__main__':
    main()
