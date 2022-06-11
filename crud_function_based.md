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

Type1:-
# from blog.models import Film, Genre
# admin.site.register(Film)
# admin.site.register(Genre)
----------------------------------
Type2:-
# @admin.register(Blogs)

# class BlogsAdmin(admin.ModelAdmin):
# 	list_display = ['id', 'title']
```

### Regiter URL
create urls.py file in your app and include the project urls.py
```python
//create urls.py

from django.contrib import admin  
from django.urls import path  
from crud_function import views
urlpatterns = [   
    path('',views.show, name='list'),
    path('create/', views.create),
    path('store/', views.store, name='store'),
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update, name='update'),  
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
### Show Data
create list.html in template folder
```python
{% for employee in employees %}
    <tr>
	<td>{{ employee.eid }}</td>
	<td>{{ employee.ename }}</td>
	<td>{{ employee.eemail }}</td>
	<td>{{ employee.econtact }}</td>
	<td>
	    <a href="/crud_function/edit/{{ employee.id }}" class="edit" ><i class="material-icons" data-toggle="tooltip" title="Edit">&#xE254;</i></a>
	    <a href="/crud_function/delete/{{ employee.id }}" class="delete"><i class="material-icons" data-toggle="tooltip" title="Delete">&#xE872;</i></a>
	    <!-- <a href="/create/{{ employee.id }}"><span class="glyphicon glyphicon-pencil" >Edit</span></a>   -->
	</td>
    </tr>
{% endfor %}
```
create function in view.py
```python
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect  
from django.urls import reverse
# from crud_function.forms import EmployeeForm  
from crud_function.models import Employee

def show(request):
	employees = Employee.objects.all()
	return render(request,"crud_function/list.html",{'employees':employees})
```


### Create Data
create file add.html in template
```python
<h1>Add member</h1>

<form action="store/" method="post">
<form action="{% url 'store' %}" method="post">
{% csrf_token %}
Name:<br>
<input type="text" name="fname">
<br><br>
 Email:<br>
<input type="email" name="email">
<br><br>
 Phone:<br>
<input type="number" name="phone">
<br><br>
<input type="submit" value="Submit">
</form>
```
Create function in view.py
```python
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect  
from django.urls import reverse
# from crud_function.forms import EmployeeForm  
from crud_function.models import Employee

def create(request):
	return render(request,"crud_function/add.html")

def store(request):
	print('storeeee')
	fname = request.POST['fname']
	email = request.POST['email']
	phone = request.POST['phone']
	storeData = Employee(ename=fname, eemail=email,econtact=phone)
	storeData.save()
	return HttpResponseRedirect(reverse('list'))
```

### Edit Update data
create Edit file in temlate section
```python
<h1>Update member</h1>

<form action="update/{{ employee.id }}" method="post">
<form action="{% url 'update' employee.id %}" method="post">
{% csrf_token %}
Name:<br>
<input name="fname" value="{{ employee.ename }}">
<br><br>
email:<br>
<input name="email" value="{{ employee.eemail }}">
<br><br>
Contact:<br>
<input name="phone" value="{{ employee.econtact }}">
<br><br>
<input type="submit" value="Submit">
</form>
```
Create function in view.py
```python

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect  
from django.urls import reverse
# from crud_function.forms import EmployeeForm  
from crud_function.models import Employee

def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request,'crud_function/edit.html', {'employee':employee})

def update(request, id):
	fname = request.POST['fname']
	email = request.POST['email']
	phone = request.POST['phone']
	
	updateData = Employee.objects.get(id=id)
	updateData.ename = fname
	updateData.eemail = email
	updateData.econtact = phone
	updateData.save()
	return HttpResponseRedirect(reverse('list'))
```

### Delete Data
In list table
```python
<a href="/crud_function/delete/{{ employee.id }}">Delete</a>
```
Urls.py
```python
path('delete/<int:id>', views.destroy),  
```
view.py
```python
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect  
from django.urls import reverse
# from crud_function.forms import EmployeeForm  
from crud_function.models import Employee

def destroy(request, id):  
    del_data = Employee.objects.get(id=id)  
    del_data.delete()  
    # return redirect("/list")
    return HttpResponseRedirect(reverse('list'))
```
