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
```python
python3 manage.py makemigrations
python3 manage.py migrate  
```

### register in admin.py for showing the django admin
```python
from django.contrib import admin

from crud_function.models import Employee
# Register your models here.
admin.site.register(Employee)
```

### Regiter URL
create urls.py file in your app and include the project urls.py
```python
//create urls.py

from django.contrib import admin  
from django.urls import path  
from crud_function import views
urlpatterns = [   
    path('list',views.show),
    path('emp', views.emp),    
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),  
]

//add url.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    path('crud_function/', include('crud_function.urls')),
]

```
