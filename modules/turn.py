import json

def turn_handler(message):
    message = message.strip().split()
    if len(message) > 1:
        if message[1] == 'list':
            return turnList()
        writeTurn(message[1:])
        return "{} got turned.".format(' '.join(message[1:]))
    else:
        return "{} has been turned {} times".format(sender,getN(sender))
    return None

def getN(user):
    user = ''.join(user)
    with open('turnHistory.json', 'r') as f:
        history = json.load(f)
    if user in history:
        return history[user]
    return 0

def writeTurn(user):
    user = ' '.join(user)
    with open('turnHistory.json', 'r') as f:
        history = json.load(f)

    if user in history:
        history[user] = int(history[user]) + 1
    else:
        history[user] = '1'

    with open('turnHistory.json', 'w') as f:
        json.dump(history, f)
    
def turnList():
    historyStr = []
    with open('turnHistory.json', 'r') as f:
        history = json.load(f)

    for name in history:
        historyStr.append(name+' '+str(history[name]))
    
    return '\n'.join(historyStr)

