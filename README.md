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

## Deployment

Pork Chop can be deployed either on a server or with AWS serverless lambda functions (coming soon).

### Server

### Serverless (AWS Lambda)

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
* [AWS Lambda](https://docs.aws.amazon.com/lambda/index.html)
* [Flask](https://flask.palletsprojects.com/en/1.1.x/quickstart/)
* [GroupMe](https://dev.groupme.com/tutorials/bots)

## Team

This project is maintained by the following person(s) and a bunch of [awesome contributors](https://github.com/danerwilliams/pork-chop/graphs/contributors).

[<img width="80" height="80" src="https://avatars3.githubusercontent.com/u/22798229?v=4&s=70">](https://github.com/danerwilliams) | [<img width="80" height="80" src="https://avatars3.githubusercontent.com/u/49375988?s=400&v=4">](https://github.com/cnrmrphy) | [<img width="80" height="80" src="https://avatars2.githubusercontent.com/u/8454416?s=400&v=4">](https://github.com/jheneghan16) | 
--- | --- | --- |
[Dane Williams](https://github.com/danerwilliams) | [Conor Murphy](https://github.com/cnrmrphy) | [James Heneghan](https://github.com/jheneghan16) |

## License

[MIT License](https://github.com/danerwilliams/pork-chop/blob/master/LICENSE)
