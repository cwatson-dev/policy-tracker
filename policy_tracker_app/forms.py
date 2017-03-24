from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from policy_tracker_app.models import Country, Policy, Category, UserProfile, Status

# basic user form
class UserForm(forms.ModelForm):
    # ensure password is hidden when typed
    password = forms.CharField(widget=forms.PasswordInput())
    # make user repeat password to test whether both are the same
    confirm_password = forms.CharField(widget=forms.PasswordInput(), help_text="Please retype password")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

    # ensure user has entered their password correctly by confirming both are the same
    def clean(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('confirm_password')
        # if passwords are not the same return error
        if password1 != password2:
            raise forms.ValidationError('Passwords do not match.', code='invalid')
        # validate passwords to ensure they are not simple
        password1 = validate_password(password1)
        password2 = validate_password(password2)

        return self.cleaned_data

# user profile form extension with website and picture
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')

# add country form
class CountryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, widget=forms.TextInput(attrs={'placeholder': 'Please enter the country name'}))
    partyInPower = forms.CharField(max_length=128, label="Party in Power", widget=forms.TextInput(attrs={'placeholder': 'Please enter the name of the governing party'}))
    startDate = forms.DateField(label="Start Date (eg YYYY-MM-DD)", widget=forms.TextInput(attrs={'placeholder': '2015-06-27'}))
    titleOfHead = forms.CharField(max_length=128, label="Title of Head of State", widget=forms.TextInput(attrs={'placeholder': 'Prime Minister'}))
    headOfState = forms.CharField(max_length=128, label="Name of Head of State", widget=forms.TextInput(attrs={'placeholder': 'Donald Trump'}))
    description = forms.CharField(max_length=1024, widget=forms.Textarea(attrs={'placeholder': 'Description...'}))
    background_image = forms.ImageField(required=False, label="Flag image (Preferred 1920px width, rectangular, high resolution)")
    map_image = forms.ImageField(required=False, label="Map image (At least 300px width, square, medium resolution)")

    class Meta:
        model = Country
        fields = ('name', 'partyInPower', 'startDate', 'titleOfHead', 'headOfState', 'description', 'background_image', 'map_image')

class PolicyForm(forms.ModelForm):
    subject = forms.CharField(max_length=128, widget=forms.TextInput(attrs={'placeholder': 'Please enter a subject'}), required=True)
    description = forms.CharField(max_length=1024, widget=forms.Textarea(attrs={'placeholder': 'Description...'}), required=True)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=True)
    status = forms.ModelChoiceField(queryset=Status.objects.all(), required=True)

    class Meta:
        model = Policy
        fields = ('subject', 'description', 'reference_url', 'category', 'status')
