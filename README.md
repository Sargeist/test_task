News Digest Django App


Features

- Admin interface to manage news sources (Source).
- Fetch articles from RSS feeds using a periodic Celery task.
- Create digests (Digest) with selected articles.
- Supports SQLite and PostgreSQL.
- Can be run locally or with Docker Compose.


Local Installation and Run

1. Clone the project and navigate to the folder:

   git clone <repo-url>
   cd <project-folder>

2. Create and activate a virtual environment:

   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows

3. Install dependencies:

   pip install -r requirements.txt

4. Configure environment variables by creating a .env file based on .env.example.

5. Apply migrations:

   python manage.py migrate

6. Create a superuser for the admin interface:

   python manage.py createsuperuser

7. Run the development server:

   python manage.py runserver

8. (Optional) Run Celery worker:

   celery -A project worker -l info

9. (Optional) Run Celery beat for periodic tasks:

   celery -A project beat -l info

Docker Compose Installation and Run

1. Ensure Docker and docker-compose are installed.
2. In the project root, run:

   docker-compose up --build

   This will start:
   - Django web application
   - SQLite database
   - Redis
   - Celery worker
   - Celery beat

3. Access the admin site: http://localhost:8000/admin