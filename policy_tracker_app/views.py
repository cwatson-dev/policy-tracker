from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm, UserChangeForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from datetime import datetime

from social_django.models import UserSocialAuth
from policy_tracker_app.models import Country, Policy, Category, Status
from policy_tracker_app.forms import UserForm, UserProfileForm, CountryForm, PolicyForm


def home(request):
    user = request.user
    if user.is_authenticated():
        auth_providers = []
        try:
            logins = user.social_auth.filter(user_id=user.id)
            for i in range(0, len(logins)):
                auth_provider = logins[i]
                if i < (len(logins) - 2):
                    auth_providers.append(auth_provider.provider + ",")
                else:
                    auth_providers.append(auth_provider.provider)
            if len(auth_providers) > 1:
                auth_providers.insert((len(auth_providers) - 1), "and")
                auth_providers.append("accounts.")
            else:
                auth_providers.append("account.")
            auth_providers = [provider.replace('google-oauth2', 'Google').replace('f', 'F').replace('tw', 'Tw').replace('gi', 'Gi') for provider in auth_providers]
        except UserSocialAuth.DoesNotExist:
            auth_providers = None

        context_dict = {
            'logins': auth_providers,
        }

    else:
        context_dict = {}

    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    context_dict['last_visit'] = request.session['last_visit']

    return render(request, 'policy_tracker/home.html', context_dict)

def about(request):
    context_dict = {'author': "Chris Watson - 2190594W"}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    context_dict['last_visit'] = request.session['last_visit']
    context_dict['nbar'] = 'about'
    return render(request, 'policy_tracker/about.html', context_dict)


def country(request, country_name_slug):
    context_dict = {}
    policy_statuses = {'No Progress': 0, 'In Progress': 0, "Achieved": 0, 'Broken': 0}
    status_fillers = []

    try:
        country = Country.objects.get(slug=country_name_slug)
        policies = Policy.objects.filter(country=country)
        context_dict['country'] = country
        context_dict['policies'] = policies
        for policy in policies:
            policy_statuses[policy.status.name] += 1
        noProgress = policy_statuses['No Progress']
        inProgress = policy_statuses['In Progress']
        achieved = policy_statuses['Achieved']
        broken = policy_statuses['Broken']
        policy_statuses = [noProgress, inProgress, achieved, broken]
        if len(policies) > 0:
            status_fillers = [
                ((float(noProgress)/float(len(policies)))*100),
                ((float(inProgress)/float(len(policies)))*100),
                ((float(achieved)/float(len(policies)))*100),
                ((float(broken)/float(len(policies)))*100),
            ]

    except Country.DoesNotExist:
        context_dict['country'] = None
        context_dict['policies'] = None

    context_dict['policy_statuses'] = policy_statuses
    context_dict['status_fillers'] = status_fillers
    context_dict['policy_table'] = True
    return render(request, 'policy_tracker/country.html', context_dict)


def countries(request):
    country_list = Country.objects.all()
    policy_list = []
    for country in country_list:
        policy_list.append(Policy.objects.filter(country=country))
    context_dict = {'countries': country_list, 'policies': policy_list}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    context_dict['last_visit'] = request.session['last_visit']
    context_dict['nbar'] = 'countries'
    return render(request, 'policy_tracker/countries.html', context_dict)


@login_required
def add_country(request):
    if request.method == 'POST':
        country_form = CountryForm(data=request.POST)

        if country_form.is_valid():
            country = country_form.save(commit=False)

            if 'background_image' in request.FILES:
                country.background_image = request.FILES['background_image']
            if 'map_image' in request.FILES:
                country.map_image = request.FILES['map_image']

            country.save()

            return HttpResponseRedirect('/countries/' + country.slug)
        else:
            print(country_form.errors)
    else:
        country_form = CountryForm()

    return render(request, 'policy_tracker/add_country.html', {"country_form": country_form, 'add_country': True})

@login_required
def add_policy(request, country_name_slug):
    context_dict = {}
    try:
        country = Country.objects.get(slug=country_name_slug)
    except Country.DoesNotExist:
        context_dict['country'] = None
        return render(request, 'policy_tracker/add_policy.html', context_dict)

    if request.method == 'POST':
        policy_form = PolicyForm(data=request.POST)

        if policy_form.is_valid():
            policy = policy_form.save(commit=False)

            policy.country = country

            policy.save()

            return HttpResponseRedirect('/policy/' + str(policy.id))
        else:
            print(policy_form.errors)
    else:
        policy_form = PolicyForm()


    return render(request, 'policy_tracker/add_policy.html', {"policy_form": policy_form, 'country': country})


@login_required
def policy(request, policy_id):
    try:
        policy = Policy.objects.get(id=policy_id)
    except Policy.DoesNotExist:
        policy = None
        return render(request, 'policy_tracker/policy.html', {'policy': policy, 'policy_id': policy_id})

    return render(request, 'policy_tracker/policy.html', {'policy': policy})


def register(request):
    if request.user.is_authenticated:
        return render(request, 'policy_tracker/register.html',
                  {'logged_in': True})
    else:
        registered = False

        if request.method == 'POST':
            user_form = UserForm(data=request.POST)
            profile_form = UserProfileForm(data=request.POST)

            if user_form.is_valid() and profile_form.is_valid():
                user = user_form.save()
                user.set_password(user.password)
                user.save()

                profile = profile_form.save(commit=False)
                profile.user = user

                if 'picture' in request.FILES:
                    profile.picture = request.FILES['picture']

                profile.save()

                registered = True
            else:
                print(user_form.errors, profile_form.errors)
        else:
            user_form = UserForm()
            profile_form = UserProfileForm()

        return render(request, 'policy_tracker/register.html',
                  {'user_form': user_form, 'profile_form': profile_form,
                   'registered': registered})



def user_login(request):
    if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(username=username, password=password)

            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('home'))
                else:
                    return HttpResponse("Your Policy Tracker account is disabled.")
            else:
                errorMessage = "Invalid login details. Username '{0}' does not match the password provided.".format(username)
                return render(request, 'policy_tracker/login.html', {'error': errorMessage, 'username': format(username)})
    else:
        return render(request, 'policy_tracker/login.html', {})

@login_required
def profile_settings(request):
    user = request.user

    try:
        google_login = user.social_auth.get(provider='google-oauth2')
    except UserSocialAuth.DoesNotExist:
        google_login = None

    try:
        github_login = user.social_auth.get(provider='github')
    except UserSocialAuth.DoesNotExist:
        github_login = None

    try:
        twitter_login = user.social_auth.get(provider='twitter')
    except UserSocialAuth.DoesNotExist:
        twitter_login = None

    try:
        facebook_login = user.social_auth.get(provider='facebook')
    except UserSocialAuth.DoesNotExist:
        facebook_login = None

    can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())

    return render(request, 'policy_tracker/profile_settings.html', {
        'google_login': google_login,
        'github_login': github_login,
        'twitter_login': twitter_login,
        'facebook_login': facebook_login,
        'can_disconnect': can_disconnect
    })

@login_required
def profile_password(request):
    if request.user.has_usable_password():
        PasswordForm = PasswordChangeForm
    else:
        PasswordForm = AdminPasswordChangeForm

    if request.method == 'POST':
        form = PasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordForm(request.user)
    return render(request, 'policy_tracker/profile_password.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val

def visitor_cookie_handler(request):
    visits = int(get_server_side_cookie(request, 'visits', '1'))
    last_visit_cookie = get_server_side_cookie(request, 'last_visit', str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7], '%Y-%m-%d %H:%M:%S')

    if (datetime.now() - last_visit_time).days > 0:
        visits = visits + 1

        request.session['last_visit'] = str(datetime.now())
    else:
        visits = 1

        request.session['last_visit'] = last_visit_cookie

    request.session['visits'] = visits

def contactus(request):
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    context_dict['last_visit'] = request.session['last_visit']
    return render(request, 'policy_tracker/contactus.html', context_dict)

def faq(request):
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    context_dict['last_visit'] = request.session['last_visit']
    return render(request, 'policy_tracker/faq.html', context_dict)

def news(request):
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    context_dict['last_visit'] = request.session['last_visit']
    context_dict['nbar'] = 'news'
    return render(request, 'policy_tracker/news.html', context_dict)
