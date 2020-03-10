##### A Software Engineering 2 project:
## Maryknoll Academy of Cateel Enrollment System

A software engineering 2 project: Enrollment System for Maryknoll Academy of Cateel

## Getting Started

To get yourself a copy of the project up and running on your local machine for development and testing purposes:

1.) Create your workspace folder and open your command line to your workspace folder

2.) Register the repository link (https://github.com/aaajii/maryknoll-system.git) to a remote 

``` git remote add origin https://github.com/aaajii/maryknoll-system.git ```

3.) Clone the repository to your folder to make yourself have your own local copy of it

``` git clone origin ```

### Prerequisites

The project requires the latest version of python 3 and Django3.0.3


Install all the requirements provided in the requirements.txt and then you are good to go.

Assuming you are using any linux OS (or git bash on windows), you can run this in your command line:
```
pip install -r requirements.txt
```

## Running the tests

In case you want to run your Django application from the terminal just run:

1) Run syncdb command to sync models to database and create Django's default superuser and auth system

    $ python manage.py migrate

2) Run Django

    $ python manage.py runserver

## Built With

* [Django 3](https://docs.djangoproject.com/en/3.0/) - The web framework used

## Deployment

Configure the web host's WSGI with:

```
import os
import sys

#assuming your manage.py is located at /home/maryknoll/project/maryknoll-system then
path = '/home/maryknoll/project/maryknoll-system'
if path not in sys.path:
    sys.path.append(path)

#assuming your settings.py is located at /home/maryknoll/project/maryknoll-system/main then
os.environ['DJANGO_SETTINGS_MODULE'] = 'main.settings'


from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

```

import necessary virtual environments first if needed!

## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration

