**Patient Information System**

A simple Flask application with SQLite backend to manage patient records, featuring user authentication and CRUD operations through both web pages and REST APIs.


**Getting Started**

Install dependencies:

  	pip install -r requirements.txt


Initialize the database:

  	python init_db.py


Run app: 

  	flask run

**Project Structure**

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

**Limitations and Trade-offs**

1. App is assumed to be deployed in the same server. The better practice is to deploy front-end and back-end separately.
2. SQLite is a file-based database and may not be suitable for large-scale deployments. PostgreSQL or MySQL would be better choice.
3. User credentials are hardcoded and insecure. User management using an Identity Provider like Entra External ID or Okta is the industry practice.
4. Uses basic HTML/CSS without client-side validation. Using Bootstrap for responsive design and WCAG is the industry practice.
5. Relies on Flask’s default signed cookie sessions and no session expiration policy. Usual practice is to use token-based auth (JWT/OAuth).
6. APIs are not documented. Swagger generated documentation is the industry practice.
7. Database connection string and secret key is in the config file, which is not recommended. Industry practice is to use a secrets manager like Azure Key Vault or AWS Secrets Manager to manage app secrets.
