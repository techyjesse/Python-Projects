import sqlite3

conn = sqlite3.connect('files.db')

# while connected, creates a cursor to operate db/execute staement ass table to db
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fileName TEXT \
        )")
    # commits tbl to database
    conn.commit()
conn.close()

fileList = ('information.docx','Hello.txt','myImage.png','myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

conn = sqlite3.connect('files.db')



with conn:
    cur = conn.cursor()
    for item in fileList:
        if item.endswith(".txt"):
            cur.execute("INSERT INTO tbl_files (col_fileName) VALUES (?)", (item,))
            print(item)
    conn.commit()
conn.close()
    
