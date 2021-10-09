import sqlite3
import sys
import datetime

# Create a connection to the database
con = sqlite3.connect('Twitter_Version\logs.db')
cur = con.cursor()

def transform_input(input: str) -> tuple:
    try:
        x, dot, y = input.partition('.')
        out = (int(x), int(y))
        return out
    except Exception as err:
        return
        print(err)

def get_most_votes(input: list) -> tuple:

    transformed_list = []
    for untransformed_vote in input:
        if transform_input(untransformed_vote) is not None:
            transformed_list.append(transform_input(untransformed_vote))

    votes = {vote: 0 for vote in transformed_list}
    for vote in transformed_list:
        votes[vote] += 1
    try:
        most_votes = max(votes, key=votes.get)
        return most_votes
    except Exception as exc:
        exception_info = sys.exc_info()
        cur.execute("INSERT INTO exceptions (exception_time, exception_type, exception_value, traceback) VALUES (?, ?, ?, ?)", (datetime.datetime.now().strftime('%m/%d/%Y, %H:%M:%S'), exception_info[0].__name__, f'{exception_info[1]}', f'{exception_info[2].tb_frame}'))
        con.commit()
        return 'error'

def create_random_id(length):
    import random
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789!-_=+$%^&*()<>?,./:;"[]{}|' 
    ID = ''
    for _ in range(length):
        ID = ID + chars[random.randint(0, len(chars)-1)]
    return ID
