from django.contrib import admin
from policy_tracker_app.models import Country, Policy, Category, UserProfile

admin.site.register(Country)
admin.site.register(Policy)
admin.site.register(Category)
admin.site.register(UserProfile)
