# Expense-tracker
This is a Django app for managing transactions between users.
Features

    Create transactions between users
    View transactions list and details
    Update transactions
    Delete transactions

Requirements

    Python 3.6 or higher
    Django 3.0 or higher

Installation

    1.Clone the repository to your local machine:
        $ git clone https://github.com/edzy16/Expense-tracker.git

    2.Change into the app directory:
        $ cd Expense-tracker

    3.Install the required packages:
        $ pip install -r requirements.txt

    4.Run migrations to create the necessary database tables:
        $ python manage.py migrate

    5.Start the development server:
        $ python manage.py runserver

Usage

    6.Create a superuser to access the Django admin panel:

python manage.py createsuperuser

    7.Log into the admin panel at http://localhost:8000/admin/ and add some users.
    8.Create transactions between users by making a POST request to /api/transactions/ with the following payload:

        json

        {
            "from_user": <user_id>,
            "to_user": <user_id>,
            "amount": <amount>,
            "description": <description>
        }

    View the transactions by making a GET request to /api/transactions/.

Documentation

The API documentation can be found at http://localhost:8000/docs/.