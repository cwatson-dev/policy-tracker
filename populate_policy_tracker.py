# -*- coding: utf-8 -*-
import sys, os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','policy_tracker_project.settings')

import django
django.setup()

from random import choice, randint
from datetime import datetime
from policy_tracker_app.models import Status, Category, Country, Policy
from django.contrib.auth.models import User

# Disable printing
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore printing
def enablePrint():
    sys.stdout = sys.__stdout__

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
    statuses = ["No Progress", "In Progress", "Achieved", "Broken"]
    status_icons = ["clock-o", "wrench", "thumbs-up", "thumbs-down"]
    status_colours = ["0275d8", "f0ad4e", "5cb85c", "d9534f"]
    add_status(statuses[0], status_icons[0], status_colours[0])
    add_status(statuses[1], status_icons[1], status_colours[1])
    add_status(statuses[2], status_icons[2], status_colours[2])
    add_status(statuses[3], status_icons[3], status_colours[3])
    categories = ["Culture", "Defense", "Economy", "Education", "Environment", "General", "Immigration", "Justice", "Security", "Welfare"]
    fa_categories = ["music", "fighter-jet", "btc", "graduation-cap", "envira", "university", "globe", "balance-scale", "shield", "medkit"]
    fa_colours=["993355", "d9534f", "f0ad4e", "5bc0de", "5cb85c", "e6e6e6", "0275d8", "ffe105", "647a78", "ff5405"]
    add_category(categories[0], fa_categories[0], fa_colours[0])
    add_category(categories[1], fa_categories[1], fa_colours[1])
    add_category(categories[2], fa_categories[2], fa_colours[2])
    add_category(categories[3], fa_categories[3], fa_colours[3])
    add_category(categories[4], fa_categories[4], fa_colours[4])
    add_category(categories[5], fa_categories[5], fa_colours[5])
    add_category(categories[6], fa_categories[6], fa_colours[6])
    add_category(categories[7], fa_categories[7], fa_colours[7])
    add_category(categories[8], fa_categories[8], fa_colours[8])
    add_category(categories[9], fa_categories[9], fa_colours[9])
    countries=[
		{
			"name": "United States of America",
			"partyInPower": "Republican",
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
			"partyInPower": "Social Democrat",
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

    policies = {
		"subject": "Progressively maintain extensive infomediaries via extensible niches.",
		"description": "Leverage agile frameworks to provide a robust synopsis for high level overviews. Iterative approaches to corporate strategy foster collaborative thinking to further the overall value proposition. Organically grow the holistic world view of disruptive innovation via workplace diversity and empowerment."}
    statuses = Status.objects.all()
    categories = Category.objects.all()
    countries_obj = Country.objects.all()
    for country_obj in countries_obj:
		rand = 0
		rand = choice([24,65,54,41,68,76,34])
		i = 0
		while (i < rand):
			print(i)
			rand_status = randint(0,3)
			rand_cat = randint(0,9)
			rand_status = statuses[rand_status]
			rand_cat = categories[rand_cat]
			policy = add_policy(policies["subject"], policies["description"], country_obj, rand_status, rand_cat)
			print(policy.status)
			i += 1


def add_policy(subject, description, country, status, category):
	p = Policy.objects.get_or_create(subject=subject, description=description, country=country, status=status, category=category)[0]
	p.save()
	return p


def add_status(name, fa_icon, fa_colour):
	s = Status.objects.get_or_create(name=name, fa_icon=fa_icon, fa_colour=fa_colour)[0]
	s.save()
	return s

def add_category(name, fa_icon, fa_colour):
	cat = Category.objects.get_or_create(name=name, fa_icon=fa_icon, fa_colour=fa_colour)[0]
	cat.save()
	return cat

def add_country(name, partyInPower, startDate, titleOfHead, headOfState, description, background_image, map_image):
	c = Country.objects.get_or_create(name=name, partyInPower=partyInPower, startDate=startDate, titleOfHead=titleOfHead, headOfState=headOfState, description=description)[0]
	c.background_image = background_image
	c.map_image = map_image
	c.save()
	return c

# Known as the populate function
if __name__ == '__main__':
	print("Starting Policy Tracker population script...")
	if len(sys.argv) > 1:
		if str(sys.argv[1]) == '-debug':
			populate()
			print("Populating complete...")
	else:
		blockPrint()
		populate()
		enablePrint()
		print("Populating complete...")
		print("Completed with all messages hidden. Add '-debug' to view all logging.")
