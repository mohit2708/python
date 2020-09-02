## Django
* Django is a free, open-source python based High-level Web Framwork.
* It follows the model view template(MVT) architectural pattern.
* It was orginally created By Adrian Holovaty and simon willison.

## Install
* Install Python https://www.python.org/downloads/
* python check version --> python --version/py -V
* Check pip version --> pip --version
* Installing Django Open cmd --> pip install django
* django check version --> python -m django --version/django-admin --version
* Uninstall Django :--> pip uninstall django

## Installing Creating a virtual environment
```python
d:\mohit> py -m venv virtual-name
d:\mohit>cd virtual-name\Scripts\activate
<virtual-name> d:\mohit> py -m pip install Django
<virtual-name> d:\mohit> django-admin --version
```

__Installing virtualenv:-__
```python
py -m pip install --user virtualenv
```
__Creating a virtual environment:-__
```python
py -m venv env
```
__Activating a virtual environment:-__
```python
.\env\Scripts\activate
```
```python
C:\Users\mohits4\env\Scripts>activate    //envirment mai jane ke liye
(env) C:\Users\mohits4\env\Scripts>      //envirment se bhar aane ke liye
```
You can confirm you’re in the virtual environment by checking the location of your Python interpreter, it should point to the env directory.
```python
where python
.../env/bin/python.exe
```
__Leaving the virtual environment:-__
```python
deactivate
```
__Installing packages:-__
```python
pip install requests
```
```python
cd C:\Users\mohits4\env\Scripts
django-admin startproject projectName
cd projectName
Python manage.py runserver
```

### Envirment mai version check karna
```python
(env) C:\Users\mohits4>django-admin --version
```

### envirment mai django delete karna
```python
(env) C:\Users\mohits4>pip uninstall django
```

## Create admin interface
```python
(env) C:\Users\mohits4\env\Scripts\testdjango>python manage.py migrate
(env) C:\Users\mohits4\env\Scripts\testdjango>python manage.py createsuperuser
user
email
pass
(env) C:\Users\mohits4\env\Scripts\testdjango>python manage.py createsuperuser

pip freeze > requirements.txt
```

### View calling
```python
=========urls.py======================
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.individual_post, name='individual_post'),
]
======create viesw.py file=============
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello, welcome to the index page.')


def individual_post(request):
    return HttpResponse('Hi, this is where an individual post will be. mohit')

```

## Template calling
```python
====setting.py=========
 'DIRS': ['templates'],
 =======create template folder in root directiry where is managed file=====
 =======and create file index.html ================
 <h1>Hello</h1>
 =====views.py=======
from django.shortcuts import render
from django.http import HttpResponse
def individual_post(request):
    return render(request, 'index.html')
=======urls.py=======
from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.individual_post, name='individual_post'),
]
```


## Check version

* pip check --> pip --version
* django check --> django-admin --version

