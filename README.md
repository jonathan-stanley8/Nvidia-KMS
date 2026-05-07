# NVIDIA Knowledge Management System (KMS)

A full-stack web application built as a capstone project that allows NVIDIA employees to store, organize, and retrieve internal knowledge articles. Designed to mirror the kind of knowledge base functionality found in enterprise help desk platforms like ServiceNow.

---

## Features

- View a list of internal knowledge articles in a clean, organized interface
- Each entry displays a title, content, and submission date
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

### Prerequisites
- Python 3.x installed
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/Nvidia-KMS.git
   cd Nvidia-KMS
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Initialize the database** (first time only)
   ```bash
   python setup_db.py
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open in your browser**
   ```
   http://127.0.0.1:5000
   ```

---

## Future Improvements

- Add ability to create, edit, and delete articles directly from the web UI
- Implement user authentication so only authorized employees can submit entries
- Add search and filtering functionality to quickly find articles by keyword
- Deploy to a cloud platform for remote access

---

## Author

**Jonathan Stanley**  
B.S. IT Data Networking & Security — Liberty University  
[LinkedIn](www.linkedin.com/in/jonathan-stanley8) | [GitHub](https://github.com/jonathan-stanley8)
