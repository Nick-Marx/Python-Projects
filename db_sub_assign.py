
'''
Python 3.10.0

Purpose: 
'''

import sqlite3

#creates db file and opens it
conn = sqlite3.connect('text.db')

#within db file, create table if it doesn't exist
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_textfiles \
        (ID INTEGER PRIMARY KEY AUTOINCREMENT, col_filename TEXT, \
        UNIQUE(col_filename))")
    
    conn.commit()

    #list of files stored in a tuple
    fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
        'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

    #finds diles with txt ext and appends them to table
    for i in fileList:
        if i.endswith('.txt'):
            cur.execute("INSERT OR IGNORE INTO tbl_textfiles(col_filename) \
                VALUES (?)", (i,))
            
    conn.commit()

    #create tuple from table contents
    cur.execute("SELECT col_filename FROM tbl_textfiles")
    
    varFiles = cur.fetchall()

    #print items in variable
    print(varFiles) 

#closes connection to db file
conn.close()

