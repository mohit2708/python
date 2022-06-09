### create model.py
```python
from django.db import models

# Create your models here.
class Employee(models.Model):  
    eid = models.CharField(max_length=20)  
    ename = models.CharField(max_length=100)  
    eemail = models.EmailField()  
    econtact = models.CharField(max_length=15)  
    class Meta:  
        db_table = "employee"
```

### register in admin.py for showing the django admin
```python
from django.contrib import admin

from crud_function.models import Employee
# Register your models here.
admin.site.register(Employee)
```
