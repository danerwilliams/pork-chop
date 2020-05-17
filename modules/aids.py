import json

def aids_handler(sender, message, bot_id, app_id):
    """Give aids to a user"""
    usage = "Give aids to a user.\n\
             usage: !aids <user>\n\
             Get Number of aids\n\
             usage: !aids\n\
             See aids History\n\
             usage: !aids list"

    message = message.strip().split()
    if len(message) > 1:
        if message[1] == 'list':
            return aidsList()
        writeAids(message[1:])
        return "{} has aids.".format(' '.join(message[1:]))
    else:
        return "{} has gotten aids {} times".format(sender,getN(sender))
    return None

def getN(user):
    user = ''.join(user)
    with open('aidsHistory.json', 'r') as f:
        history = json.load(f)
    if user in history:
        return history[user]
    return 0

def writeAids(user):
    user = ' '.join(user)
    with open('aidsHistory.json', 'r') as f:
        history = json.load(f)

    if user in history:
        history[user] = int(history[user]) + 1
    else:
        history[user] = '1'

    with open('aidsHistory.json', 'w') as f:
        json.dump(history, f)
    
    

def aidsList():
    historyStr = []
    with open('aidsHistory.json', 'r') as f:
        history = json.load(f)

    for name in history:
        historyStr.append(name+' '+str(history[name]))
    
    return '\n'.join(historyStr)


if __name__ == '__main__':
    print('Test aids')
    print(aids_handler('Cheeks','!aids woody',' ',' '))
    print(aids_handler('Cheeks','!aids woody',' ',' '))

    print('Test self count')
    print(aids_handler('Woody','!aids',' ',''))
    print ('Test list')
    print(aids_handler('Cheeks','!aids list',' ',''))