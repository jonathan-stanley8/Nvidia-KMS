# NVIDIA Knowledge Management System (KMS)

A full-stack web application built as a capstone project that allows NVIDIA employees to store, organize, and retrieve internal knowledge articles. Designed to mirror the kind of knowledge base functionality found in enterprise help desk platforms like ServiceNow.

---

## Features

- View a list of internal knowledge articles in a clean, organized interface
- Each entry displays a title, content, and submission date
- Submit new knowledge entries directly from the web interface
- Backend database for persistent storage and easy management
- Lightweight and fast — runs locally with minimal setup

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python |
| Web Framework | Flask |
| Database | SQLite |
| DB Management | DB Browser for SQLite |
| Frontend | HTML, CSS |

---

## Project Structure

```
Nvidia KMS/
├── app.py            # Flask application — routes and DB queries
├── setup_db.py       # Database initialization and seed data
├── database.py       # Database module
├── kms.db            # SQLite database file
├── requirements.txt  # Python dependencies
└── templates/
    └── index.html    # Frontend UI
```

---

## Getting Started

### Step 1 — Install Required Software

Before running the app, make sure the following are installed on your machine:

#### Python
Python is the programming language the app runs on.

1. Go to https://www.python.org/downloads/
2. Download and run the installer for your operating system
3. **Important:** During installation, check the box that says **"Add Python to PATH"**
4. Verify the installation by opening a terminal and running:
   ```bash
   python --version
   ```

#### Git
Git is used to download the project from GitHub.

1. Go to https://git-scm.com/downloads
2. Download and run the installer for your operating system
3. During installation, make sure **"Add Git to PATH"** is selected (this is the default)
4. Verify the installation by opening a terminal and running:
   ```bash
   git --version
   ```

> **Don't want to install Git?** You can skip it entirely by downloading the project directly from GitHub instead — click the green **Code** button on the repository page and select **Download ZIP**. Extract the ZIP and skip to Step 3.

---

### Step 2 — Download the Project

Open a terminal and run:

```bash
git clone https://github.com/jonathan-stanley8/Nvidia-KMS.git
cd Nvidia-KMS
```

---

### Step 3 — Install Flask

Flask is the web framework the app is built on. Install it by running:

```bash
pip install flask
```

Or if that doesn't work, try:

```bash
pip3 install flask
```

Verify Flask installed successfully:

```bash
python -m flask --version
```

---

### Step 4 — Install Remaining Dependencies

```bash
pip install -r requirements.txt
```

---

### Step 5 — Initialize the Database
*(First time only)*

```bash
python setup_db.py
```

---

### Step 6 — Run the Application

```bash
python app.py
```

You should see a message like:
```
Running on http://127.0.0.1:5000
```

---

### Step 7 — Open in Your Browser

```
http://127.0.0.1:5000
```
---

## Future Improvements

- Add ability to edit and delete articles directly from the web UI
- Implement user authentication so only authorized employees can submit entries
- Add search and filtering functionality to quickly find articles by keyword
- Deploy to a cloud platform for remote access

---

## Author

**Jonathan Stanley**  
B.S. IT Data Networking & Security — Liberty University  
[LinkedIn](www.linkedin.com/in/jonathan-stanley8) | [GitHub](https://github.com/jonathan-stanley8)
