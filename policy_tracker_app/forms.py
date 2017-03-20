from django import forms
from django.contrib.auth.models import User
from policy_tracker_app.models import Country, Promise, Category, UserProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput() )

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')

class CountryForm(forms.ModelForm):
    name = forms.CharField(max_length=64, help_text="Please enter the country name.")
    inPower = forms.CharField(max_length=64, help_text="Please enter the governing body/ruler.")

    class Meta:
        model = Country
        fields = ('name', 'inPower')
