import json

def usage_handler(message):
    '''Have pork chop display all enabled commands'''
    
    usage = 'Say pork chops name and he will respond.\n\nPork Chop will also reply to these commands:\n\n'

    # load config file
    with open("config.json", "r") as f:
        config = json.loads(f.read())
        ignore = config['ignore_modules']

    print(ignore)

    # add to usage string everything not specified to be ignored in config.json
    with open("README.md") as f:
        commands = []
        for line in f:
            line = line.strip()
            # isolate lines of readme describing the modules
            if '* !' in line:
                if not line.split()[1] in ignore:
                    commands.append(line[line.find('!'):].replace('\\', ''))
    
    return usage + '\n'.join(commands)
