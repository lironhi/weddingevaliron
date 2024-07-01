Wedding Website

Welcome to our wedding website built using Django!

Features
RSVP System: Guests can RSVP directly through the website.
Event Details: Information about the wedding events, venue, and timings.
Photo Gallery: A collection of photos from our journey together.
Contact Us: A form for guests to contact us with any questions.
Reservations: Database to save some informations.

Installation

Clone the repository:
git clone <repository-url>

Create a virtual environment:
python -m venv env

Activate the virtual environment:
pip install -r requirements.txt

Apply migrations:
python manage.py migrate

Start the development server:
python manage.py runserver

Open your web browser and go to http://localhost:8000 to view the website.

Configuration
Database: By default, the project uses SQLite for ease of setup. For production, consider using PostgreSQL or MySQL. (worked on sqlite using heroku)

Deployment: Refer to Django's documentation for deploying the project in production.

Contributing
Feel free to fork the repository and submit pull requests or issues.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Authors
LironHi
