Patient Information System
A simple Flask application with SQLite backend to manage patient records, using CRUD operations through both web pages and REST APIs.

Project Structure

patient-info-system-flask/
app.py                  # Flask application factory and configuration
models.py               # SQLAlchemy models
routes.py               # Route definitions, view functions, and authentication decorator
init_db.py              # SQLite database initialization & seeding script
templates/              # Jinja2 HTML templates
    base.html           # Base layout with navigation and flash messages
    login.html          # User login page
    patients.html       # List of patients with link to details
    patient_form.html   # Form for creating a new patient 
    patient_detail.html # View/update/delete a patient
static/
    styles.css          # Global CSS styling
instance/
    patients.db         # SQLite database instance

Running the App

