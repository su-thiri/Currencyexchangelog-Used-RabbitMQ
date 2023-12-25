from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import UserAccessLog
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
import requests
from user_agents import parse
from currency_app import tasks


@login_required
def user_dashboard(request):
   
    # data = UserAccessLog.objects.create(
    #     user = request.user,
    #     country=request.META.get('HTTP_X_APP_USER_COUNTRY', 'Unknown'), 
    #     browser=request.META.get('HTTP_USER_AGENT', 'Unknown')
    # )
    # Get user's country using a geolocation API (replace 'YOUR_API_KEY' with a valid key)
    

    geo_api_url = f'https://api.ipstack.com/{request.META["REMOTE_ADDR"]}?access_key=395fe2ca6638c2d469f52114fc009161'
    geo_response = requests.get(geo_api_url)
    geo_data = geo_response.json()
    country = geo_data.get('country_name', 'Myanmar')

    # Get browser information from User-Agent header
    user_agent = parse(request.META.get('HTTP_USER_AGENT', ''))
    browser = user_agent.browser.family

    # Create a new UserAccessLog instance and associate it with the current user
    data = UserAccessLog.objects.create(
        user=request.user,
        country=country,
        browser=browser,
    )
    
    user_info = {
        'username': request.user.username,
        'country': data.country,
        'browser': data.browser,
    }

    
    

    return render(request, 'user_dashboard.html', {'user_info': user_info})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('user_dashboard')
    else:
        form = AuthenticationForm()

    return render(request, 'user_login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('user_login')

def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('user_dashboard')
    else:
        form = UserCreationForm()

    return render(request, 'user_register.html', {'form': form})