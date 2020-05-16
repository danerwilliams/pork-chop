import json

def usage_handler(message):
    '''Have pork chop display all enabled commands'''
    usage = '''Say pork chops name and he will respond. 

    Boss pork chop around with these commands:
    '''

    # load config file
    f = open("config.json", "r")
    config = json.loads(f.read())
    ignore = config['ignore_modules']

    # add to usage string everything not specified to be ignored in config.json
    with open("README.md") as f:
        commands = []
        for line in f:
            line = line.strip()
            # isolate lines of readme describing the modules
            if ('* !' in line) & (not line.split()[1]):
                commands.append(line.replace('\\', ''))
    
    return usage + '\n '.join(commands)
