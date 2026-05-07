from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = "nvidia-kms-secret-key"

@app.route("/")
def index():
    conn = sqlite3.connect("kms.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, content, date_submitted FROM knowledge_entries")
    entries = cursor.fetchall()
    conn.close()
    return render_template("index.html", entries=entries)

@app.route("/submit", methods=["POST"])
def submit():
    title = request.form.get("title", "").strip()
    content = request.form.get("content", "").strip()

    if not title or not content:
        flash("Please fill in all fields.", "error")
        return redirect(url_for("index"))

    conn = sqlite3.connect("kms.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO knowledge_entries (title, content) VALUES (?, ?)", (title, content))
    conn.commit()
    conn.close()

    flash("Submission was successful", "success")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
