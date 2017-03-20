from django import forms
from django.contrib.auth.models import User
from policy_tracker_app.models import UserProfile

class UserForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(), help_text="Please retype password")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
        widgets = {
            'password': forms.PasswordInput(attrs={"class":"test"}),
        }

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        if cleaned_data['password'] != cleaned_data['confirm_password']:
            raise forms.ValidationError("The two passwords entered do not match.")

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')
