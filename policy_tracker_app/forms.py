from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from policy_tracker_app.models import Country, Policy, Category, UserProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput(), help_text="Please retype password")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

    def clean(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('confirm_password')

        if password1 != password2:
            raise forms.ValidationError('Passwords do not match.', code='invalid')

        password1 = validate_password(password1)
        password2 = validate_password(password2)

        return self.cleaned_data

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')

class CountryForm(forms.ModelForm):
    name = forms.CharField(max_length=64, help_text="Please enter the country name.")
    inPower = forms.CharField(max_length=64, help_text="Please enter the governing body/ruler.")
    map_image_url = forms.CharField(disabled=True)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Country
        fields = ('name', 'inPower', 'description', 'background_image')
