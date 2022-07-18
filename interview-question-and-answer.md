# Interview Question And Answer

# Python interview questions

#### Table of Contents


#### Ques. What is Django?
* Django—pronounced “Jango,”. Django is a free and open source web application framework written in Python.
* Django follows the MVT (Model View Template) pattern which is based on the Model View Controller architecture.

#### Ques. Explain the django project directory structure?
<ul>
    <li><b>manage.py</b> - A command-line utility that allows you to interact with your Django project</li>
    <li><b>__init__.py</b> - An empty file that tells Python that the current directory should be considered as a Python package</li>
    <li><b>settings.py</b> - Comprises the configurations of the current project like DB connections.</li>
    <li><b>urls.py</b> - All the URLs of the project are present here</li>
    <li><b>wsgi.py</b> - This is an entry point for your application which is used by the web servers to serve the project you have created.</li>
</ul>


#### Ques. What are models in Django?
A model is a class that represents table or collection in our DB, and where every attribute of the class is a field of the table or collection. Models are defined in the app/models.py (in our example: myapp/models.py)
```python
from django.db import models

class Employee(models.Model):

   first_name = models.CharField(max_length = 50)
   middle_name = models.CharField(max_length = 50)
   last_name = models.CharField(max_length = 50)
   number = models.IntegerField()

   class Meta:
      db_table = "employee"
```

#### Ques. Name some companies that make use of Django?
Some of the companies that make use of Django are Instagram, DISCUS, Mozilla Firefox, YouTube, Pinterest, Reddit, etc.

#### Ques. What are the features of Django?
* SEO Optimized
* Extremely fast

#### Ques. How to create virtual Enviroment and How can Activate?
```python
python -m venv virtual-name

# Activate Process
virtual Enviroment Folder -> Scripts -> Activate
```

#### Ques. How to install Django and Uninstall Django?
```python
# Install Django
python -m pip install django

# Uninstall Django
pip uninstall django
```

#### Ques. How do you check for the version of Django installed on your system?
```python
# you can open the command prompt and enter the following command:
python -m django –version

# You can also try to import Django and use the get_version() method as follows:
import django
print(django.get_version())
```

#### Ques. How to Run Server?
```python
python manage.py runserver
```

#### Ques. How to create Project and App?
```python
# Create the Project
django-admin startproject projectName

# Create the app
python manage.py startapp app_name
```
