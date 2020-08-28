### Ques. What are the key features of Python?
* Python is a high-level, interpreted, interactive and object-oriented scripting language.
* It was created by Guido van Rossum, and released in 1991.
* It is used for:
  * web development (server-side),
  * software development,
  * mathematics,
  * system scripting.
  
  
### Ques. Python Comments?
__single Line Comments__
```python
#This is a comment
print("Hello, World!")

print("Hello, World!") #This is a comment
```
__Multi Line Comments__
```python
"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")
```

### Ques. Python Variables?
 * A variable name must start with a letter or the underscore character
 * A variable name cannot start with a number
 * A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
 * Variable names are case-sensitive (age, Age and AGE are three different variables)
```python
#Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#Illegal variable names:
2myvar = "John"
my-var = "John"
my var = "John"
```
__Example__
```python
x = 5
y = "Mohit"
print(x)
print(y)
```
output:- 5<br>Mohit
```python
# double quotes are the same as single quotes:
x = 4 # x is of type int
x = "saxena" # x is now of type str
x = 'mohit' # x is now of type str
print(x)
```
output:-Mohit

__Assign Value to Multiple Variables__
```python
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
```
output:- Orange<br>Banana<br>Cherry
```python
x = y = z = "Orange"
print(x)
print(y)
print(z)
```
output:- Orange<br>Orange<br>Orange



