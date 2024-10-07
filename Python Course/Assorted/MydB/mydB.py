import sqlite3

conn = sqlite3.connect('newdB.db')

#Creates the table 'tbl_newdb' with an incrementing ID, and 'db_type' columns.
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_newdb( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        db_type TEXT)")
    conn.commit()


# Variable with a tuple list of parameters or pass through.
fileList = ["information.docx","Hello.txt","myImage.png", \
            "myMovie.mpg","World.txt","data.pdf","myPhoto.jpg"]

# A new list for our '.txt' files to reside.
newlist = []

# Loop to find the strings that contain '.txt' and append them into a new list.
for x in fileList:
    if x.endswith('.txt'):
        newlist.append(x)
print(newlist)        

# A for loop that iterates through the list and inserts the items into the table.
with conn:
    for x in newlist:
        cur.execute("insert into tbl_newdb(db_type) VALUES (?)",(x,))
    conn.commit()

    # Print debugging information to prove we inserted things correctly
    cur.execute("SELECT db_type FROM tbl_newdb")
    print(cur.fetchall())

# Close the connection after creating the table
conn.close()




