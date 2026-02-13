# Flaskr - A Full-Featured Flask Blog

[![Python](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/flask-3.2-green)](https://flask.palletsprojects.com/)

**Flaskr** is a full-featured, installable blog application built with **Flask**.  
It demonstrates user authentication, database integration, and CRUD operations, making it a great learning project or starting point for real-world web apps.

---

## Features

- **User Authentication:**  
  - Register, login, logout  
  - Secure password storage
- **Blog Management:**  
  - Create, read, update, delete posts (CRUD)  
  - View all posts on the home page
- **Database Integration:**  
  - SQLite (lightweight, file-based, no separate server required)  
  - Easily replaceable with PostgreSQL or MySQL
- **Templates & UI:**  
  - Jinja2 templates with base layout  
  - Flash messages for success/error feedback
- **Installable Project:**  
  - Can be installed with `pip` from `pyproject.toml`  
  - Editable mode for development  

---

---

## Installation

1. Clone the repository:
git clone https://github.com/yourusername/flaskr.git
cd flaskr

2. Create a virtual environment:
(write in terminal)
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser  #Windows
.venv\Scripts\Activate.ps1      # Windows
pip install -r requirements.txt

3. Install the project in editable mode:
pip install -e .

4. pip install -e .
flask --app flaskr init-db

5. Run the development server:
flask --app flaskr --debug run
Visit http://127.0.0.1:5000 to see your app in action.

---

---

## Usage

Navigate to /auth/register to create a new user.
Login at /auth/login to access the blog features.
Create, edit, and delete posts after logging in.
View posts on the home page (/).

---

---

## Database
Type: SQLite
File: flaskr.sqlite (located in the instance folder)
Contains two tables:
user → stores user accounts
post → stores blog posts with author_id as foreign key

---

---

## Project Metadata (pyproject.toml)
[project]
name = "flaskr"
version = "1.0.0"
description = "The basic blog app built in the Flask tutorial."
dependencies = [
    "flask",
]

[build-system]
requires = ["flit_core<4"]
build-backend = "flit_core.buildapi"

---

Flaskr is perfect for learning Flask, understanding project structure, authentication, database handling, and building real-world web applications quickly.
