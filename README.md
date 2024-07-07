
# Event Management System

This is a REST API for a event management system built using Django REST Framework.


## Features

- Token Based and Access Control authentication system
- CRUD APIs for events
- Search Events by names
- Filter Events by Event Categories
- Different permission levels for Event Organizers, Event Clients, Vendors and Attendees
- Reviews / Feedback for events by Attendees
- STRIPE Payment Integration

## Color Reference

| EndPoints             | Descriptions                                                               |
| ----------------- | ------------------------------------------------------------------ |
| roles/    |   Views Roles that are used for access control    |
| register/   |  Sign up new user |
| login/ | Login user and retrieve Django Auth token|
| logout/ | Logout user |
| events/ | Retrieve list of events, search using ?search=, filter using ?category= |
| events/<id>| Retrieve, update or delete a book|
| venue| Retrievelist if venue|
| venue/<id>| Retrieve, update or delete a venue|
| attendees| Retrieve list of attendees|
| attendees/<id>| Retrieve, update or delete a attendees|
| feedback| Retrieve list of reviews done by attendees|
| feedback/<id>| Retrieve, update or delete a reviews|
| process_payment| Process Payment via Stripe Payment and details are stored in Ticket model|
| revenuereport/<id>| Total reports according to events that shows no of attendees, total logistic charges, Ticket sales, etc|


## Deployment

__Installation__
- Clone the repository
- Create and activate a virtual environment
- Install dependencies
```bash
  virtualenv env
  pip install -r requirements.txt
```

__Setup__
- Run migrations
- Create superuser
```bash
  python manage.py migrate
  python manage.py createsuperuser
```
__Run Server__
- Start development server
```bash
  python manage.py runserver
```
The API will be available at `http://127.0.0.1:8000/`
