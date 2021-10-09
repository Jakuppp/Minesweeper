# Minesweeper/Twitter Minesweeper bot

![GitHub commit activity](https://img.shields.io/github/commit-activity/m/Jakoobb/Minesweeper?logo=github%20actions&style=for-the-badge)
![GitHub last commit](https://img.shields.io/github/last-commit/Jakoobb/Minesweeper?logo=github%20actions&style=for-the-badge)
![GitHub repo size](https://img.shields.io/github/repo-size/Jakoobb/Minesweeper?logo=github&style=for-the-badge)
![GitHub top language](https://img.shields.io/github/languages/top/Jakoobb/Minesweeper?logo=python&style=for-the-badge)
![GitHub followers](https://img.shields.io/github/followers/Jakoobb?logo=github%20sponsors&style=for-the-badge)

# Table of contents

* **[Playing the terminal version](#Minesweeper)**
* **[Twitter bot](#Twitter-bot)**
    * *[Installing the bot](#Installing-the-bot)*
    * *[Setting up the bot](#Setting-up-the-bot)*
    * *[Launching the bot](#Launching-the-bot)*
    * *[Checking error logs](#Checking-error-logs)*

# Minesweeper

> To play the game:<br/>
> Make sure, that you have Python v.3.9+ and Git installed<br/>
> Next, type the following in your terminal:

```python
>>> git clone https://github.com/Jakoobb/Minesweeper.git
>>> cd Minesweeper/Scripts
Minesweeper/Scripts>>> python game_manager.py
```

> Enjoy!

# Twitter bot

### Installing the bot

> To install the bot:<br/>
> Make sure that you have Python v.3.9+ and Git installed<br/>
> Next, type the following in your terminal:

```python
>>> git clone https://github.com/Jakoobb/Minesweeper.git
>>> pip install Minesweeper/Twitter_Version/requirements.txt
```

### Setting up the bot

> To set up the bot make a Twitter developer account and a "Search Tweets: 30-Days/Sandbox" dev environment.<br/>
> Next, input all of the neccesary credentials into the [.env file](Twitter_Version/.env)

*.env file*
```md
# .env
API_KEY=
API_KEY_SECRET=
ACCESS_TOKEN=
ACCESS_TOKEN_SECRET=
NAME=
ENVIRONMENT_NAME=
```

### Launching the bot

> To launch the bot, type the following in your terminal:
```python
>>> cd Minesweeper/Twitter_Version/Scripts
Minesweeper/Twitter_Version/Scripts>>> python main.py
```

### Checking error logs

> To view errors, execute the [view_exception_logs.py file](Twitter_Version/Scripts/view_exception_logs.py)
