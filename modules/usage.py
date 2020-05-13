import json

def usage_handler(message):
    '''Have pork chop display all enabled commands'''
    usage = '''
    Say pork chops name and he will respond. 

    With auto reply enabled, pork chop will automatically reply when he's feeling confident, even if you don't say his name.

    Boss pork chop around with these commands:
    !usage - display available commands
    '''

    # load config file
    f = open("config.json", "r")
    config = json.loads(f.read())
    ignore = config['ignore_modules']

    # hard coded module usage definitions
    modules = {
        '!example': 'example module not to be included'
    }

    # add to usage string everything not specified to be ignored in config.json
    for mod in modules:
        if not mod in ignore:
            usage += f'\n{mod} - {modules[mod]}'


    return usage
