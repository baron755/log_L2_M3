import sqlite3

conn = sqlite3.connect("university")
cursor = conn.cursor()

ct_query = " "

cursor.execute('''CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEST,
    age INTEGER
    major TEXT
)
               ''')

cursor.execute('''CREATE TABLE IF NOT EXISTS courses (
    course_id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_name TEXT,
    instructor TEXT
)
               ''')