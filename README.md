# biblioteca 

# Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone git@github.com/diegoreiss/biblioteca.git
    $ cd biblioteca
    
Activate the virtualenv for your project.
    
Install project dependencies:

    $ pip install -r requirements.txt
    
    $ cd biblioteca
    
Then simply apply the migrations:

    $ python manage.py migrate

You can now run the development server:

    $ python manage.py runserver

.env params:
    
    EMAIL_SENDER_SMTP_SSL=
    EMAIL_SENDER_NAME=
    EMAIL_SENDER_PASSWORD=
    EMAIL_SENDER_PORT=
    EMAIL_SENDER_SMTP_SSL=

