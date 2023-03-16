import sqlite3

conn = sqlite3.connect("myquotes.db")
curr = conn.cursor()

curr.execute("""CREATE TABLE quotes_tb(
 title TEXT,
 author TEXT,
 tag TEXT
 )""")


curr.execute("""INSERT INTO quotes_tb VALUES ('pyhton is awsome','ccodewith','python')""")

conn.commit()
conn.close()