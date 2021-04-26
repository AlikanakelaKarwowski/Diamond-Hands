import sqlite3 as sql

conn = sql.connect('database.db')
print("Opened database successfully")

cursor = conn.cursor()

sqlQuery1 = """ CREATE TABLE IF NOT EXISTS users (
    userID INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
)"""
cursor.execute(sqlQuery1)

print("Table created successfully")
conn.close()