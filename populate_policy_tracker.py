# -*- coding: utf-8 -*-
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','policy_tracker_project.settings')

import django
django.setup()

from datetime import datetime
from policy_tracker_app.models import Status, Category, Country
from django.contrib.auth.models import User

def populate():

	u = User.objects.get_or_create(username="admin")[0]
	u.password = "bcrypt_sha256$$2b$12$Ev.9bbzm5eUStKgqVeonNObEDAywnE4Q/C1BbJkJbFqiyLPYj3yu6"
	u.is_superuser = 1
	u.first_name = "PolicyTracker"
	u.last_name = "Admin"
	u.email = "admin@policy-tracker.co.uk"
	u.is_staff = 1
	u.is_active = 1
	u.save()
	
	
	
	statuses = ["No Progress","In Progress", "Achieved", "Broken"]

	for status in statuses:
		s = add_status(status)

	categories = ["Culture", "Defense", "Economy", "Education", "Environment", "General", "Immigration", "Justice", "Security", "Welfare"]

	for category in categories:
		c = add_category(category)
		
	countries = [
		{
			"name": "United States of America", 
			"partyInPower": "Republicans", 
			"startDate": "2017-01-20", 
			"titleOfHead": "President", 
			"headOfState": "Donald Trump", 
			"description": "Leverage agile frameworks to provide a robust synopsis for high level overviews. Iterative approaches to corporate strategy foster collaborative thinking to further the overall value proposition. Organically grow the holistic world view of disruptive innovation via workplace diversity and empowerment. Bring to the table win-win survival strategies to ensure proactive domination. At the end of the day, going forward, a new normal that has evolved from generation X is on the runway heading towards a streamlined cloud solution. User generated content in real-time will have multiple touchpoints for offshoring. Capitalize on low hanging fruit to identify a ballpark value added activity to beta test. Override the digital divide with additional clickthroughs from DevOps. Nanotechnology immersion along the information highway will close the loop on focusing solely on the bottom line.",
			"background_image": "/media/country_images/cf2277ec2bac.jpg",
			"map_image": "/media/map_images/e3e5208ce73d.jpg",
			"slug": "united-states-of-america"
		},
		{
			"name": "United Kingdom", 
			"partyInPower": "Conservative", 
			"startDate": "2015-05-07", 
			"titleOfHead": "Prime Minister", 
			"headOfState": "Theresa May", 
			"description": "Leverage agile frameworks to provide a robust synopsis for high level overviews. Iterative approaches to corporate strategy foster collaborative thinking to further the overall value proposition. Organically grow the holistic world view of disruptive innovation via workplace diversity and empowerment. Bring to the table win-win survival strategies to ensure proactive domination. At the end of the day, going forward, a new normal that has evolved from generation X is on the runway heading towards a streamlined cloud solution. User generated content in real-time will have multiple touchpoints for offshoring. Capitalize on low hanging fruit to identify a ballpark value added activity to beta test. Override the digital divide with additional clickthroughs from DevOps. Nanotechnology immersion along the information highway will close the loop on focusing solely on the bottom line.",
			"background_image": "/media/country_images/823fcaf777e8.jpg",
			"map_image": "/media/map_images/2723e225ec14.png",
			"slug": "united-kingdom"
		},
		{
			"name": "Sweden", 
			"partyInPower": "Social Democrats", 
			"startDate": "2014-10-03", 
			"titleOfHead": "Prime Minister", 
			"headOfState": "Stefan Löfven", 
			"description": "Leverage agile frameworks to provide a robust synopsis for high level overviews. Iterative approaches to corporate strategy foster collaborative thinking to further the overall value proposition. Organically grow the holistic world view of disruptive innovation via workplace diversity and empowerment. Bring to the table win-win survival strategies to ensure proactive domination. At the end of the day, going forward, a new normal that has evolved from generation X is on the runway heading towards a streamlined cloud solution. User generated content in real-time will have multiple touchpoints for offshoring. Capitalize on low hanging fruit to identify a ballpark value added activity to beta test. Override the digital divide with additional clickthroughs from DevOps. Nanotechnology immersion along the information highway will close the loop on focusing solely on the bottom line.",
			"background_image": "/media/country_images/ef91c89c3859.jpg",
			"map_image": "/media/map_images/af7c13dd7b7b.png",
			"slug": "sweden"
		},
		{
			"name": "Russia", 
			"partyInPower": "United Russia", 
			"startDate": "2012-05-07", 
			"titleOfHead": "President", 
			"headOfState": "Vladimir Putin", 
			"description": "Leverage agile frameworks to provide a robust synopsis for high level overviews. Iterative approaches to corporate strategy foster collaborative thinking to further the overall value proposition. Organically grow the holistic world view of disruptive innovation via workplace diversity and empowerment. Bring to the table win-win survival strategies to ensure proactive domination. At the end of the day, going forward, a new normal that has evolved from generation X is on the runway heading towards a streamlined cloud solution. User generated content in real-time will have multiple touchpoints for offshoring. Capitalize on low hanging fruit to identify a ballpark value added activity to beta test. Override the digital divide with additional clickthroughs from DevOps. Nanotechnology immersion along the information highway will close the loop on focusing solely on the bottom line.",
			"background_image": "/media/country_images/6dc760994373.jpg",
			"map_image": "/media/map_images/25b7808d4dd4.png",
			"slug": "russia"
		},
		{
			"name": "France", 
			"partyInPower": "Socialist", 
			"startDate": "2012-05-15", 
			"titleOfHead": "President", 
			"headOfState": "François Hollande", 
			"description": "Leverage agile frameworks to provide a robust synopsis for high level overviews. Iterative approaches to corporate strategy foster collaborative thinking to further the overall value proposition. Organically grow the holistic world view of disruptive innovation via workplace diversity and empowerment. Bring to the table win-win survival strategies to ensure proactive domination. At the end of the day, going forward, a new normal that has evolved from generation X is on the runway heading towards a streamlined cloud solution. User generated content in real-time will have multiple touchpoints for offshoring. Capitalize on low hanging fruit to identify a ballpark value added activity to beta test. Override the digital divide with additional clickthroughs from DevOps. Nanotechnology immersion along the information highway will close the loop on focusing solely on the bottom line.",
			"background_image": "/media/country_images/11c65c1a71ea.jpg",
			"map_image": "/media/map_images/4d72ba94df22.png",
			"slug": "france"
		},
		{
			"name": "Australia", 
			"partyInPower": "Liberal", 
			"startDate": "2015-09-15", 
			"titleOfHead": "Prime Minister", 
			"headOfState": "Malcolm Turnbull", 
			"description": "Leverage agile frameworks to provide a robust synopsis for high level overviews. Iterative approaches to corporate strategy foster collaborative thinking to further the overall value proposition. Organically grow the holistic world view of disruptive innovation via workplace diversity and empowerment. Bring to the table win-win survival strategies to ensure proactive domination. At the end of the day, going forward, a new normal that has evolved from generation X is on the runway heading towards a streamlined cloud solution. User generated content in real-time will have multiple touchpoints for offshoring. Capitalize on low hanging fruit to identify a ballpark value added activity to beta test. Override the digital divide with additional clickthroughs from DevOps. Nanotechnology immersion along the information highway will close the loop on focusing solely on the bottom line.",
			"background_image": "/media/country_images/0f2e61de56fd.jpg",
			"map_image": "/media/map_images/4ed3381757da.png",
			"slug": "australia"
		}
	]
	
	for country in countries:
		add_country(country["name"], country["partyInPower"], country["startDate"], country["titleOfHead"], country["headOfState"], country["description"], country["background_image"], country["map_image"])

def add_status(name):
	s = Status.objects.get_or_create(name=name)[0]
	s.save()
	return s

def add_category(name):
	c = Category.objects.get_or_create(name=name)[0]
	c.save()
	return c

def add_country(name, partyInPower, startDate, titleOfHead, headOfState, description, background_image, map_image):
	c = Country.objects.get_or_create(name=name, partyInPower=partyInPower, startDate=startDate, titleOfHead=titleOfHead, headOfState=headOfState, description=description)[0] 
	c.background_image = background_image
	c.map_image = map_image
	c.save()
	return c
	
# Known as the populate function
if __name__ == '__main__':
	print("Starting Policy Tracker population script...")
	populate()
