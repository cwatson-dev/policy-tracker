from django.contrib import admin
from policy_tracker_app.models import Country, Policy, Category, UserProfile

class CountryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    exclude = ('demonym', 'population', 'capital')
    list_display = ('name', 'partyInPower', 'startDate', 'titleOfHead', 'headOfState', 'description')

class PolicyAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject', 'country', 'status', 'category')


admin.site.register(Country, CountryAdmin)
admin.site.register(Policy, PolicyAdmin)
admin.site.register(Category)
admin.site.register(UserProfile)
