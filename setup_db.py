import sqlite3

conn = sqlite3.connect("kms.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS knowledge_entries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        content TEXT NOT NULL,
        date_submitted TEXT DEFAULT (date('now'))
    )
""")

cursor.executemany("INSERT INTO knowledge_entries (title, content) VALUES (?, ?)", [
    ("Example 1", "Example 1"),
    ("Example 2", "Example 2"),
    ("Example 3", "Example 3"),
])

conn.commit()
conn.close()

print("File has been created.")
