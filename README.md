# promise-tracker
A political promise tracker for monitoring Government parties and their policies/manifestos.

## Getting Started
Clone this git repository down to your system.
Navigate to `policy-tracker` folder; which contains the `manage.py` file.

Run the following command to install `social-auth-app-django`:

```bash
pip install social-auth-app-django
```

After the module has been installed you can safely run the application with:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Then just navigate to <http://localhost:8000> or <http://127.0.0.1:8000>.

## GoogleOAuth2 API
Login via GoogleOAuth2 API is implemented through the social-auth-app-django module for Django that you have just installed with Pip.

Currently, a basic template Home HTML file is used with no functionality. As such, for now, logging in with GoogleOAuth2 has to be done by directly navigating to:

<http://localhost:8000/soc/login/google-oauth2/?next=/>

There you will be asked to login and/or pick which Google account you want to use to grant permissions to Policy Tracker.
Policy Tracker will then receive details such as Firstname, Surname and email address to create a User object in the DB with.
You will then be redirected to the Home page with a logged in status.
