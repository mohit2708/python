### Ques. What are the key features of Python?
* Python is an __interpreter__ language. It means it executes the code line by line.
* Python is a high-level, interpreted, interactive and object-oriented scripting language.
* It was created by __Guido van Rossum__, and released in __1991__.
* It is used for:
  * web development (server-side),
  * software development,
  * mathematics,
  * system scripting.
 
 
### Ques. Features of Python?
1. __Easy:-__ Python is very easy to learn and understand; using this Python tutorial, any beginner can understand the basics of Python.
2. __Interpreted:-__ It is interpreted(executed) line by line. This makes it easy to test and debug.
3. __Object-Oriented:-__ The Python programming language supports classes and objects. We discussed these above.
4. __Free and Open Source:-__ The language and its source code are available to the public for free; there is no need to buy a costly license.
5. __Portable:-__ Since it is open-source, you can run Python on Windows, Mac, Linux or any other platform. Your programs will work without needing to the changed for every machine.
6. __GUI Programming:-__ You can use it to develop a GUI (Graphical User Interface). One way to do this is through Tkinter.
7. __Large Library:-__ Python provides you with a large standard library. You can use it to implement a variety of functions without needing to reinvent the wheel every time. Just pick the code you need and continue. This lets you focus on other important tasks.

### Ques. Python Frameworks?
1. Django
2. Flask
3. Pyramid
4. Tornado
5. Bottle
6. web2py
7. NumPy
8. SciPy
9. Pylons

### Ques. File Extensions in Python?
* __.py–__ The normal extension for a Python source file
* __.pyc-__ The compiled bytecode
* __.pyd-__ A Windows DLL file
* __.pyo-__ A file created with optimizations
* __.pyw-__ A Python script for Windows
* __.pyz-__ A Python script archive



### Build-In Python Module
https://docs.python.org/3/py-modindex.html<br>
Example
```python
>>> import html
>>> import html.parser
import mysql.connector
```
ye buil in packege hote hai<br>
agar or karne hai to pip ki help sa karenge

### Ques. Is indentation required in python?
Indentation is necessary for Python. It specifies a block of code. All code within loops, classes, functions, etc is specified within an indented block. It is usually done using four space characters. If your code is not indented necessarily, it will not execute accurately and will throw errors as well.
![indentation](https://github.com/mohit2708/python/blob/master/image/indentation.PNG)

### Ques. Python Comments?
__single Line Comments__
```python
#This is a comment
print("Hello, World!")

print("Hello, World!") #This is a comment
```
__Multi Line Comments(OR)Docstring__
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

### Ques. What is List?
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

##### Example of List
```python
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[1])                //Access Item ke liye
print(thislist[2:5])              //Range of Indexes (2 sa 5 tak)
print(thislist[:4])               //Range of Indexes (4 tak)
print(thislist[2:])               //2 to the end.
print(thislist[-1])               //Negative Indexing
print(thislist[-4:-1])            //-4 sa -1 tak

Output:- 
banana                                                  //Access Item
['cherry', 'orange', 'kiwi']                            //Range of Indexes (2 sa 5 tak)
['apple', 'banana', 'cherry', 'orange']                 //Range of Indexes (4 tak)
['cherry', 'orange', 'kiwi', 'melon', 'mango']          //2 to the end.
cherry                                                  //Negative Indexing
['orange', 'kiwi', 'melon']                             //-4 sa -1 tak
```

##### Examples Of list
```python
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"                          //List Change/replace Item Value
thislist.append("orange")                             //List Add Items   
thislist.insert(1, "orange")                          //add Items in partcular postion
thislist.remove("banana")                             //Remove Items
thislist.pop()                                        //remove the last item using pop
thislist.pop(1)                                       //remove the particular item using pop keyword
del thislist[0]                                       //The __del__ keyword removes the specified index:
del thislist                                          //The del keyword can also delete the list completely:
thislist.clear()                                      //The __clear()__ method empties the list:
print(thislist)                                        

Output:- 
['apple', 'blackcurrant', 'cherry']                    //List Change/replace Item Value
['apple', 'banana', 'cherry', 'orange']                //List Add Items 
['apple', 'orange', 'banana', 'cherry']                //add Items in partcular postion
['apple', 'cherry']                                    //Remove Items
['apple', 'banana']                                    //remove the last item using pop
['apple', 'cherry']                                    //remove the particular item using pop keyword
['banana', 'cherry']                                   //The __del__ keyword removes the specified index:
....................                                   //The del keyword can also delete the list completely:
[]                                                     //The __clear()__ method empties the list:

```


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


### Dictionaries
A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.<br>
Example:-
```python
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
Output:- {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
=========Accessing Items Type 1========
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
x = thisdict.get("model") // Accessing Items Type 1
print(x)
Output:- Mustang
==========Change Values============
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
print(thisdict)
Output:- {'brand': 'Ford', 'model': 'Mustang', 'year': 2018}
==========Loop Through a Dictionary Type 1=============
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
print(x)
Output:- 
brand
model
year
==========Loop Through a Dictionary Type 2=============
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
print(thisdict[x])
Output:- 
Ford
Mustang
1964
==========Loop Through a Dictionary Type 3=============
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.values():
print(x)
Output:- 
Ford
Mustang
1964
==========Loop Through a Dictionary Type 4=============
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in thisdict.items():
print(x, y)
Output:- 
brand Ford
model Mustang
year 1964
===========Check if Key Exists===========
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
print("Yes, 'model' is one of the keys in the thisdict dictionary")
Output:-
Yes, 'model' is one of the keys in the thisdict dictionary
=====Dictionary Length==========
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(len(thisdict))
Output:- 3
========Adding Items==========
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)
Output:-
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}
========Removing Items=============
*** The pop() method removes the item with the specified key name
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)
Output:- {'brand': 'Ford', 'year': 1964}

*** The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):

thisdict.popitem()
print(thisdict)
Output:- {'brand': 'Ford', 'model': 'Mustang'}

*** The del keyword removes the item with the specified key name:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)
Output:- {'brand': 'Ford', 'year': 1964}


*** The del keyword can also delete the dictionary completely:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
print(thisdict)
Output:- 
Traceback (most recent call last):
  File "demo_dictionary_del3.py", line 7, in <module>
    print(thisdict) #this will cause an error because "thisdict" no longer exists.
NameError: name 'thisdict' is not defined


*** The clear() method empties the dictionary:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)
Output:- {}
===========Copy a Dictionary===================
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)
Output:- {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

*** Another way to make a copy is to use the built-in function dict()
mydict = dict(thisdict)
print(mydict)
Output:- {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
```

### Ques. What is Set?
* Sets are used to store multiple items in a single variable.
* A set is a collection which is both unordered and unindexed.
* Sets are written with curly brackets.
* __syntex:-__ myset = {"apple", "banana", "cherry"}
* Example:-
```python
thisset = {"apple", "banana", "cherry"}
print(thisset)
Output: {'cherry', 'apple', 'banana'}
```

##### Note:-

* Sets are unordered, so you cannot be sure in which order the items will appear.
* Set items are unordered, unchangeable, and do not allow duplicate values.
* __Unordered__ means that the items in a set do not have a defined order.
* __Sets are unchangeable__, meaning that we cannot change the items after the set has been created.(Once a set is created, you cannot change its items, but you can add new items.)
* Sets __Duplicates__ Not Allowed.
```python
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
Output:-
{'banana', 'cherry', 'apple'}
```

#### Get the Length of a Set
```python
thisset = {"apple", "banana", "cherry"}
print(len(thisset))
Output:-
3
```





### What is pep 8?
PEP stands for Python Enhancement Proposal. It is a set of rules that specify how to format Python code for maximum readability.



### Object-Oriented Programming (OOP)
__How to create a class__<br>
To define a class in Python, you can use the class keyword, followed by the class name and a colon. Inside the class, an __init__ method has to be defined with def. This is the initializer that you can later use to instantiate objects. It's similar to a constructor in Java. __init__ must always be present! It takes one argument: self, which refers to the object itself. Inside the method, the pass keyword is used as of now, because Python expects you to type something there.<br>

__Instantiating objects__<br>
```python
mohit = Person()
print(mohit)
```

__Example__
```python
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
```

__Example__
```python
class Dog:

    def __init__(self, name, age):  
        self.name = name
        self.age = age

    def bark(self):
        print("bark bark!")

    def doginfo(self):
        print(self.name + " is " + str(self.age) + " year(s) old.")
        
ozzy = Dog("Ozzy", 2)
skippy = Dog("Skippy", 12)
filou = Dog("Filou", 8)

ozzy.bark()
skippy.doginfo()
filou.doginfo()
```
Output:-<br>bark bark!<br>
Skippy is 12 year(s) old.<br>
Filou is 8 year(s) old.<br>















