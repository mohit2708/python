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
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib import messages, auth

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def do_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        passw = request.POST.get('password')
        user = authenticate(request, username=username, password=passw)
        if user is not None:
            form = login(request,user)
            messages.success(request, f' wecome {username} !!')
            return redirect('/home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
    
def home(request):
    return render(request, 'home.html', {'username': request.user.username})

def do_logout(request):
    auth.logout(request)
    return render(request,'logout.html')
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
 <ul class="nav navbar-nav navbar-right">
        {% if user.is_authenticated %} 
      <li><a href="{% url "logout" %}"><span class="glyphicon glyphicon-log-out"></span> Log Out</a></li>
      {% else %}
      <li><a href="{% url "signup" %}"><span class="glyphicon glyphicon-user"></span> Sign Up</a></li>
      <li><a href="{% url "login" %}"><span class="glyphicon glyphicon-log-in"></span> Login</a></li>
      {% endif %}
    </ul>
------------
<div class="container">
    {% block start %}
  {{ username }}  
  {% if request.user.is_authenticated %}
  Hello {{ request.user.first_name }}, <a href="{% url "logout" %}">Logout</a>
{% else %}
<a href="{% url "login" %}">Log-in</a>
{% endif %}
  {% endblock %}
</div>
```

### Extra Field Badane hai to
```python
===========create forms.py===========
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    mobile = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'mobile', 'password1', 'password2')
 ============views.py============
 from .forms import SignUpForm

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
```
