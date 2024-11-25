This is a Django-based task management system that allows administrators to manage tasks and send email invitations to new users. It includes features like task creation, updating, deleting, and user registration via invitation links.

Features User authentication (login/register) Admin can send email invitations Task creation, update, and deletion Separate views for users and admins Prerequisites Before setting up the project, ensure you have the following installed:

Python (version 3.12.6) pip (Python package manager) Django (version 5.1.3) SQLite Git Installation Follow these steps to set up the project:

Clone the repository bash Copy code git clone https://github.com/yourusername/your-repo-name.git cd your-repo-name Set up a virtual environment

bash Copy code python -m venv venv source venv/bin/activate # On Windows: venv\Scripts\activate Install dependencies

bash Copy code pip install -r requirements.txt Apply migrations

bash Copy code python manage.py makemigrations python manage.py migrate Create a superuser (admin)

bash Copy code python manage.py createsuperuser Run the development server

bash Copy code python manage.py runserver Access the application

Open your browser and go to http://127.0.0.1:8000/admin to log in as an admin. Configuration Email Settings: Update the email settings in settings.py for sending invitations. Example:

python Copy code EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' EMAIL_HOST = 'smtp.gmail.com' EMAIL_PORT = 587 EMAIL_USE_TLS = True EMAIL_HOST_USER = 'your-email@gmail.com' EMAIL_HOST_PASSWORD = 'your-email-password' Environment Variables: Use .env files to store sensitive credentials.

Usage Admin can log in to the admin panel and send invitations to new users. Invited users will receive an email with a registration link. Registered users can log in to manage their tasks. Contributing Feel free to fork this repository and submit pull requests. Contributions are welcome!

License This project is licensed under the MIT License - see the LICENSE file for details. Acknowledgments Django Documentation
