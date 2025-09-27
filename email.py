import re

with open ('mbox.txt') as handler:
    message = handler.read()
    email=re.findall('\s+@\s+',message)


with open('email.txtt')


import sqlite3

#creation of database
conn = sqlite3.connect('mall.db)

a=conn.cursor()