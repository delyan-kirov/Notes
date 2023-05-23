import os
import sqlite3
import time

def add_files_to_db():
    conn = sqlite3.connect('userFiles.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS files (filename text)''')
    data_files = []
    # Adjust the path to the Data folder as needed
    for root, dirs, files in os.walk('./data'):
        for file in files:
            data_files.append(file)
            c.execute("SELECT COUNT(*) FROM files WHERE filename=?", (file,))
            if c.fetchone()[0] == 0:
                c.execute("INSERT INTO files VALUES (?)", (file,))
                print(f"Added file {file} to the database")
    c.execute("SELECT filename FROM files WHERE filename NOT IN ({})".format(','.join(['?']*len(data_files))), data_files)
    for row in c.fetchall():
        print(f"File {row[0]} is no longer present in the Data folder")
    c.execute("DELETE FROM files WHERE filename NOT IN ({})".format(','.join(['?']*len(data_files))), data_files)
    conn.commit()
    conn.close()

def delete_files():
    conn = sqlite3.connect('userFiles.db')
    c = conn.cursor()
    c.execute("SELECT filename FROM files")
    data_files = [row[0] for row in c.fetchall()]
    conn.close()
    # Adjust the path to the templates folder as needed
    for root, dirs, files in os.walk('./templates'):
        for file in files:
            if file.endswith('.html') and file[:-5] not in data_files:
                os.remove(os.path.join(root, file))
                print(f"Deleted file {file}")

while True:
    add_files_to_db()
    time.sleep(10) # wait 10 secs
    delete_files()
    time.sleep(10) # wait 10 secs