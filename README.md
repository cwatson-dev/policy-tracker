# promise-tracker
A political promise tracker for monitoring Government parties and their policies/manifestos.

## Getting Started
Clone this git repository down to your system.

`git clone https://github.com/2190594W/policy-tracker`

then

`git pull`

Navigate to `policy-tracker` folder; which contains the `manage.py` file.

Run the following command to install the correct dependencies:

```bash
pip install -r requirements.txt
```

Next, you can safely run the application with:

```bash
python manage.py makemigrations
python manage.py migrate
python populate_policy_tracker.py
python manage.py runserver
```

Then just navigate to <http://localhost:8000> or <http://127.0.0.1:8000>.

## OAuth2 APIs
Login via OAuth2 APIs is implemented through the social-auth-app-django module for Django that you have manually installed with Pip.

Currently, a basic template Home HTML file is used with little functionality. However, on the Home Page there are four links to allow a User to login with Google, Facebook, Twitter or GitHub. Standard Django login/registration is not yet implemented.

There you will be asked to login and/or pick which Google/Facebook/Twitter/GitHub account you want to use to grant permissions to Policy Tracker. And a brief description of the permissions will show next to the Policy Tracker logo.
Policy Tracker will then receive details such as Firstname, Surname and email address to create a User object in the DB with.

You will then be redirected to the Home page with a logged in status.

Once logged in with one of the services, the user can then access the below link to view their current connected services, and choose to disconnect any that they may wish to:

<http://localhost:8000/profile/settings/>

### When developing the application, always commit to a new branch that is based off of the 'Development' branch. That way any commits can be reviewed for errors/clashes before being pulled into the main 'Development' branch. Periodically, we will update the 'Master' branch to reflect the changes of the 'Development' branch.

### When developing, it useful to be able to easily see the contents of the database (db.sqlite3 file). As such you should download the "DB Browser for SQLite" application <http://sqlitebrowser.org/>. It is an exceptionally lightweight and easy-to-use DB Browser and only requires launching the application and selecting "Open Database" in the top righthand corner. Then just browse to the application's `db.sqlite3` file.
