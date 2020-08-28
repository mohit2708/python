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

__Output Variables(combine both text and a variable)__
```python
x = "awesome"
print("Python is " + x)
```
output:- Python is awesome
```python
x = "Python is "
y = "awesome"
z =  x + y
print(z)
```
output:-Python is awesome
```python
x = 5
y = 10
print(x + y)
```
output:- 15<br>

Note:- If you try to combine a string and a number, Python will give you an error:
```python
x = 5
y = "John"
print(x + y)
```
output:- TypeError: unsupported operand type(s) for +: 'int' and 'str'

### Ques. Global Variables?
 * Variables that are created outside of a function.
 * Global variables can be used by everyone, both inside of functions and outside.
__Example:-__
```python
x = "awesome"
def myfunc():
  print("Python is " + x)
myfunc()
```
output:- Python is awesome
```python
x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)
myfunc()
print("Python is " + x)
```
output:- Python is fantastic<br>Python is awesome

### Ques. Global Keyword?
In Python, global keyword allows you to modify the variable outside of the current scope. It is used to create a global variable and make changes to the variable in a local context.<br>
__Rules of global Keyword__
 * When we create a variable inside a function, it is local by default.
 * When we define a variable outside of a function, it is global by default. You don't have to use global keyword.
 * We use global keyword to read and write a global variable inside a function.
 __Example__
 ```python
 def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)
 ```
 Output:-Python is fantastic
  ```python
x = "awesome"
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)
```
output:-Python is fantastic

### Ques. How to check What type of datatype?
Python has the following data types built-in by default, in these categories:
|  |  |
|:----:| ---------|
|Text Type | str |
| Numeric Types | int, float, complex |
| Sequence Types | list, tuple, range |
| Mapping Type | dict
| Set Types | set, frozenset |
| Boolean Type | bool |
| Binary Types |	bytes, bytearray, memoryview |

```python
x = 5
print(type(x)) 
```
output:- <class 'int'>

### Ques. Python Strings?
##### String Literals
'hello' is the same as "hello".

##### Assign String to a Variable
```python
a = "Hello"
print(a)
```
Output:- Hello

##### Multiline Strings
You can assign a multiline string to a variable by using three quotes:
```python
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
```
Output:-<br>
Lorem ipsum dolor sit amet,<br>
consectetur adipiscing elit,<br>
sed do eiusmod tempor incididunt<br>
ut labore et dolore magna aliqua.<br>

### Python Collections (Arrays)?
There are four collection data types in the Python programming language:
 * __List__ is a collection which is ordered and changeable. Allows duplicate members.
 * __Tuple__ is a collection which is ordered and unchangeable. Allows duplicate members.
 * __Set__ is a collection which is unordered and unindexed. No duplicate members.
 * __Dictionary__ is a collection which is unordered, changeable and indexed. No duplicate members.

# List
A list is a collection which is ordered and changeable. In Python lists are written with square brackets[], separated by commas.
```python
my_list = ["apple", "banana", "cherry"]
my_list = [1, "Hello", 3.4]
my_list = ["mouse", [8, 4, 6], ['a']] #A list can also have another list as an item. This is called a nested list.
print(my_list)
```
output:-<br>
["apple", "banana", "cherry"]
[1, "Hello", 3.4]
["mouse", [8, 4, 6], ['a']]


```python
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[1])
print(thislist[2:5])
print(thislist[:4])
print(thislist[2:])
print(thislist[-1])
print(thislist[-4:-1])
print(thislist[-4:-1])
```
Output:- <br>
banana<br>
['cherry', 'orange', 'kiwi']<br>
['apple', 'banana', 'cherry', 'orange']<br>
cherry<br>
['cherry', 'orange', 'kiwi', 'melon', 'mango']<br>
['orange', 'kiwi', 'melon']

### List Change/replace Item Value
```python
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
```
Output:- ['apple', 'blackcurrant', 'cherry']

### List Add Items
```python
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist) 
```
Output:- ['apple', 'banana', 'cherry', 'orange']
```python
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
```
Output:- ['apple', 'orange', 'banana', 'cherry']

### List Remove Items
```python
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
```
Output:- ['apple', 'cherry']

* The __pop()__ method removes the specified index, (or the last item if index is not specified):
```python
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
```
Output:-['apple', 'banana']
```python
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
```
Output:-['apple', 'cherry']

* The __del__ keyword removes the specified index:
```python
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
```
Output:- ['banana', 'cherry']

* The del keyword can also delete the list completely:
```python
thislist = ["apple", "banana", "cherry"]
del thislist
print(thislist)
```

* The __clear()__ method empties the list: 
```python
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
```
Output:- []

### Copy a List
* Make a copy of a list with the __copy()__ method:
```python
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
```
Output:- ['apple', 'banana', 'cherry']

* Make a copy of a list with the __list()__ method:
```python
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
```
Output:- ['apple', 'banana', 'cherry']

### Join Two Lists
* One of the easiest ways are by using the + operator.
```python
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)
```
Output:- ['a', 'b', 'c', 1, 2, 3]

* Another way to join two lists are by appending all the items from list2 into list1, one by one:
```python
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)
```
Output:- ['a', 'b', 'c', 1, 2, 3]

* Use the __extend()__ method to add list2 at the end of list1:
```python
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list3 = [1, 1, 3]
list1.extend(list2)
list1.extend(list3)
print(list1)
```
Output:-
['a', 'b', 'c', 1, 2, 3, 1, 2, 3]

### list() Constructor
It is also possible to use the __list()__ constructor to make a new list.
```python
thislist = list(("apple", "banana", "cherry"))
print(thislist)
```
output:- ['apple', 'banana', 'cherry']


### Ques. Difference between List and Tuples in Python?
| List | Tuples |
|:---:|:---:|
|List is mutable.|Tuple is immutable.|
|List iteration is slower and is time consuming.|Tuple iteration is faster.|
|List is useful for insertion and deletion operations.|Tuple is useful for readonly operations like accessing elements.|
|List consumes more memory.|Tuples consumes less memory.|
|	List provides many in-built methods.|Tuples have less in-built methods.|
|List operations are more error prone|Tuples operations are safe.|


### Object-Oriented Programming (OOP)
__How to create a class__<br>
To define a class in Python, you can use the class keyword, followed by the class name and a colon. Inside the class, an ____init____ method has to be defined with def. This is the initializer that you can later use to instantiate objects. It's similar to a constructor in Java. ____init____ must always be present! It takes one argument: self, which refers to the object itself. Inside the method, the pass keyword is used as of now, because Python expects you to type something there.














