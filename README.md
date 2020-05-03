[![CI Status](https://github.com/jugmac00/workout-bot/workflows/CI/badge.svg?branch=master)](https://github.com/jugmac00/workout-bot/actions?workflow=CI)

# workout bot

Once set up properly, this bot will send you a daily workout.

## a word of caution

This project is very alpha, and will change very much in near future.

## setup

```
# git clone this repository
$ git clone git@github.com:jugmac00/workout-bot.git

# create and activate a virtual environment
$ python3.8 -m venv venv
$ . venv/bin/activate

# install requirements
pip install -r requirements.txt

# create a `.env` file with the following content
echo "exporting API_KEY..."
export API_KEY="XXXX" # replace with your bot API_KEY
export TELEGRAM_ID="XXXX" # replace with your Telegram ID

# set up environment
$ source .env

# manually run...
$ cd workout_bot
$ python main.py

# or set up a cron job to run daily
```

## thank you

Currently, all thanks goes to my colleague Chris.

He asked me to help him finding a bug in his bot.

Without him, I would have never came up with the idea to play with the Telegram bot API.
