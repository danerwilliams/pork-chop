import json

def turn_handler(message):
    message = message.strip().split()
    if len(message) > 1:
        # list turns
        if message[1] == 'list':
            return turnList()
        # turn a user
        writeTurn(message[1:])
        return f"{''.join(message[1:])} got turned."
    
    return "specify a user with !turn <user> or use !turn list"

def writeTurn(user):
    user = ' '.join(user).lower()
    with open('data/turnHistory.json', 'r') as f:
        history = json.load(f)

    if user in history:
        history[user] = int(history[user]) + 1
    else:
        history[user] = '1'

    with open('data/turnHistory.json', 'w') as f:
        json.dump(history, f)

def turnList():
    with open('data/turnHistory.json', 'r') as f:
        history = json.load(f)
    return "\n".join( f"{name} {num}" for name, num in history.items())

