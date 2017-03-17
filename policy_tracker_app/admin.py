from django.contrib import admin
from policy_tracker_app.models import Country, Promise, Category, UserProfile

admin.site.register(Country)
admin.site.register(Promise)
admin.site.register(Category)
admin.site.register(UserProfile)
