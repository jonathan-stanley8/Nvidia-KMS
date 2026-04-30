from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    conn = sqlite3.connect("kms.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, content, date_submitted FROM knowledge_entries")
    entries = cursor.fetchall()
    conn.close()
    return render_template("index.html", entries=entries)

if __name__ == "__main__":
    app.run(debug=True)
