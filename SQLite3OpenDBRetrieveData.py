

import sqlite3

conn = sqlite3.connect('db_submission1.db')#variable will hold the connection to the dB. 
#setting up table with columns and rows

with conn:
    cur = conn.cursor() #this is a shortcut, so we don't have to keep writing "con.cursor"
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files1(\
    ID INTEGER PRIMARY KEY AUTOINCREMENT,\
    col_docname TEXT\
     )") #in brackets is SQLITE commands
    
fileList = ('information.docx', 'Hello.txt', 'myImage.png',\
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg') #declaring the variable as a tuple


for x in fileList: #"for all items in tuple above"
    if x.endswith(".txt"): #"if the item ends with extension "txt""
        with conn:
            cur =conn.cursor()
            cur.execute("INSERT INTO tbl_files1(col_docname) VALUES (?)",(x,))#insert the items in to
            #the table with column name "docname"
            print(x)
conn.close() #close the connection
