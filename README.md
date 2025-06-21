Patient Information System

A simple Flask application with SQLite backend to manage patient records, featuring user authentication and CRUD operations through both web pages and REST APIs.

Getting Started

1. Install dependencies
python3 -m venv venv
source venv/bin/activate       # Windows: venv\Scripts\activate
pip install -r requirements.txt

2. Initialize the database
python init_db.py

3. Run
export FLASK_APP=app.py         # Windows: set FLASK_APP=app.py
flask run
