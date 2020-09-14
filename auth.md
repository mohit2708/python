## Auth By Defalt

```python
=========setting.py===========
'DIRS': ['templates'],

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'auth_app',
]


=======urls.py=========
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.signup),
    path('signup/', views.signup),    
    path('login/', views.login),    
]
========views.py=========
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'login.html')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return render(request, 'home.html')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
=========signup.html================
<h1>Signup</h1>
    <form action="/signup/" method="post">
        {% csrf_token %}
        {{ form }}
        <input type="submit" value="Signup">
    </form>
=========login.html================
<h1>Log In</h1>
    <form action="/login/" method="post">
        {% csrf_token %}
        {{ form }}
        <input type="submit" value="Log In">
    </form>
======Home.html===========
<h1>Home</h1>

```
