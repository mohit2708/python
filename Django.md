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


## Check version

* pip check --> pip --version
* django check --> django-admin --version

