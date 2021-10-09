import sqlite3

# Create a connection to the database
con = sqlite3.connect('Twitter_Version/logs.db')
curs = con.cursor()

for row in curs.execute('SELECT * FROM exceptions'):
    print(row)
