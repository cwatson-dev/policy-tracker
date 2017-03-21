import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE','policy_tracker_project.settings') 
 
import django
django.setup()

from policy_tracker_app.models import Status, Category
from django.contrib.auth.models import User
 
def populate():

	u = User.objects.get_or_create(username="admin")[0]
	u.password = "testPolicies1!"
	u.is_superuser = 1
	u.first_name = "PolicyTracker"
	u.last_name = "Admin"
	u.email = "admin@policy-tracker.co.uk"
	u.is_staff = 1
	u.is_active = 1
	u.save()
 
	statuses = ["No Progress","In Progress", "Acheived", "Broken"]
 
	for status in statuses: 
		s = add_status(status)
		
	categories = ["Culture", "Defense", "Economy", "Education", "Environment", "General", "Immigration", "Justice", "Security", "Welfare"] 
	
	for category in categories:
		c = add_category(category)
 
def add_status(name): 
	s = Status.objects.get_or_create(name=name)[0] 
	s.save() 
	return s 
	
def add_category(name):
	c = Category.objects.get_or_create(name=name)[0]
	c.save()
	return c
	
# Known as the populate function	
if __name__ == '__main__': 
	print("Starting Policy Tracker population script...") 
	populate()
