# Interview Question And Answer

### Ques. What is Django?
* Django—pronounced “Jango,”. Django is a free and open source web application framework written in Python.
* Django follows the MVT (Model View Template) pattern which is based on the Model View Controller architecture.

### Ques. Explain the django project directory structure?
* __manage.py__ - A command-line utility that allows you to interact with your Django project
* <pre>__init__.py - An empty file that tells Python that the current directory should be considered as a Python package</pre>
* __settings.py__ - Comprises the configurations of the current project like DB connections.
* __urls.py__ - All the URLs of the project are present here
* __wsgi.py__ - This is an entry point for your application which is used by the web servers to serve the project you have created.

### Ques. What are models in Django?
A model is a class that represents table or collection in our DB, and where every attribute of the class is a field of the table or collection. Models are defined in the app/models.py (in our example: myapp/models.py)
```python
from django.db import models

class Dreamreal(models.Model):

   website = models.CharField(max_length = 50)
   mail = models.CharField(max_length = 50)
   name = models.CharField(max_length = 50)
   phonenumber = models.IntegerField()

   class Meta:
      db_table = "dreamreal"
```

### Ques. Name some companies that make use of Django?
Some of the companies that make use of Django are Instagram, DISCUS, Mozilla Firefox, YouTube, Pinterest, Reddit, etc.

### Ques. What are the features of Django?
* SEO Optimized
* Extremely fast

### Ques. How do you check for the version of Django installed on your system?
```python
you can open the command prompt and enter the following command:
python -m django –version
```
```
You can also try to import Django and use the get_version() method as follows:
import django
print(django.get_version())
```

### Ques. 
