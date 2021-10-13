import sqlite3

# Create a connection to the database
con = sqlite3.connect('logs.db')
curs = con.cursor()

for row in curs.execute('SELECT * FROM exceptions'):
    print(row)
