## Django
* Django is a free, open-source python based High-level Web Framwork.
* It follows the model view template(MVT) architectural pattern.
* It was orginally created By Adrian Holovaty and simon willison.

## Install
* Install Python https://www.python.org/downloads/
* python check version --> python --version/py -V
* Check pip version --> pip --version

## Installing Creating a virtual environment
```python
d:\mohit> python -m venv virtual-name
d:\mohit>cd virtual-name\Scripts
d:\mohit\virtual-name\Scripts> activate             // env activate
<virtual-name> d:\mohit> pip install django         // install django
<virtual-name> d:\mohit> pip uninstall django         // uninstall django
<virtual-name> d:\mohit> django-admin --version     // to check django version
<virtual-name> d:\mohit> django-admin startproject projectName  //project create
<virtual-name> d:\mohit\projectName> python manage.py runserver // run server
```

## create app
```pyhon
<virtual-name> d:\mohit\projectName> python manage.py startapp <app_name>
====settings.py======
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    '<app_name>',
]
```

## Url Seeting
```python
========Main urls.py=========
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('crud.urls')),
    path('admin/', admin.site.urls),    
]
==========urls.py file create in your app===============
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup),
    path('login/', views.login),
    path('', views.individual_post),
    path('create', views.stinsert, name='create1'),
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete_st), 
]
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

## view calling using template
```python
====setting.py=========
 'DIRS': ['templates'],
 =======create template folder in root directiry where is managed file=====
 =======and create file index.html ================
 <h1>Hello</h1>
 <h1>Hello {{name}}</h1>
 =====views.py=======
from django.shortcuts import render
from django.http import HttpResponse
def individual_post(request):
    return render(request, 'index.html')
    return render(request,"signup.html", {'name':'mohit'})
=======urls.py=======
from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.individual_post, name='individual_post'),
]
```

## add 2 value
```python
=====urls.py==========
path('add/', views.add1, name='addvalue'),
======koi html file=================
<form action="{% url 'addvalue' %}">
	<input type="text" name="num1">
	<input type="text" name="num2">
	<input type="submit">
</form>
======result.html file=====
results : {{result}}
==========views.py===========
def add1(request):
    val1 = int(request.GET["num1"])
    val2 = int(request.GET["num2"])
    res = val1 + val2
    return render(request, "result.html", {'result':res})
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
(env) C:\Users\mohits4\env\Scripts\testdjango> python manage.py runserver
(env) C:\Users\mohits4\env\Scripts\testdjango> pip freeze > requirements.txt
```




## create app
```python
====model.py=========
from django.db import models
# Create your models here.
class crudst(models.Model):
    stname = models.CharField(max_length = 200)
    stemail = models.EmailField(max_length = 100)
    staddress = models.CharField(max_length = 100)
    stmobile = models.IntegerField()
    stgender = models.CharField(max_length=10)
    
=====admin.py======
from django.contrib import admin
from crud.models import crudst
#from .models import crudst, crudst1 //aise bhi likh sakte hai

# Register your models here.
admin.site.register(crudst)     //app supar admin mai show hone ke liye
admin.site.register(crudst1)     //app supar admin mai show hone ke liye
====and go to cmd //jha manage.py hota hai====
D:\mohit\projectName> python manage.py makemigrations
D:\mohit\projectName> python manage.py migrate


```

