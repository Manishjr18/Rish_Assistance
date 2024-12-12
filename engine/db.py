import csv
import sqlite3

con = sqlite3.connect("rish.db")
cursor = con.cursor()

# Command to drop the table if needed
# que = "DROP TABLE IF EXISTS sys_command"
# cursor.execute(que)

# Run this once to insert into table else duplicate items will be inserted
# query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
# cursor.execute(query)

# query = "INSERT INTO sys_command VALUES (null,'Android studio', 'C:\\Program Files\\Android\\Android Studio\\bin\\studio64.exe')"
# cursor.execute(query)
# con.commit()

# query = "INSERT INTO sys_command VALUES (null,'one note', 'C:\\Program Files\\Microsoft Office\\root\\Office16\\ONENOTE.EXE')"
# cursor.execute(query)
# con.commit()




# Table for links
# query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'youtube', 'https://www.youtube.com/')"
# cursor.execute(query)
# con.commit()
# query = "INSERT INTO web_command VALUES (null,'canva', 'https://www.canva.com/en_in/')"
# cursor.execute(query)
# con.commit()




# testing module
# app_name = "android studio"
# cursor.execute('SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
# results = cursor.fetchall()
# print(results[0][0])

# Create a table with the desired columns
cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (id integer primary key, name VARCHAR(200), mobile_no VARCHAR(255), email VARCHAR(255) NULL)''')


# Specify the column indices you want to import (0-based index)
# Example: Importing the 1st and 3rd columns
desired_columns_indices = [0, 18]

# # Read data from CSV and insert into SQLite table for the desired columns
# with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
#     csvreader = csv.reader(csvfile)
#     for row in csvreader:
#         selected_data = [row[i] for i in desired_columns_indices]
#         cursor.execute(''' INSERT INTO contacts (id, 'name', 'mobile_no') VALUES (null, ?, ?);''', tuple(selected_data))

# # Commit changes and close connection
# con.commit()
# con.close()

# query = "INSERT INTO contacts VALUES (null,'tejas', '7202014682', 'null')"
# cursor.execute(query)
# con.commit()


# Search from db
query = 'Manish'
query = query.strip().lower()

cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
results = cursor.fetchall()
print(results[0][0])