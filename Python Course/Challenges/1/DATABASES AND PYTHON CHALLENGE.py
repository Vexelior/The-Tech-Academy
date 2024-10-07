import sqlite3

conn = sqlite3.connect('db_challenge.db')

#Creates the table 'tbl_challenge' with an incrementing ID, and 'db_type' columns.
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_challenge( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        Name TEXT, \
        Species TEXT, \
        IQ INT)")
    conn.commit()

#Inserts the data into the new table.
with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_challenge(Name, Species, IQ) VALUES (?,?,?)", \
                ('Jean-Baptiste Zorg', 'Human', '122'))
    cur.execute("INSERT INTO tbl_challenge(Name, Species, IQ) VALUES (?,?,?)", \
                ('Korben Dallas', 'Meat Popsicle', '100'))
    cur.execute("INSERT INTO tbl_challenge(Name, Species, IQ) VALUES (?,?,?)", \
                ('Aknot', 'Mangalore', '-5'))
    conn.commit()

with conn:
    cur = conn.cursor()
    cur.execute("UPDATE tbl_challenge SET Species = 'Human' WHERE Name = 'Korben Dallas'")
    conn.commit()

with conn:
    cur = conn.cursor()
    cur.execute("SELECT * FROM tbl_challenge WHERE Species = 'Human'")
    conn.commit()

conn.close()


