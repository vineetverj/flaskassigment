import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('database.db')
print("Connected to database successfully")



# Execute SQL queries
conn.execute('CREATE TABLE students(name TEXT,addr TEXT,city TEXT)')
print("Table 'students' created successfully")

# Commit changes and close the connection

conn.close()
