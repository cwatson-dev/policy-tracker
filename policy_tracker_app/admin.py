from django.contrib import admin
from policy_tracker_app.models import Country, Policy, Category, UserProfile

class CountryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ('name', 'inPower',)

admin.site.register(Country, CountryAdmin)
admin.site.register(Policy)
admin.site.register(Category)
admin.site.register(UserProfile)
