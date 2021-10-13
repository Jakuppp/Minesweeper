# Python built-in modules
import os
import datetime
import sqlite3
import sys

# Modules requiring pip
import dotenv
import tweepy

from minesweeper import Minesweeper
from other import *

if __name__ == '__main__':

    # Create a connection to the database
    con = sqlite3.connect('logs.db')
    cur = con.cursor()
  
    # Create the table with the exception logs
    try:
        cur.execute('''CREATE TABLE exceptions (exception_time, exception_type, exception_value, traceback)''')
        con.commit()
    except Exception as exception:
        exception_info = sys.exc_info()
        cur.execute("INSERT INTO exceptions (exception_time, exception_type, exception_value, traceback) VALUES (?, ?, ?, ?)", (datetime.datetime.now().strftime('%m/%d/%Y, %H:%M:%S'), exception_info[0].__name__, f'{exception_info[1]}', f'{exception_info[2].tb_frame}'))
        con.commit()

    # Store all of the necessary credentials
    dotenv.load_dotenv()
    API_KEY=os.getenv('API_KEY')
    API_KEY_SECRET=os.getenv('API_KEY_SECRET')
    ACCESS_TOKEN=os.getenv('ACCESS_TOKEN')
    ACCESS_TOKEN_SECRET=os.getenv('ACCESS_TOKEN_SECRET')
    NAME=os.getenv('NAME')
    ENVIRONMENT_NAME=os.getenv('ENVIRONMENT_NAME')

    auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)

    while True:
        # Create a new game
        game = Minesweeper(5,8)
        game_on = True
        won = True
        api.update_status(game.render(create_random_id(80)))
        while game_on:

            # Update the status every 5 minutes
            minutes = datetime.datetime.now().minute
            seconds = datetime.datetime.now().second
            if minutes%5 == 0 and seconds == 0:

                try:

                    # Get all of the replies from the latest tweet
                    replies=[]
                    for tweet in tweepy.Cursor(api.search_30_day, ENVIRONMENT_NAME, 'to:'+NAME).items(1000):
                        if hasattr(tweet, 'in_reply_to_status_id_str') and tweet.in_reply_to_status_id_str==api.user_timeline(screen_name=NAME, count=1)[0].id_str:
                            replies.append(tweet.text)

                    # Get the cell that had the most replies and reveal it   
                    for reply in replies:

                            mention, space, body = reply.partition(' ')
                            replies[replies.index(reply)] = body
                
                    choice = game.reveal_cell(get_most_votes(replies))

                    # If any cell was revealed update the status and the game
                    if get_most_votes(replies) != 'error':
                        game_on = choice
                        if game_on:
                            won = game.check_if_won()
                            if not won:
                                game_on=won
                            else:
                                pass
                        
                        api.update_status(game.render(create_random_id(80)))
            
                except Exception as exception:
                    exception_info = sys.exc_info()
                    cur.execute("INSERT INTO exceptions (exception_time, exception_type, exception_value, traceback) VALUES (?, ?, ?, ?)", (datetime.datetime.now().strftime('%m/%d/%Y, %H:%M:%S'), exception_info[0].__name__, f'{exception_info[1]}', f'{exception_info[2].tb_frame}'))
                    con.commit()

        if not won:
            api.update_status(game.win(create_random_id(80)))
        else:
            api.update_status(game.lose(create_random_id(80)))
        api.update_status(game.render(create_random_id(80)))
