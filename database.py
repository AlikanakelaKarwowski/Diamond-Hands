import sqlite3 as sql

conn = sql.connect('database.db')
print("Opened database successfully")

cursor = conn.cursor()

sqlQuery1 = """ CREATE TABLE IF NOT EXISTS users (
    userID INTEGER PRIMARY KEY AUTOINCREMENT,
    createdID TEXT NOT NULL UNIQUE,
    firstName TEXT NOT NULL,
    lastName TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
)"""
cursor.execute(sqlQuery1)

print("Table created successfully")
conn.close()