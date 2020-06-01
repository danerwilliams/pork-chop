# pork-chop

> An AI chat bot

<p align="center">
  <img width="350" height="513" src="./groupme_screenshot.png">
</p>

## Conversations

We use [ChatterBot](https://github.com/gunthercox/ChatterBot), a machine learning conversational dialog engine to power Pork Chop's conversations.

### Training

Pork Chop has a few options for training:
* Train with csv data - The success and training time with this is dependent on the size and quality of the data you provide it. For reference, a 70,000 message file we trained pork chop with took around 10 minutes on a AWS EC2 t3.micro VM. See [example_training.csv](./example_training.csv) for reference.
* Train with english corpus - Train with the small english corpus provided by ChatterBot
* Train with Ubuntu corpus - This is a huge data set which will take a long time to download and train

## Command Modules

Pork chop will respond to the following command modules:
* !example - Template module
* !usage - Display modules and their use
* !kanye - Display a random Kanye West quote.
* !stonks \<symbol\> - Get stock price information
* !turn \<user\> [list] - Turn a user or list number of turns for all users
* !helpmecook \<food\> - Get recipe help for cooking a tasty vegan meal with spoonacular api (try cooking manwich)
* !yt \<query\> - Get the best-match YouTube video url for your query
* !reddit \<query\> - Get the best-match subreddit for your query

## Deployment

Pork Chop can be deployed on any server with python3.

### Bot Registration

* Navigate to [dev.groupme.com/bots](https://dev.groupme.com/bots)
* Click the orange button labeled "create bot"
* Choose the groupchat you would like pork chop to live in
* For the callback URL, enter the ip or domain of the server Pork Chop will be run on with the extension /bot as this is where the flask handler is set to.
* If you are running pork chop on serverless mode set up the callback URL appropriate to you AWS Lambda function
* You can leave Avatar URL blank or set it to your desired image

### Server

* `git clone https://github.com/danerwilliams/pork-chop.git` Clone pork-chop
* `cd pork-chop` enter pork-chop directory
* `pip3 install -r requirements.txt` install pork-chop's python3 dependencies
* Set environment variables for secrets:
	- `$EDITOR .env` record environment variables to a file with text editor of choice, minimum need to set BOT_ID (use .env.example for reference)
	- `export $(grep -v '^#' .env)` set environment variables from .env file
* OR use .secrets json formatted file for secrets:
	- `$EDITOR .secrets` record secrets to file with text editor of choice, minimum need to set BOT_ID (use .secrets.example for reference)
* `sudo ./pork-chop.py -d` deploy pork chop on port 80 (you can add `&> /dev/null &` to ignore output and run in background)

## Flags

`./pork-chop.py -h`

```
usage: pork-chop [-h] [-c CORES] [-t TRAIN [TRAIN ...]] [-d] [-u] [-e]
                 [-n NAME]

optional arguments:
  -h, --help            show this help message and exit
  -c CORES, --cores CORES
                        Number of CPU cores to use
  -t TRAIN [TRAIN ...], --train TRAIN [TRAIN ...]
                        Train bot from csv data files
  -d, --deploy          Deploy bot with flask on port 80 (requires sudo)
  -u, --ubuntu          Train bot from ubuntu corpus
  -e, --english         Train bot from english corpus
  -n NAME, --name NAME  Change Pork Chop's name from default
```

## References

Inspired by [ginglis13/shortstop](https://github.com/ginglis13/shortstop) and [pbui/bobbit](https://github.com/pbui/bobbit)

Useful Documentation:
* [ChatterBot](https://chatterbot.readthedocs.io/en/stable/)
* [Flask](https://flask.palletsprojects.com/en/1.1.x/quickstart/)
* [GroupMe](https://dev.groupme.com/tutorials/bots)

## Team

This project is maintained by the following person(s) and a bunch of [awesome contributors](https://github.com/danerwilliams/pork-chop/graphs/contributors).

[<img width="80" height="80" src="https://avatars3.githubusercontent.com/u/22798229?v=4&s=70">](https://github.com/danerwilliams) | [<img width="80" height="80" src="https://avatars3.githubusercontent.com/u/49375988?s=400&v=4">](https://github.com/cnrmrphy) | [<img width="80" height="80" src="https://avatars2.githubusercontent.com/u/8454416?s=400&v=4">](https://github.com/jheneghan16) | [<img width="80" height="80" src="https://avatars3.githubusercontent.com/u/50080644?s=400&u=45b2e63a2d05e4ce0887c3d82e26ab08d6e13dbe&v=4">](https://github.com/beniaminogreen) |
--- | --- | --- | --- |
[Dane Williams](https://github.com/danerwilliams) | [Conor Murphy](https://github.com/cnrmrphy) | [James Heneghan](https://github.com/jheneghan16) | [Ben Green](https://github.com/beniaminogreen) |

## License

[MIT License](https://github.com/danerwilliams/pork-chop/blob/master/LICENSE)
