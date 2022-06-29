# Python interview questions

### Table of Contents

| No. | Questions |
|:----:| ---------
| 1 | [What Is Python?](#Ques-what-is-Python) |
| 2 | [Features of Python?](#Ques-Features-of-Python) |
| 2 | [Python Frameworks?](#Ques-Python-Frameworks) |
| 3 | [File Extensions in Python?](#Ques-File-Extensions-in-Python) |
|   | [Python Comments?](#Ques-Python-Comments) |
|   | [Python Variables?](#ques-python-variables) |
|   | [Global Variables?](#ques-global-variables) |
|   | [How to check What type of datatype?](#ques-how-to-check-what-type-of-datatype) |
|   | [Python Strings?](#ques-python-strings) |
|   | [Python Shallow Copy and Deep Copy?](#ques-python-shallow-copy-and-deep-copy) |
|   | [What is built-in module in Python?](#Ques-What-is-built-in-module-in-Python) |
|   | [Is indentation required in python?](#ques-is-indentation-required-in-python) |
|   | [How is memory managed in Python?](#ques-how-is-memory-managed-in-python) |
|   | [What is PEP 8?](#ques-what-is-pep-8) |
|   | [Global Keyword?](#ques-global-keyword) |
|   | [Python Collections (Arrays)?](#python-collections-arrays) |
|   | [What is List?](#ques-what-is-list) / [Access List Items](#access-list-items) / [Change List Items](#change-list-items) / [Add List Items](#add-list-items) / [Remove List Items](#remove-list-items) / [Loop Lists](#loop-lists) / [Copy Lists](#copy-lists) / [Join Lists](#join-lists) /  [List Comprehension](#list-comprehension) / [List Methods](#list-methods) / [list() Constructor](#list-constructor) | 
|   | [What is difference between Discard() and Remove()?](#) | 
|   | [What isTuples?](#ques-what-is-tuples) / [Tuple Length](#tuple-length) / [Create Tuple With One Item](#create-tuple-with-one-item) / [Access Tuple Items](#access-tuple-items) / [Update Tuples](#update-tuples) / [Unpack Tuples](#unpack-tuples) / [Loop Tuples](#loop-tuples) / [Join Tuples](#join-tuples) / [Tuple Methods](#tuple-methods) / [tuple() Constructor](#tuple-constructor) |
|   | [Difference between List and Tuples in Python?](#ques-difference-between-list-and-tuples-in-python) |
|   | [What is Set?](#ques-what-is-set) / [Length of a Set](#get-the-length-of-a-set) / [Acesss Items of set](#acesss-items-of-set) / [Remove Item of set](#remove-item-of-set-) / [Loop Sets](#loop-sets) / [Join Two Set](#join-two-set) / [set() Constructor](#set-constructor) / [Set Methods](#set-methods) |
|   | [What is Dictionaries?](#ques-what-is-dictionaries) / (Dictionary Length)[#dictionary-length] / [Access Item](#access-item-of-dictionary) / [Change Dictionary Items](#change-dictionary-items) / [Add Dictionary Items](#add-dictionary-items) / [Remove Dictionary Items](#remove-dictionary-items) / [Copy Dictionaries](#copy-dictionaries) / [loop-dictionaries](#loop-dictionaries) / [Nested Dictionaries](#nested-dictionaries) / [Dictionary Methods](#dictionary-methods) |



### Ques. What is Python?
* Python is a high-level, interpreted, general-purpose programming language.
* Python is an __interpreter__ language. It means it executes the code line by line
* It was created by __Guido van Rossum__, and released in __1991__
* It is used for:
  * web development (server-side)
  * software development
  * mathematics
  * system scripting


**[⬆ Back to Top](#table-of-contents)**
### Ques. Features of Python?
1. __Easy:-__ Python is very easy to learn and understand; using this Python tutorial, any beginner can understand the basics of Python.
2. __Interpreted:-__ It is interpreted(executed) line by line. This makes it easy to test and debug.
3. __Object-Oriented:-__ The Python programming language supports classes and objects. We discussed these above.
4. __Free and Open Source:-__ The language and its source code are available to the public for free; there is no need to buy a costly license.
5. __Portable:-__ Since it is open-source, you can run Python on Windows, Mac, Linux or any other platform. Your programs will work without needing to the changed for every machine.
6. __GUI Programming:-__ You can use it to develop a GUI (Graphical User Interface). One way to do this is through Tkinter.
7. __Large Library:-__ Python provides you with a large standard library. You can use it to implement a variety of functions without needing to reinvent the wheel every time. Just pick the code you need and continue. This lets you focus on other important tasks.


**[⬆ Back to Top](#table-of-contents)**
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

**[⬆ Back to Top](#table-of-contents)**
### Ques. File Extensions in Python?
* __.py–__ The normal extension for a Python source file
* __.pyc-__ The compiled bytecode
* __.pyd-__ A Windows DLL file
* __.pyo-__ A file created with optimizations
* __.pyw-__ A Python script for Windows
* __.pyz-__ A Python script archive


### Ques. Python Comments?
__single Line Comments:-__ Comments starts with a #
```python
#This is a comment
print("Hello, World!")

print("Hello, World!") #This is a comment
```
__Multi Line Comments(OR)Docstring__
* To add a multiline comment you could insert a # for each line.
* you can add a multiline string (triple quotes) in your code, and place your comment inside it.
```python
"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")
```

**[⬆ Back to Top](#table-of-contents)**
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

<details>
  <summary>Assign Value to Multiple Variables</summary>
  
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
</details>

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

**[⬆ Back to Top](#table-of-contents)**
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

**[⬆ Back to Top](#table-of-contents)**
### Ques. How to check What type of datatype?
Python has the following data types built-in by default, in these categories:
| | |
|:----:| ---------|
|Text Type | str("Hello World") |
| Numeric Types | int(20), float(20.5), complex(1j) |
| Sequence Types | list, tuple, range |
| Mapping Type | dict
| Set Types | set, frozenset |
| Boolean Type | bool |
| Binary Types |	bytes, bytearray, memoryview |

* We can get the data type of any object by using the __type()__ function.
```python
x = 5
print(type(x)) 
```
output:- <class 'int'>

**[⬆ Back to Top](#table-of-contents)**
**[⬆ Back to Top](#table-of-contents)**
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

##### Slicing Strings
```python
b = "Hello, World!"
   print(b[2:5])
 
Output:- llo

# Slice From the Start:- Get the characters from the start to position 5 (not included):
b = "Hello, World!"
print(b[:5])

Output:- Hello

# Slice To the End:- Get the characters from position 2, and all the way to the end:
b = "Hello, World!"
print(b[2:])

Output:- llo, World!
 
# Negative Indexing:- Get the characters from position 2, and all the way to the end:
b = "Hello, World!"
print(b[-5:-2])

Output:- orl
```
 
##### Modify Strings
```python
# Upper Case.:- The __upper()__ method returns the string in upper case.
a = "Hello, World!"
print(a.upper())

Output:- HELLO, WORLD!
----------------------------------------------------------------------------------

# Lower Case:- The __lower()__ method returns the string in lower case.
a = "Hello, World!"
print(a.lower())

Output:- hello, world!
----------------------------------------------------------------------------------

# Remove Whitespace:- 
# Whitespace is the space before and/or after the actual text, and very often you want to remove this space.
# The __strip()__ method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip())

Output:- Hello, World!
------------------------------------------------------------------------------------- 

# Replace String:- The __replace()__ method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))

Output:- Jello, World!
----------------------------------------------------------------------------------------------

# Split String:- The split() method splits the string into substrings if it finds instances of the separator:
a = "Hello, World!"
b = a.split(",")
print(b)

Output:- ['Hello', ' World!']
```

##### String Concatenation
```python
# String Concatenation:- To concatenate, or combine, two strings you can use the + operator.
a = "Hello"
b = "World"
c = a + b
print(c)

Output:- HelloWorld

# To add a space between them, add a " ":
a = "Hello"
b = "World"
c = a + " " + b
print(c)

Output:- Hello World
```

##### Format - Strings
```python
# String Format:- As we learned in the Python Variables chapter, we cannot combine strings and numbers like this.
age = 36
txt = "My name is John, I am " + age
print(txt) 

Output:- 
Traceback (most recent call last):
File "demo_string_format_error.py", line 2, in <module>
   txt = "My name is John, I am " + age
TypeError: must be str, not int


# we can combine strings and numbers by using the __format()__ method!
# The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:
   age = 36
    txt = "My name is John, and I am {}"
    print(txt.format(age))
 
   output:- My name is John, and I am 36

 
# The format() method takes unlimited number of arguments, and are placed into the respective placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price)) 

output:- I want 3 pieces of item 567 for 49.95 dollars.
 
# You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
 
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price)) 

Output:- I want to pay 49.95 dollars for 3 pieces of item 567
```
 
<details>
  <summary>Escape Characters</summary>

* An escape character is a backslash \ followed by the character you want to insert.
 
  ```python
    txt = "We are the so-called \"Vikings\" from the north."
    print(txt) 

    output:- We are the so-called "Vikings" from the north.
  ```

### Single Quote
  ```python
    txt = 'It\'s alright.'
    print(txt)  

    output:- It's alright.
  ```

### Backslash 
  ```python
    txt = "This will insert one \\ (backslash)."
    print(txt)   

    output:- This will insert one \ (backslash).
  ```

### New Line 
  ```python
    txt = "Hello\nWorld!"
    print(txt)    

    output:- 
Hello
World!
  ```

### Carriage Return
    ```python
    txt = "Hello\rWorld!"
    print(txt)

    Output:-
Hello
World!
    ```

### Tab
    ```python
    txt = "Hello\tWorld!"
    print(txt)

    Output:- Hello   World!
    ```

### Backspace
    ```python
    txt = "Hello \bWorld!"
    print(txt)

    Output:- HelloWorld!
    ```

### Octal value	
    ```python
    txt = "\110\145\154\154\157"
    print(txt)

    Output:- Hello
    ```

### Hex value
    ```python
    txt = "\x48\x65\x6c\x6c\x6f"
    print(txt) 

    Output:- Hello
    ```
 
</details>

### Ques. How to get Id()?
id() function takes a single parameter object.
```python
a = 5
print(id(a))
```


**[⬆ Back to Top](#table-of-contents)**
### Ques. Python Shallow Copy and Deep Copy?
__Deep Copy:-__ In deep copy any changes made to a copy of object do not reflect in the orginal object.
```python
import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.deepcopy(old_list)

new_list[1][0] = 'BB'

print("Old list:", old_list)
print("New list:", new_list)

Output:- 
Old list: [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
New list: [[1, 1, 1], ['BB', 2, 2], [3, 3, 3]]
```
__Shallow copy:-__ A shallow copy creates a new object which stores the reference of the original elements.
```python
 import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.copy(old_list)

new_list[1][1] = 'AA'

print("Old list:", old_list)
print("New list:", new_list)

Output:- 
Old list: [[1, 1, 1], [2, 'AA', 2], [3, 3, 3]]
New list: [[1, 1, 1], [2, 'AA', 2], [3, 3, 3]]
```
 
**[⬆ Back to Top](#table-of-contents)**
### Ques. What is built-in module in Python?
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


**[⬆ Back to Top](#table-of-contents)**
### Ques. How is memory managed in Python?
* Python also has an inbuilt garbage collector, which recycles all the unused memory and so that it can be made available to the heap space.
* Memory management in python is managed by Python private heap space. All Python objects and data structures are located in a private heap. The programmer does not have access to this private heap. The python interpreter takes care of this instead.
* The allocation of heap space for Python objects is done by Python’s memory manager. The core API gives access to some tools for the programmer to code.

**[⬆ Back to Top](#table-of-contents)**
### Ques. What is PEP 8?
* PEP stands for __Python Enhancement Proposal__. 
* PEP8 is a document that provides various guidline to write the readable in python.
* PEP8 describe how the developers can write the beautiful code.

**[⬆ Back to Top](#table-of-contents)**
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

**[⬆ Back to Top](#table-of-contents)**
### Python Collections (Arrays)?
There are four collection data types in the Python programming language:
 * __List__ is a collection which is ordered and changeable. Allows duplicate members.
 * __Tuple__ is a collection which is ordered and unchangeable. Allows duplicate members.
 * __Set__ is a collection which is unordered and unindexed. No duplicate members.
 * __Dictionary__ is a collection which is unordered, changeable and indexed. No duplicate members.


**[⬆ Back to Top](#table-of-contents)**
### a=1, b=1 does both have same Id or not?
Two variables in Python have same id, but not lists.
```python
a = 10
b = 10
print(id(a))
print(id(b))

Output:- 
9788992
9788992
---------------------------------------------
# In List
a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)

Output:- False
---------------------------------------------------
# In tuples
a = (1, 2, 3)
b = (1, 2, 3)
print(a is b)

Output:- True
```

**[⬆ Back to Top](#table-of-contents)**
### What is the Difference Between “is” and “==” in Python?
* ==operator is used to check whether two variables reference objects with the same value.
* is operator is used to check whether two variables point to the same object in memory.

**[⬆ Back to Top](#table-of-contents)**
### Ques. What is List?
* Lists are used to store multiple items in a single variable.
* List items are ordered, changeable, and allow duplicate values.
* In Python lists are written with square brackets[], separated by commas.
 
1. The list is __changeable__, meaning that we can change, add, and remove items in a list after it has been created.
2. Since lists are indexed, lists can have items with the __same value.__

```python
my_list = ["apple", "banana", "cherry"]
my_list = [1, "Hello", 3.4]
my_list = ["mouse", [8, 4, 6], ['a']] #A list can also have another list as an item. This is called a nested list.
print(my_list)
 
output:-
["apple", "banana", "cherry"]
[1, "Hello", 3.4]
["mouse", [8, 4, 6], ['a']]
```

**[⬆ Back to Top](#table-of-contents)**
##### Access List Items
```python
# Access Items
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[1])

Output:- banana
-----------------------------------------------------------------------------
# Negative Indexing
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-1])

Output:- mango
----------------------------------------------------------------------------- 
 
# Range of Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(thislist[2:5]) //Range of Indexes (2 sa 5 tak)
print(thislist[:4])  //Range of Indexes (4 tak)
print(thislist[2:])  //2 to the end.
print(thislist[-4:-1]) //-1 sa -4 tak

Output:- ['cherry', 'orange', 'kiwi']
Output:- ['apple', 'banana', 'cherry', 'orange']
Output:- ['cherry', 'orange', 'kiwi', 'melon', 'mango']
Output:- ['orange', 'kiwi', 'melon']
-----------------------------------------------------------------------------

# Check if Item Exists
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

Output:- Yes, 'apple' is in the fruits list
```
 
**[⬆ Back to Top](#table-of-contents)**
##### Change List Items
```python
# Change Item Value:- To change the value of a specific item, refer to the index number.
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"

print(thislist)

Output:- ['apple', 'blackcurrant', 'cherry']
------------------------------------------------

# Change a Range of Item Values:- To change the value of items within a specific range, define a list
  # with the new values, and refer to the range of index numbers where you want to insert the new values.
# 1 se 2 wale range ke element hut jaynge
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

Output:- ['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']
```

**[⬆ Back to Top](#table-of-contents)**
##### Add List Items
```python
# Append Items:- add an item to the end of the list, use the append() method.
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

Output:- ['apple', 'banana', 'cherry', 'orange']
-----------------------------------------------------------------------------
# List Insert Items:- The insert() method inserts an item at the specified index.
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

Output:- ['apple', 'orange', 'banana', 'cherry']
----------------------------------------------------------------------------- 
 
# Extend List:- To append elements from another list to the current list, use the extend() method.
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]

thislist.extend(tropical)

print(thislist)

Output:- ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']
-----------------------------------------------------------------------------

# Add Any Iterable:- The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")

thislist.extend(thistuple)

print(thislist) 

Output:- ['apple', 'banana', 'cherry', 'kiwi', 'orange']
```

**[⬆ Back to Top](#table-of-contents)**
##### Remove List Items
```python
# Remove Specified Item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

Output:- ['apple', 'cherry']
-----------------------------------------------------------------------------
# Remove Specified Index
# The pop() method removes the specified index.
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

Output:- ['apple', 'cherry']

# If you do not specify the index, the pop() method removes the last item.
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

Output:- ['apple', 'banana']

# The del keyword also removes the specified index:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

Output:- ['banana', 'cherry']

# The del keyword can also delete the list completely.
thislist = ["apple", "banana", "cherry"]
del thislist
print(thislist) #this will cause an error because you have succsesfully deleted "thislist".

Output:- Error
----------------------------------------------------------------------------- 
 
# Clear the List:- The clear() method empties the list.
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

Output:- []
```

**[⬆ Back to Top](#table-of-contents)**
##### Loop Lists
```python
# Loop Through a List
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

Output:- 
apple
banana
cherry
--------------------------------------------------------------------------------

# Loop Through the Index Numbers
# You can also loop through the list items by referring to their index number.
#Use the range() and len() functions to create a suitable iterable.
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

Output:-
 apple
 banana
 cherry
---------------------------------------------------------------------------------

# Using a While Loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

Output:-
 apple
 banana
 cherry
-------------------------------------------------------------------------------------

# Looping Using List Comprehension
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

Output:-
 apple
 banana
 cherry
``` 

**[⬆ Back to Top](#table-of-contents)**
##### Copy Lists
```python
# Make a copy of a list with the copy() method.
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

Output:- ['apple', 'banana', 'cherry']
-----------------------------------------------------------------------------
# Another way to make a copy is to use the built-in method list().
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

Output:- ['apple', 'banana', 'cherry']
```

**[⬆ Back to Top](#table-of-contents)**
##### Join Lists
```python
# There are several ways to join, or concatenate, two or more lists in Python.
# One of the easiest ways are by using the + operator.
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

Output:- ['a', 'b', 'c', 1, 2, 3]
--------------------------------------------------------------------------------

# Another way to join two lists is by appending all the items from list2 into list1, one by one:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

Output:- ['a', 'b', 'c', 1, 2, 3]
---------------------------------------------------------------------------------

# Or you can use the extend() method, which purpose is to add elements from one list to another list.
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

Output:-['a', 'b', 'c', 1, 2, 3]
```

**[⬆ Back to Top](#table-of-contents)**
##### List Comprehension
* List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
__Syntax__ newlist = [expression for item in iterable if condition == True]
```python
# Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.

# Without list comprehension you will have to write a for statement with a conditional test inside.
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

# With list comprehension you can do all that with only one line of code:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]

print(newlist)

Output:- ['apple', 'banana', 'mango']
```  

**[⬆ Back to Top](#table-of-contents)**
##### Sort Lists
```python
# Sort List Alphanumerically
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

Output:- ['banana', 'kiwi', 'mango', 'orange', 'pineapple']

# Example2:-
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

Output:- [23, 50, 65, 82, 100]
---------------------------------------------------------------------------
# Sort Descending:- To sort descending, use the keyword argument reverse = True:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

Output:- ['pineapple', 'orange', 'mango', 'kiwi', 'banana']
-------------------------------------------------------------------------------
# Case Insensitive Sort:- By default the sort() method is case sensitive, resulting 
# in all capital letters being sorted before lower case letters:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

Output:- ['Kiwi', 'Orange', 'banana', 'cherry']

# So if you want a case-insensitive sort function, use str.lower as a key function:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

Output:- ['banana', 'cherry', 'Kiwi', 'Orange']
------------------------------------------------------------------------------------
# Reverse Order:- The reverse() method reverses the current sorting order of the elements.
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist) 

Output:- ['cherry', 'Kiwi', 'Orange', 'banana']
```
                        
**[⬆ Back to Top](#table-of-contents)**
##### List Methods
                        
| Method  | Description |
| ------------- | ------------- |
| append()  | Adds an element at the end of the list  |
| clear()  | Removes all the elements from the list  |
| copy() | Returns a copy of the list |
| count() | Returns the number of elements with the specified value |
| extend() | Add the elements of a list (or any iterable), to the end of the current list |
| index() | Returns the index of the first element with the specified value |
| insert() | Adds an element at the specified position |
| pop() | Removes the element at the specified position |
| remove() | Removes the item with the specified value |
| reverse() | Reverses the order of the list |
| sort() | Sorts the list |

```python
# append():- Adds an element at the end of the list
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)

Output:- ['apple', 'banana', 'cherry', 'orange']

# Example2:-
a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
a.append(b)
print(a)

Output:- ['apple', 'banana', 'cherry', ["Ford", "BMW", "Volvo"]]
------------------------------------------------------------------
                        
# clear():-	Removes all the elements from the list
fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)

Output:- []
-------------------------------------------------------------------
# copy():-	Returns a copy of the list
fruits = ["apple", "banana", "cherry"]
x = fruits.copy()
print(x)

Output:- ['apple', 'banana', 'cherry']
-------------------------------------------------------------------
                        
# count():-	Returns the number of elements with the specified value
fruits = [1, 4, 2, 9, 7, 8, 9, 3, 1]
x = fruits.count(9)
print(x)

Output:- 2
--------------------------------------------------------------------

# extend():-	Add the elements of a list (or any iterable), to the end of the current list
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)
                        
output:- ['apple', 'banana', 'cherry', 'Ford', 'BMW', 'Volvo']
--------------------------------------------------------------------

# index():-	Returns the index of the first element with the specified value
fruits = [4, 55, 64, 32, 16, 32]
x = fruits.index(32)
print(x)
                        
Output:- 3
------------------------------------------------------------------------

# insert():-	Adds an element at the specified position
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")
print(fruits)

Output:- ['apple', 'orange', 'banana', 'cherry']
-----------------------------------------------------------------------
                                        
# pop():-	Removes the element at the specified position
fruits = ['apple', 'banana', 'cherry']
x = fruits.pop(1)
print(x)
print(fruits)
                        
output:- 
banana
['apple', 'cherry']
----------------------------------------------------------------------

# remove():-	Removes the item with the specified value
fruits = ['apple', 'banana', 'cherry']
fruits.remove("banana")
print(fruits)
                        
Output:- ['apple', 'cherry']
----------------------------------------------------------------------
                        
# reverse():-	Reverses the order of the list
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)                        
                        
Output:- ['cherry', 'banana', 'apple']
----------------------------------------------------------------------
                        
# sort():-	Sorts the list
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)

Output:- ['BMW', 'Ford', 'Volvo']

# Parameter Values in sort()
 1. reverse:- tional. reverse=True will sort the list descending. Default is reverse=False
 2. key	Optional. A function to specify the sorting criteria(s)

Example:- 
cars = ['Ford', 'BMW', 'Volvo']
cars.sort(reverse=True)
print(cars)

Output:- ['Volvo', 'Ford', 'BMW']

Example2:-
def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(key=myFunc)
print(cars)

Output:- ['VW', 'BMW', 'Ford', 'Mitsubishi']
                        
Example3:- 
def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(reverse=True, key=myFunc)
print(cars)
                        
Output:- ['Mitsubishi', 'Ford'', 'BMW', 'VW']
 
Example4:- 
def myFunc(e):
  return e['year']

cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]

cars.sort(key=myFunc)

print(cars)

Output:- 
[{'car': 'Mitsubishi', 'year': 2000}, {'car': 'Ford', 'year': 2005}, {'car': 'VW', 'year': 2011}, {'car': 'BMW', 'year': 2019}]
```

**[⬆ Back to Top](#table-of-contents)**
##### list() Constructor
It is also possible to use the __list()__ constructor to make a new list.
```python
thislist = list(("apple", "banana", "cherry"))
print(thislist)

Output:- ['apple', 'banana', 'cherry']
```

**[⬆ Back to Top](#table-of-contents)**
##### Multiply a Python List by a Number Using a for loop
```python
numbers = [1, 2, 3, 4, 5]
multiplied = []
for number in numbers:
    multiplied.append(number * 2)
print(multiplied)
Output:- [2, 4, 6, 8, 10]
```

**[⬆ Back to Top](#table-of-contents)**
##### Multiply a Python List by a Number Using a list comprehension
```python
numbers = [1, 2, 3, 4, 5]
multiplied = [number * 2 for number in numbers]
print(multiplied)
Output:- [2, 4, 6, 8, 10]
```


**[⬆ Back to Top](#table-of-contents)**
### Ques. What is Tuples?
* Tuples are used to store multiple items in a single variable.
* A tuple is a collection which is ordered and unchangeable.
* Tuples are written with round brackets.
* Tuple items are ordered, unchangeable, and allow duplicate values.
* A tuple can contain different data types.
```python
thistuple = ("apple", "banana", "cherry")
tuple1 = ("abc", 34, True, 40, "male")
print(thistuple)

Output:- ('apple', 'banana', 'cherry')
```

**[⬆ Back to Top](#table-of-contents)**
##### Tuple Length
To determine how many items a tuple has, use the len() function
```python
thistuple = tuple(("apple", "banana", "cherry"))
print(len(thistuple))

Output:- 3
```

**[⬆ Back to Top](#table-of-contents)**
##### Create Tuple With One Item
To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
```python
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

Output:-
<class 'tuple'>
<class 'str'>
```

**[⬆ Back to Top](#table-of-contents)**
##### tuple() Constructor
```python
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)

Output:- ('apple', 'banana', 'cherry')
```

**[⬆ Back to Top](#table-of-contents)**
##### Access Tuple Items
```python
# Access Tuple Items
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

Output:- banana
-----------------------------------------------------

# Negative Indexing
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

Output:- cherry
------------------------------------------------------

# Range of Indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
print(thistuple[:4])
print(thistuple[2:])
print(thistuple[-4:-1])

Output:- ('cherry', 'orange', 'kiwi')
Output:- ('apple', 'banana', 'cherry', 'orange')
Output:- ('cherry', 'orange', 'kiwi', 'melon', 'mango')
Output:- ('orange', 'kiwi', 'melon')
------------------------------------------------------

# Check if Item Exists
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

Output:- Yes, 'apple' is in the fruits tuple
```

**[⬆ Back to Top](#table-of-contents)**
##### Update Tuples
* Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
* You can convert the tuple into a list, change the list, and convert the list back into a tuple.
```python
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

Output:- ("apple", "kiwi", "cherry")
----------------------------------------------------------------

# Add Items
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

print(thistuple)

output:- ('apple', 'banana', 'cherry', 'orange')
---------------------------------------------------------------------

# Remove Items
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

print(thistuple)

Output:- ('banana', 'cherry')

# Example2:-
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple)

Output:- Error
----------------------------------------------------------------------

# Add tuple to a tuple
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

Output:- ('apple', 'banana', 'cherry', 'orange')
```

**[⬆ Back to Top](#table-of-contents)**
##### Unpack Tuples
```python
# packing a Tuple:- When we create a tuple, we normally assign values to it. This is called "packing" a tuple.
fruits = ("apple", "banana", "cherry")
print(fruits)

Output:- ('apple', 'banana', 'cherry')

# Unpacking a Tuple:- in Python, we are also allowed to extract the values back into variables. This is called "unpacking".
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

Output:- 
apple
banana
cherry

# Example2 Using Asterisk (*):-
#If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list. 
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

Output:- 
apple
['mango', 'papaya', 'pineapple']
cherry
```

**[⬆ Back to Top](#table-of-contents)**
#####  Loop Tuples
```python
# Loop Through a Tuple
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
  
Output:- 
apple
banana
cherry
-----------------------------------------------------------------------

# Loop Through the Index Numbers
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
  
Output:-
apple
banana
cherry
----------------------------------------------------------------------

# Using a While Loop
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
  
Output:- 
apple
banana
cherry
```

**[⬆ Back to Top](#table-of-contents)**
##### Join Tuples
```python
# Join Two Tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

Output:- 
('a', 'b', 'c', 1, 2, 3)
-------------------------------------------------------

# Multiply Tuples
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

Output:- ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')
```

##### Tuple Methods
| Method | Description |
| ------ | ----------- |
| count() |	Returns the number of times a specified value occurs in a tuple |
| index() | Searches the tuple for a specified value and returns the position of where it was found |

```python
# Tuple count() Method
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x)

Output:- 2
-------------------------------------------------------------------------------

# Tuple index() Method:- Search for the first occurrence of the value 8, and return its position.
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(x)

Output:- 3
```

**[⬆ Back to Top](#table-of-contents)**
### Ques. Difference between List and Tuples in Python?
| List | Tuples |
|:---:|:---:|
|List is mutable. i.e they can be edited.|Tuple is immutable. (tuples are lists which can’t be edited).|
|List iteration is slower and is time consuming.|Tuple iteration is faster.|
|List is useful for insertion and deletion operations.|Tuple is useful for readonly operations like accessing elements.|
|List consumes more memory.|Tuples consumes less memory.|
|List is stored in two blocks of memory (One is fixed sized and the other is variable sized for storing data)|Tuple is stored in a single block of memory.|
|List provides many in-built methods.|Tuples have less in-built methods.|
|List operations are more error prone|Tuples operations are safe.|
|Syntax: list_1 = [10, ‘Chelsea’, 20]	|Syntax: tup_1 = (10, ‘Chelsea’ , 20)|



**[⬆ Back to Top](#table-of-contents)**
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
* Set items can be of any data type.(String, int and boolean)
```python
set1 = {"abc", 34, True, 40, "male"}
print(set1)
output:-
{True, 34, 40, 'male', 'abc'}
```

**[⬆ Back to Top](#table-of-contents)**
##### Get the Length of a Set
```python
thisset = {"apple", "banana", "cherry"}
print(len(thisset))
Output:-
3
```

**[⬆ Back to Top](#table-of-contents)**
##### Acesss Items of set
```python			
# Loop through the set, and print the values.
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)
			
output:-
apple
cherry
banana
-----------------------------------------------------------------

# Check if "banana" is present in the set:
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)
			
output:-
True
```

**[⬆ Back to Top](#table-of-contents)**			
##### Add Items of set:-
```python
# To add one item to a set use the add() method.
			
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
			
Output:-
{'cherry', 'orange', 'apple', 'banana'}
---------------------------------------------------------------------
			
# Try to add an element that already exists:
thisset = {"apple", "banana", "cherry"}
thisset.add("apple")
print(thisset)

Output:- 
{'banana', 'apple', 'cherry'}			
--------------------------------------------------------------------------------
			
# To add items from another set into the current set, use the update() method.
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
			
output:-
{'apple', 'mango', 'cherry', 'pineapple', 'banana', 'papaya'}
-----------------------------------------------------------------------

# Add Any Iterable:- The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)
			
Output:-
{'banana', 'cherry', 'apple', 'orange', 'kiwi'}
```

**[⬆ Back to Top](#table-of-contents)**
##### Remove Item of set:-
```python
# To remove an item in a set, use the remove(), or the discard() or pop() method.
# Note:- If the item to remove does not exist, remove() will raise an error.
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
			
Output:-
{'apple', 'cherry'}

--------------------------------------------------------------------------------
# Note:- If the item to remove does not exist, __discard()__ will NOT raise an error.
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
			
Output:-
{'apple', 'cherry'}
			
-------------------------------------------------------------------------
# __Note:-__ You can also use the pop() method to remove an item, but this method will remove the last item. Remember that sets are unordered, so you will not know # # what item that gets removed.
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x) #removed item
print(thisset) #the set after removal
			
Output:-
banana
{'cherry', 'apple'}
			
---------------------------------------------------------------------
# The clear() method empties the set:
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)
			
output:-
set()

--------------------------------------------------------------------
# The del keyword will delete the set completely:
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset) #this will raise an error because the set no longer exists
			
output:-
Error
```

**[⬆ Back to Top](#table-of-contents)**
##### Loop Sets
```python
# Loop Items
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)
			
Output:- 
banana
cherry
apple
```

**[⬆ Back to Top](#table-of-contents)**
##### Join Two Set
You can use the union() method that returns a new set containing all items from both sets, or the update() method that inserts all the items from one set into another.
			
```python
# The union() method returns a new set with all items from both sets.
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
			
output:-
{'a', 1, 2, 3, 'b', 'c'}
-----------------------------------------------------------------------------
			
# The update() method inserts the items in set2 into set1.
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)
			
output:-
{'b', 'c', 1, 'a', 2, 3}
--------------------------------------------------------------------------------

# NOTE:- Note: Both union() and update() will exclude any duplicate items.
			
# The intersection_update() method will keep only the items that are present in both sets.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)
			
output:-
{'apple'}
----------------------------------------------------------------------------------

# The intersection() method will return a new set, that only contains the items that are present in both sets.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)

output:-
{'apple'}
-----------------------------------------------------------------------------------			

# The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)

output:-
{'google', 'banana', 'microsoft', 'cherry'}
----------------------------------------------------------------------------------------------

# The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)
			
output:-
{'google', 'banana', 'microsoft', 'cherry'}
```

**[⬆ Back to Top](#table-of-contents)**
##### set() Constructor
* It is also possible to use the set() constructor to make a set(the double round-brackets).
```python
thisset = set(("apple", "banana", "cherry"))
print(thisset)
output:-
{'apple', 'banana', 'cherry'}
```

##### What is difference between Discard() and Remove()?
This method is different from the discard() method, because the remove() method will raise an error if the specified item does not exist, and the discard() method will not.
```python
# Discard
numbers = {1, 2, 3, 4, 5}
numbers.discard(3)
print(numbers)

Output:- {1, 2, 4, 5}

numbers = {1, 2, 3, 4, 5}
numbers.discard(13)
print(numbers)

Output:- {1, 2, 3, 4, 5}
-------------------------------------------------
# Remove.
numbers = {1, 2, 3, 4, 5}
numbers.remove(3)
print(numbers)

Output:- {1, 2, 4, 5}

numbers = {1, 2, 3, 4, 5}
numbers.remove(31)
print(numbers)

Output:- Error
```

**[⬆ Back to Top](#table-of-contents)**
##### Set Methods
| Method | Description |
| ------ | ----------- |
| add() | Adds an element to the set |
| clear() | Removes all the elements from the set |
| copy() | Returns a copy of the set |
| difference() | Returns a set containing the difference between two or more sets |
| difference_update() | Removes the items in this set that are also included in another, specified set |
| discard() | Remove the specified item |
| intersection() | Returns a set, that is the intersection of two other sets |
| intersection_update() | Removes the items in this set that are not present in other, specified set(s) |
| isdisjoint() | Returns whether two sets have a intersection or not |
| issubset() | Returns whether another set contains this set or not |
| issuperset() | Returns whether this set contains another set or not |
| pop()	| Removes an element from the set |
| remove() | Removes the specified element |
| symmetric_difference() | Returns a set with the symmetric differences of two sets |
| symmetric_difference_update() | inserts the symmetric differences from this set and another |
| union() | Return a set containing the union of sets |
| update() | Update the set with the union of this set and others |

```python
# add():-  Adds an element to the set
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

Output:- {'cherry', 'orange', 'apple', 'banana'}
# Example2:- Try to add an element that already exists:

thisset = {"apple", "banana", "cherry"}
thisset.add("apple")
print(thisset)

Output:- {'apple', 'banana', 'cherry'}
-----------------------------------------------------------------------------------

# clear():- Removes all the elements from the set
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

Output:- set()
------------------------------------------------------------------------------------

# copy():- Returns a copy of the set
fruits = {"apple", "banana", "cherry"}
x = fruits.copy()
print(x)

Output:- {'banana', 'apple', 'cherry'}
--------------------------------------------------------------------------------------
# difference():- Returns a set containing the difference between two or more sets

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.difference(y) 

print(z)

Output:- {'cherry', 'banana'}

# Example2:- Reverse the first example. Return a set that contains the items that only exist in set y, and not in set x:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = y.difference(x) 

print(z)

Output:- {'microsoft', 'google'}
----------------------------------------------------------------------------------------

# difference_update():- Removes the items in this set that are also included in another, specified set

# The difference_update() method removes the items that exist in both sets.

# The difference_update() method is different from the difference() method, because the difference() method returns a new set, without the 
# unwanted items, and the difference_update() method removes the unwanted items from the original set.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.difference_update(y) 

print(x)

Output:- {'banana', 'cherry'}
-----------------------------------------------------------------------------------------

# discard():- Remove the specified item
# This method is different from the remove() method, because the remove() method will raise an error if the specified item does not exist, 
# and the discard() method will not.
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

Output:- {'cherry', 'apple'}
-------------------------------------------------------------------------------------------

# intersection():- Returns a set, that is the intersection of two other sets
x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}

result = x.intersection(y, z)

print(result)

Output:- {'c'}
-------------------------------------------------------------------------------------------

# intersection_update():- Removes the items in this set that are not present in other, specified set(s)
# The intersection_update() method is different from the intersection() method, because the intersection() method returns a new set, without the 
# unwanted items, and the intersection_update() method removes the unwanted items from the original set.
x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}

x.intersection_update(y, z)

print(x)

Output:- {'c'}
------------------------------------------------------------------------------------------------

# isdisjoint():- Returns whether two sets have a intersection or not
# Return True if no items in set x is present in set y:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}

z = x.isdisjoint(y) 

print(z)

Output:- True
-------------------------------------------------------------------------------------------------

# issubset():- Returns whether another set contains this set or not
# Return True if all items in set x are present in set y:

x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

z = x.issubset(y) 

print(z)

Output:- True
--------------------------------------------------------------------------------------------------

# issuperset():- Returns whether this set contains another set or not
# Return True if all items set y are present in set x:

x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}

z = x.issuperset(y)

print(z)

Output:- True
--------------------------------------------------------------------------------------------------

# pop():- The pop() method removes a random item from the set.
fruits = {"apple", "banana", "cherry"}
fruits.pop() 
print(fruits)

Output:- {'apple', 'banana'}
--------------------------------------------------------------------------------------------------

# remove():- The remove() method removes the specified element from the set.
# This method is different from the discard() method, because the remove() method will raise an error if the specified item does not exist, and the discard() method will not.
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana") 
print(fruits)

Output:- {'cherry', 'apple'}
--------------------------------------------------------------------------------------------------

# symmetric_difference():- Return a set that contains all items from both sets, except items that are present in both sets:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y) 

print(z)

Output:- {'google', 'microsoft', 'banana', 'cherry'}

--------------------------------------------------------------------------------------------------

# symmetric_difference_update():- Remove the items that are present in both sets, AND insert the items that is not present in both sets:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y) 

print(x)

Output:- {'google', 'banana', 'microsoft', 'cherry'}

--------------------------------------------------------------------------------------------------

# union():- Return a set containing the union of sets
x = {"a", "b", "c"}
y = {"f", "d", "a"}
z = {"c", "d", "e"}

result = x.union(y, z) 

print(result)

Output:- {'b', 'e', 'f', 'd', 'c', 'a'}
--------------------------------------------------------------------------------------------------

# update():- The update() method updates the current set, by adding items from another set (or any other iterable).
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.update(y) 

print(x)

Output:- {'microsoft', 'banana', 'cherry', 'google', 'apple'}
```


**[⬆ Back to Top](#table-of-contents)**
### Ques. What is Dictionaries?

* Dictionaries are written with curly brackets, and have keys and values.
* Dictionary items are ordered, changeable, and does not allow duplicates.
* Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

Example:-
```python
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
Output:- {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
```

**[⬆ Back to Top](#table-of-contents)**
* __Duplicates Not Allowed__
```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
Output:- {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}
```

**[⬆ Back to Top](#table-of-contents)**
###### Dictionary Length:- To determine how many items a dictionary has, use the len() function.
```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(len(thisdict))
Output:- 3
```

**[⬆ Back to Top](#table-of-contents)**
* __Dictionary Items - Data Types:__ The values in dictionary items can be of any data type.
```python
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)
Output:- {'brand': 'Ford', 'electric': False, 'year': 1964, 'colors': ['red', 'white', 'blue']}
```

**[⬆ Back to Top](#table-of-contents)**
##### Access Item of Dictionary
```python
# You can access the items of a dictionary by referring to its key name, inside square brackets.
thisdict =	{
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict["model"]
print(x)

Output:- Mustang

# get() Method
thisdict =	{
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict.get("model")
print(x)

Output:- Mustang
--------------------------------------------------------------------------------
# Get Keys of the Dictionary:- The keys() method will return a list of all the keys in the dictionary.
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change

Output:- 
dict_keys(['brand', 'model', 'year'])
dict_keys(['brand', 'model', 'year', 'color'])
-----------------------------------------------------------------------------

# Get Values of the Dictionary and We can change the value of a specific item by referring to its key name.
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change

Output:-
dict_values(['Ford', 'Mustang', 1964])
dict_values(['Ford', 'Mustang', 2020])
------------------------------------------------------------------------------

# Get Items :- The items() method will return each item in a dictionary, as tuples in a list.
thisdict = {
   "brand": "Ford",
   "model": "Mustang",
   "year": 1964
}

x = thisdict.items()

print(x)

Output:- dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
------------------------------------------------------------------------------

# Check if Key Exists
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

Output:- Yes, 'model' is one of the keys in the thisdict dictionary
```

**[⬆ Back to Top](#table-of-contents)**
##### Change Dictionary Items
```python
# Change Values:- We can change the value of a specific item by referring to its key name.
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict["year"] = 2018

print(thisdict)

Output:- {'brand': 'Ford', 'model': 'Mustang', 'year': 2018}
---------------------------------------------------------------------------------

# Update Dictionary:- The update() method will update the dictionary with the items from the given argument.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

print(thisdict)

Output:- {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}
```

**[⬆ Back to Top](#table-of-contents)**
##### Add Dictionary Items
```python
# Adding Items
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

Output:- {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}

# Adding Items using Update() Method
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})

print(thisdict)

Output:- {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}
```

**[⬆ Back to Top](#table-of-contents)**
##### Remove Dictionary Items
```python
# Removing item using pop() methods.
# The pop() method removes the item with the specified key name:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

Output:- {'brand': 'Ford', 'year': 1964}
--------------------------------------------------------------------------------

# Removing item using popitem() methods
# method removes the last inserted item (in versions before 3.7, a random item is removed instead).
thisdict =	{
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
thisdict.popitem()
print(thisdict)

Output:-  {'brand': 'Ford', 'model': 'Mustang'}
----------------------------------------------------------------------------------

# Removing item using del methods
# keyword removes the item with the specified key name.
thisdict =	{
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
del thisdict["model"]
print(thisdict)

Output:-  {'brand': 'Ford', 'year': 1964}
---------------------------------------------------------------------------------

# The Removing item using del methods keyword can also delete the dictionary completely.
thisdict =	{
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
del thisdict
print(thisdict)

Output:-  this will cause an error because "thisdict" no longer exists.
----------------------------------------------------------------------------------

# The Removing item using clear() methods method empties the dictionary.
thisdict =	{
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
thisdict.clear()
print(thisdict)

Output:-  {}
```

**[⬆ Back to Top](#table-of-contents)**
##### Copy Dictionaries
```python
# Copy a Dictionary using copy() method.
thisdict =	{
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
mydict = thisdict.copy()
print(mydict)

Output:-  {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
-----------------------------------------------------------------------

# Another way to make a copy is to use the built-in function dict().
thisdict =	{
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
mydict = dict(thisdict)
print(mydict)

Output:-  {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
```

**[⬆ Back to Top](#table-of-contents)**
##### Loop Dictionaries
```python
# Print all key names in the dictionary, one by one:
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
---------------------------------------------------------------------------------

# You can use the keys() method to return the keys of a dictionary:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.keys():
  print(x)

Output:-
brand
model
year
---------------------------------------------------------------------------------

# Print all values in the dictionary, one by one:
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
-------------------------------------------------------------------------------------

# You can also use the values() method to return values of a dictionary:
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
--------------------------------------------------------------------------------------

# Loop through both keys and values, by using the items() method:
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
```

**[⬆ Back to Top](#table-of-contents)**
##### Nested Dictionaries
A dictionary can contain dictionaries, this is called nested dictionaries.
```python
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)

Output:-
{'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}
-------------------------------------------------------------------------------------------

# Example2:-
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily)

Output:- 
{'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}

```

**[⬆ Back to Top](#table-of-contents)**
##### Dictionary Methods
```python
| Method | Description |
| ------ | ----------- |
| clear() |	Removes all the elements from the dictionary |
| copy() | Returns a copy of the dictionary |
| fromkeys() | Returns a dictionary with the specified keys and value. |
| get() | Returns the value of the specified key. |
| items() | Returns a list containing a tuple for each key value pair. |
| keys() | Returns a list containing the dictionary's keys. |
| pop() | Removes the element with the specified key. |
| popitem() | Removes the last inserted key-value pair. |
| setdefault() | Returns the value of the specified key. If the key does not exist: insert the key, with the specified value. |
| update() | Updates the dictionary with the specified key-value pairs. |
| values() | Returns a list of all the values in the dictionary. |

```python
# Dictionary clear() Method:- The clear() method removes all the elements from a dictionary.
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()

print(car)

Output:- {}
------------------------------------------------------------------------------------

# Dictionary copy() Method:- The copy() method returns a copy of the specified dictionary.
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.copy()

print(x)

Output:- 
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
-----------------------------------------------------------------------------------------

# Dictionary fromkeys() Method:- The fromkeys() method returns a dictionary with the specified keys and the specified value.
# Example1:-
x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)

Output:- ['key1': 0, 'key2': 0, 'key3': 0]

# Example2:- 
x = ('key1', 'key2', 'key3')
thisdict = dict.fromkeys(x)
print(thisdict)

Output:- ['key1': None, 'key2': None, 'key3': None]
------------------------------------------------------------------------------------------

# Dictionary get() Method:- The get() method returns the value of the item with the specified key.
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.get("model")

print(x)

Output:- Mustang

# Example2:-
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.get("price", 15000)

print(x)

Output:- 15000
--------------------------------------------------------------------------------------------

# Dictionary items() Method:- The items() method returns a view object. The view object contains the \n key-value pairs of the dictionary, as tuples in a list.
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.items()
print(x)

Output:- dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

# example2:- 
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.items()
car["year"] = 2018
print(x)

Output:- dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2018)])
------------------------------------------------------------------------------------------------------

# Dictionary keys() Method:- The keys() method returns a view object. The view object contains the keys of the dictionary, as a list.
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.keys()
print(x)

car["color"] = "white"
print(x)

Output:- dict_keys(['brand', 'model', 'year'])
Output:- dict_keys(['brand', 'model', 'year', 'color'])
------------------------------------------------------------------------------------------------------

# Dictionary pop() Method:- The pop() method removes the specified item from the dictionary.
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.pop("model")
print(x)
print(car)

Output:- Mustang
Output:- {'brand': 'Ford', 'year': 1964}
-------------------------------------------------------------------------------------------------

# Dictionary popitem() Method:- The popitem() method removes the item that was last inserted into the dictionary.
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.popitem()

print(x)
print(car)

Output:- 
('year', 1964)
{'brand': 'Ford', 'model': 'Mustang'}
-------------------------------------------------------------------------------------------------

# Dictionary setdefault() Method:- The setdefault() method returns the value of the item with the specified key.
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("color", "White")
y = car.setdefault("model", "Bronco")

print(x)
print(y)

Output:- White
Output:- Mustang
---------------------------------------------------------------------------------------------

# Dictionary update() Method:- The update() method inserts the specified items to the dictionary.
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.update({"color": "White"})

print(car)

Output:- {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'White'}
------------------------------------------------------------------------------------------------

# Dictionary values() Method:- The values() method returns a view object. The view object contains the values of the dictionary, as a list.
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.values()

print(x)

Output:- dict_values(['Ford', 'Mustang', 1964])

# Example2:-
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.values()

car["year"] = 2018

print(x)

Output:- dict_values(['Ford', 'Mustang', 2018])
```


			
			
			
### Ques. What is If Else?
* Equals: a == b
* Not Equals: a != b
* Less than: a < b
* Less than or equal to: a <= b
* Greater than: a > b
* Greater than or equal to: a >= b

```python
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
output:- a is greater than b
```

* __Short Hand If__
```python
a = 200
b = 33

if a > b: print("a is greater than b")
output:- "a is greater than b"
```

* __Short Hand If ... Else__
```python
a = 2
b = 330

print("A") if a > b else print("B")
output:- B
```

* One line if else statement, __with 3 conditions:__
```python
a = 330
b = 330

print("A") if a > b else print("=") if a == b else print("B")
Output:- =
```

* The __and__ keyword is a logical operator, and is used to combine conditional statements.
```python
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
output:- Both conditions are True
```

* The __Or__ keyword is a logical operator, and is used to combine conditional statements.
```python
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
output:- At least one of the conditions is True
```

* __Nested If__ You can have if statements inside if statements, this is called nested if statements.
```python
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
Output:- 
Above ten,
and also above 20!
```

* __The pass Statement__ if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
```python
a = 33
b = 200

if b > a:
  pass
Output:- 
```

### Ques. What is Lambda/Anonymous Function?
* A lambda function is a small anonymous function.
* In Python, an anonymous function is a function that is defined without a name.
* While normal functions are defined using the __def__ keyword in Python, anonymous functions are defined using the __lambda__ keyword.
```python
def add(a,b):
print(a+b)
add(5,10)

# Using Lambda function
x = lambda a: a + 10
print(x(5))

Output:- 15
```
	
### Ques:- What is Python JSON?
 * JSON is a syntax for storing and exchanging data.
 * JSON is text, written with JavaScript object notation.
 * Python has a built-in package called json, which can be used to work with JSON data.
 
 __Convert from JSON to Python__<br>If you have a JSON string, you can parse it by using the __json.loads()__ method.
 
 ```python
import json

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
# the result is a Python dictionary:
print(y["age"])
 
Output:- 30
 ```
__Convert from Python to JSON__<br>If you have a Python object, you can convert it into a JSON string by using the __json.dumps()__ method.
 ```python
 import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

Output:- {"name": "John", "age": 30, "city": "New York"}
```

### Decorators
* Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it.
* A decorator function is a function that accepts a function as parameter and return a function(decorator ek function hai jo as a argument leta bhi function hai and return bhi function karta hai).
```python
def decor(fun):
    def inner():
        print('befor inhance')
        fun()
        print('after inhance')
    return inner
    
def num():
    print('hello mohit')

result = decor(num)
result()

# Example2:- 
def decor(fun1):
    def inner():
        print('befor inhance')
        fun1()
        print('after inhance')
    return inner
    
@decor   
def num():
    print('hello mohit')
    
num()


Output:-
befor inhance
hello mohit
after inhance
-------------------------------------------------------------------------------------------------------------
def num_decor(num):
    def inner():
        a = num()
        add = a + 5
        return add
    return inner
    
@num_decor
def num():
    return 10

print(num())

# Example:-
def num_decor(num):
    def inner():
        a = num()
        add = a + 5
        return add
    return inner
def num():
    return 10

result = num_decor(num)
print(result())


Output:- 15
```


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


	
	
	
### Python Access Modifiers
```python
#defining class Student
class Student:
    #constructor is defined
    def __init__(self, name, age, salary):
        self.age = age             # public Attribute
        self._name = name          # protected Attribute 
        self.__salary = salary     # private Attribute

    def _funName(self):            # protected method
        pass
 
    def __funName(self):           # private method
        pass

# object creation
obj = Student('Mohit',53434)


```

##### Public Access Modifier
By default, all the variables and member functions of a class are public in a python program.
```python
class Employee:
    # constructor
    def __init__(self, name, sal):
        self.name = name;
        self.sal = sal;
obj = Employee('mohit',555)
print(obj.name)
print(obj.sal)

Output:- 
Mohit
555
```

##### protected Access Modifier
adding a prefix _(single underscore) to a variable name makes it protected.
```python
class Employee:
    # constructor
    def __init__(self, name, sal):
        self._name = name;   # protected attribute 
        self._sal = sal;     # protected attribute

obj = Employee('mohit',15)
print(obj._name)

Output:-
Mohit

# Example2:-
class Employee:
    # constructor
    def __init__(self, name, sal):
        self._name = name;   # protected attribute 
        self._sal = sal;     # protected attribute
 
class HR(Employee):
    def task(self):
        print ("We manage Employees")
        

hrEmp = HR("Captain", 10000);
print(hrEmp._sal)
print(hrEmp.task())

Output:-
10000
We manage Employees
```

##### private Access Modifier
While the addition of prefix __(double underscore) results in a member variable or function becoming private.
```python
class Person:
    def __init__(self, name, age, height):
        self.name     = name   # public
        self._age     = age    # protected
        self.__height = height # private

p1 = Person("John", 20, 170)

print(p1.name)        # public: can be accessed
print(p1._age)        # protected: can be accessed but not advised
# print(p1.__height)  # private: will give AttributeError
```
	
	
	
++++++++++++++++++
 <!DOCTYPE html>
<html lang="en">
   <head>
      <title>Python Interview Questions</title>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
      <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
      <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
      <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
      <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"></script>
   </head>
   <style type="text/css">
      .code_script{
      background: #ffffff; overflow: auto; width: auto; border: solid orange; border-width: .1em .1em .1em .8em; padding: .2em .6em;
      }
      .code_script_ans{
      background: #ffffff; overflow: auto; width: auto; border: solid green; border-width: .1em .1em .1em .8em; padding: .2em .6em;
      }
      .code{
      border: 0.1rem solid #cdd5e4;
      background-color: #f5f8ff;
      padding: 0.5rem 1rem;
      }
      .accordion-item {
      background-color: #f9f9f9;
      margin-bottom: 10px;
      position: relative;
      border-radius: 40px;
      overflow: hidden;
      }
   </style>
   <body>
      <div class="container">
         <div class="m-4">
            <div class="accordion" id="myAccordion">
               

               <div class="accordion-item">
                  <h2 class="accordion-header" id="headingTwo">
                     <button type="button" class="accordion-button collapsed" data-bs-toggle="collapse" data-bs-target="#Features"><strong>Ques. </strong> What is Python Features?</button>
                  </h2>
                  <div id="Features" class="accordion-collapse collapse" data-bs-parent="#myAccordion">
                     <div class="card-body">
                        <p><strong>Easy:- </strong>Python is very easy to learn and understand; any beginner can learn Python easily. When writing code in Python, you need fewer lines of code compared to languages like Java.</p>
                        <p><strong>Interpreted:- </strong>It is interpreted(executed) line by line. This makes it easy to test and debug.</p>
                        <p><strong>Object-Oriented:- </strong>The Python programming language supports classes and objects and hence it is object-oriented.</p>
                        <p><strong>Free and Open Source:- </strong>The language and its source code are available to the public for free; there is no need to buy a costly license.</p>
                        <p><strong>Portable:- </strong>Since Python is open-source, you can run it on Windows, Mac, Linux or any other platform. Your programs will work without any need to change it for every machine.</p>
                        <p><strong>GUI Programming:- </strong>You can use it to develop a GUI (Graphical User Interface). One way to do this is through Tkinter.</p>
                        <p><strong>Large Python Library:- </strong>Python provides you with a large standard library.</p>
                     </div>
                  </div>
               </div>
               
			   
			    <div class="accordion-item">
                  <h2 class="accordion-header" id="headingTwo">
                     <button type="button" class="accordion-button collapsed" data-bs-toggle="collapse" data-bs-target="#Comments"><strong>Ques. </strong>  Python Comments?</button>
                  </h2>
                  <div id="Comments" class="accordion-collapse collapse" data-bs-parent="#myAccordion">
                     <div class="card-body">
                        <p>single Line Comments</p>
						<pre class="code"><code>
#This is a comment
print("Hello, World!")

print("Hello, World!") #This is a comment
</pre></code>
						<p>Multi Line Comments(OR)Docstring</p>
							<pre class="code"><code>
"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")
</pre></code>
                      
                     </div>
                  </div>
               </div>
			   
			   
			   	<div class="accordion-item">
                  <h2 class="accordion-header" id="headingTwo">
                     <button type="button" class="accordion-button collapsed" data-bs-toggle="collapse" data-bs-target="#Variables"><strong>Ques. </strong>  Python Variables?</button>
                  </h2>
                  <div id="Variables" class="accordion-collapse collapse" data-bs-parent="#myAccordion">
                     <div class="card-body">
					 <ul>
						<li>A variable name must start with a letter or the underscore character</li>
						<li>A variable name cannot start with a number</li>
						<li>A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )</li>
						<li>Variable names are case-sensitive (age, Age and AGE are three different variables)</li>
					 </ul>
                      
						<pre class="code"><code>
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
</pre></code>
						<strong>Assign Value to Multiple Variables</strong>
							<pre class="code"><code>
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

output:- 
Orange
Banana
Cherry
</pre></code>
                      
                     </div>
                  </div>
               </div>
			   
			   		    <div class="accordion-item">
                  <h2 class="accordion-header" id="headingTwo">
                     <button type="button" class="accordion-button collapsed" data-bs-toggle="collapse" data-bs-target="#global_variables"><strong>Ques. </strong>  Global Variables?</button>
                  </h2>
                  <div id="global_variables" class="accordion-collapse collapse" data-bs-parent="#myAccordion">
                     <div class="card-body">
					 <ul>
						<li>Variables that are created outside of a function.</li>
						<li>Global variables can be used by everyone, both inside of functions and outside. </li>						
					 </ul>
                      
						<pre class="code"><code>
x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)
myfunc()
print("Python is " + x)

OutPut:- 
Python is fantastic
Python is awesome
</pre></code>
                      
                     </div>
                  </div>
               </div>
			   
			   
			    <div class="accordion-item">
                  <h2 class="accordion-header" id="headingTwo">
                     <button type="button" class="accordion-button collapsed" data-bs-toggle="collapse" data-bs-target="#global_keyword"><strong>Ques. </strong>Global Keyword?</button>
                  </h2>
                  <div id="global_keyword" class="accordion-collapse collapse" data-bs-parent="#myAccordion">
                     <div class="card-body">
					 <p>In Python, global keyword allows you to modify the variable outside of the current scope. It is used to create a global variable and make changes to the variable in a local context.</p>
					 <strong>Rules of global Keyword</strong>
					 <ul>
						<li>When we create a variable inside a function, it is local by default.</li>
						<li>When we define a variable outside of a function, it is global by default. You don't have to use global keyword.</li>
						<li>We use global keyword to read and write a global variable inside a function.</li>
					 </ul>


					 <ul>
						<li>Variables that are created outside of a function.</li>
						<li>Global variables can be used by everyone, both inside of functions and outside. </li>						
					 </ul>
                      
						<pre class="code"><code>
x = "awesome"
def myfunc():
    global x
    x = "fantastic"
myfunc()
print("Python is " + x)

Output:-
Python is fantastic
</pre></code>
                      
                     </div>
                  </div>
               </div>
			   
			   
			   
               <div class="accordion-item">
                  <h2 class="accordion-header" id="headingTwo">
                     <button type="button" class="accordion-button collapsed" data-bs-toggle="collapse" data-bs-target="#PEP"><strong>Ques. </strong> What is PEP 8?</button>
                  </h2>
                  <div id="PEP" class="accordion-collapse collapse" data-bs-parent="#myAccordion">
                     <div class="card-body">
                        <p>PEP stands for Python Enhancement Proposal. It is a set of rules that specify how to format Python code for maximum readability.</p>
                     </div>
                  </div>
               </div>
			    <div class="accordion-item">
                  <h2 class="accordion-header" id="headingTwo">
                     <button type="button" class="accordion-button collapsed" data-bs-toggle="collapse" data-bs-target="#data_types"><strong>Ques. </strong> What are the common built-in data types in Python?</button>
                  </h2>
                  <div id="data_types" class="accordion-collapse collapse" data-bs-parent="#myAccordion">
                     <div class="card-body">
                        <p>Python has the following data types built-in by default, in these categories:</p>
						<ul>
						<p>1. Numbers</p>
                     </div>
                  </div>
               </div>
			   
			   
               <div class="accordion-item">
                  <h2 class="accordion-header" id="headingTwo">
                     <button type="button" class="accordion-button collapsed" data-bs-toggle="collapse" data-bs-target="#operator"><strong>Ques. </strong> What is the operator?</button>
                  </h2>
                  <div id="operator" class="accordion-collapse collapse" data-bs-parent="#myAccordion">
                     <div class="card-body">
                        <p>Python language supports the following types of operators.</p>
                        <ul>
                           <li>Arithmetic Operators</li>
                           <li>Comparison (Relational) Operators.</li>
                           <li>Assignment Operators</li>
                           <li>Logical Operators</li>
                           <li>Bitwise Operators</li>
                           <li>Membership Operators</li>
                           <li>Identity Operators</li>
                        </ul>
                        <strong>Arithmetic Operators</strong>
                        <table class="table table-striped">
                           <thead>
                              <tr>
                                 <th scope="col">Operators</th>
                                 <th scope="col">Descrption</th>
                                 <th scope="col">Result</th>
                              </tr>
                           </thead>
                           <tbody>
                              <tr>
                                 <td>Addition(+)</td>
                                 <td>Adds the values on either side of the operator.</td>
                                 <td>3+4=7</td>
                              </tr>
                              <tr>
                                 <td>Subtraction(-)</td>
                                 <td>Subtracts the value on the right from the one on the left.</td>
                                 <td>3+4=-1</td>
                              </tr>
                              <tr>
                                 <td>Multiplication(*)</td>
                                 <td>Multiplies the values on either side of the operator.</td>
                                 <td>3*4=12</td>
                              </tr>
                              <tr>
                                 <td>Division(/)</td>
                                 <td>Divides the value on the left by the one on the right. Notice that division results in a floating-point value.</td>
                                 <td>3/4=0.75</td>
                              </tr>
                              <tr>
                                 <td>Exponentiation(**)</td>
                                 <td>Raises the first number to the power of the second.</td>
                                 <td>3**4=81</td>
                              </tr>
                              <tr>
                                 <td>Floor Division(//)</td>
                                 <td>Divides and returns the integer value of the quotient. It dumps the digits after the decimal.</td>
                                 <td>10//3=3</td>
                              </tr>
                              <tr>
                                 <td> Modulus(%)</td>
                                 <td>Divides and returns the value of the remainder.</td>
                                 <td>3%4=3</td>
                              </tr>
                           </tbody>
                        </table>
                        <strong>Comparison(Relational) Operators</strong>
                        <table class="table table-striped">
                           <thead>
                              <tr>
                                 <th scope="col">Operators</th>
                                 <th scope="col">Descrption</th>
                                 <th scope="col">Result</th>
                              </tr>
                           </thead>
                           <tbody>
                              <tr>
                                 <td>Less than(<)</td>
                                 <td>This operator checks if the value on the left of the operator is lesser than the one on the right.</td>
                                 <td>3<4=True</td>
                              </tr>
                              <tr>
                                 <td>Greater than(>)</td>
                                 <td>It checks if the value on the left of the operator is greater than the one on the right.</td>
                                 <td>3>4=False</td>
                              </tr>
                              <tr>
                                 <td>Less than or equal to(<=)</td>
                                 <td>It checks if the value on the left of the operator is lesser than or equal to the one on the right.</td>
                                 <td>7<=7 = True</td>
                              </tr>
                              <tr>
                                 <td> Greater than or equal to(>=)</td>
                                 <td>It checks if the value on the left of the operator is greater than or equal to the one on the right.</td>
                                 <td>0>=0  = True</td>
                              </tr>
                              <tr>
                                 <td>Equal to(= =)</td>
                                 <td>This operator checks if the value on the left of the operator is equal to the one on the right.(1 is equal to the Boolean value True, but 2 isn’t. Also, 0 is equal to False.)</td>
                                 <td>
                                    3==3.0 = True<br>
                                    <hr>
                                    1==True = True<br>
                                    <hr>
                                    7==True = False<br>
                                    <hr>
                                    0==False = True<br>
                                    <hr>
                                    0.5==True = False
                                 </td>
                              </tr>
                              <tr>
                                 <td>Not equal to(!=)</td>
                                 <td>It checks if the value on the left of the operator is not equal to the one on the right.</td>
                                 <td>1!=1.0 = False</td>
                           </tbody>
                        </table>
                        <strong>Assignment Operators</strong>
                        <table class="table table-striped">
                           <thead>
                              <tr>
                                 <th scope="col">Operators</th>
                                 <th scope="col">Descrption</th>
                                 <th scope="col">Result</th>
                              </tr>
                           </thead>
                           <tbody>
                              <tr>
                                 <td>Assign(=)</td>
                                 <td>Assigns a value to the expression on the left. Notice that = = is used for comparing, but = is used for assigning.</td>
                                 <td>>>> a=7<br>
                                    >>> print(a)<br> //output:- 7
                                 </td>
                              </tr>
                              <tr>
                                 <td>Add and Assign(+=)</td>
                                 <td>Adds the values on either side and assigns it to the expression on the left. a+=10 is the same as a=a+10.</td>
                                 <td>>>> a+=2<br>
                                    >>> print(a)<br> //output:- 9
                                 </td>
                              </tr>
                              <tr>
                                 <td>Divide and Assign(/=)</td>
                                 <td>Divides the value on the left by the one on the right. Then it assigns it to the expression on the left.</td>
                                 <td>>>> a/=7<br>
                                    >>> print(a)<br> //output:- 1.0
                                 </td>
                              </tr>
                              <tr>
                                 <td>Multiply and Assign(*=)</td>
                                 <td>Multiplies the values on either sides. Then it assigns it to the expression on the left.</td>
                                 <td>>>> a*=8<br>
                                    >>> print(a)<br> // 8.0
                                 </td>
                              </tr>
                              <tr>
                                 <td>Modulus and Assign(%=)</td>
                                 <td>Performs modulus on the values on either side. Then it assigns it to the expression on the left.</td>
                                 <td>>>> a%=3<br>
                                    >>> print(a)<br> //output:- 2.0
                                 </td>
                              </tr>
                              <tr>
                                 <td>Exponent and Assign(**=)</td>
                                 <td>Performs exponentiation on the values on either side. Then assigns it to the expression on the left.</td>
                                 <td>>>> a**=5<br>
                                    >>> print(a)<br> //output:- 32.0
                                 </td>
                              </tr>
                              <tr>
                                 <td>Floor-Divide and Assign(//=)</td>
                                 <td>Performs floor-division on the values on either side. Then assigns it to the expression on the left.</td>
                                 <td>>>> a//=3 <br>
                                    >>> print(a)<br> //output:- 10.0
                                 </td>
                              </tr>
                           </tbody>
                        </table>
                        <strong>Bitwise Operators</strong>
                        <table class="table table-striped">
                           <thead>
                              <tr>
                                 <th scope="col">Operators</th>
                                 <th scope="col">Descrption</th>
                                 <th scope="col">Result</th>
                              </tr>
                           </thead>
                           <tbody>
                              <tr>
                                 <td>Binary AND(&) </td>
                                 <td>It performs bit by bit AND operation on the two values. Here, binary for 2 is 10, and that for 3 is 11. &-ing them results in 10, which is binary for 2.</td>
                                 <td>>>> 2&3<br>
                                    //output:- 2
                                 </td>
                              </tr>
                              <tr>
                                 <td>Binary OR(|)</td>
                                 <td>---</td>
                                 <td>----
                                 </td>
                              </tr>
                              <tr>
                                 <td>Binary XOR(^)</td>
                                 <td>---</td>
                                 <td>---
                                 </td>
                              </tr>
                              <tr>
                                 <td>Binary One’s Complement(~) </td>
                                 <td>---</td>
                                 <td>---
                                 </td>
                              </tr>
                              <tr>
                                 <td>Binary Left-Shift(<<)</td>
                                 <td>---</td>
                                 <td>---
                                 </td>
                              </tr>
                              <tr>
                                 <td>Binary Right-Shift(>>)</td>
                                 <td>--</td>
                                 <td>---</td>
                              </tr>
                           </tbody>
                        </table>
                     </div>
                  </div>
               </div>
			   
			   <div class="accordion-item">
                  <h2 class="accordion-header" id="headingTwo">
                     <button type="button" class="accordion-button collapsed" data-bs-toggle="collapse" data-bs-target="#data_types"><strong>Ques. </strong> What is Data Types?</button>
                  </h2>
                  <div id="data_types" class="accordion-collapse collapse" data-bs-parent="#myAccordion">
                     <div class="card-body">
					 <p>Python has the following data types built-in by default, in these categories:</p>
						<ul>
						<li>Numbers
							<ul>
								<li><b>int:-</b> int stores integers eg a=100, b=25, c=526, etc.</li>
								<li><b>long:-</b> long stores higher range of integers eg a=908090999L, b=-0x1990999L, etc.</li>
								<li><b>float:-</b> float stores floating-point numbers eg a=25.6, b=45.90, c=1.290, etc.</li>
								<li><b>complex:-</b> complex stores numbers eg a=3 + 4j, b=2 + 3j, c=complex(4,6), etc.</li>
							</ul>
						</li>
						<li>Sequence Types:
							<ul>
								<li><b>list:-</b> Mutable sequence used to store collection of items.</li>
								<li><b>tuple:-</b> Immutable sequence used to store collection of items.</li>
								<li><b>range:-</b> Represents an immutable sequence of numbers generated during execution.</li>
								<li><b>str:-</b> Immutable sequence of Unicode code points to store textual data.</li>
							</ul>
						</li>
						<li>Mapping Types:
							<ul>
								<li><b>dict:-</b> Stores comma-separated list of key: value pairs.</li>
							</ul>
						</li>
						<li>Set Types:
							<ul>
								<li><b>set:-</b>-----</li>
								<li><b>frozenset:-</b>-----</li>
							</ul>
						</li>
						<li>Boolean Type:
							<ul>
								<li><b>bool:-</b>-----</li>
							</ul>
						</li>
						<li>Binary Types:
							<ul>
								<li><b>bytes:-</b>-----</li>
								<li><b>bytearray:-</b>-----</li>
								<li><b>memoryview:-</b>-----</li>
							</ul>
						</li>		
						</ul>
                     </div>
                  </div>
               </div>
			   
			   
			   	<div class="accordion-item">
                  <h2 class="accordion-header" id="headingTwo">
                     <button type="button" class="accordion-button collapsed" data-bs-toggle="collapse" data-bs-target="#pass"><strong>Ques. </strong> What is pass in Python?</button>
                  </h2>
                  <div id="pass" class="accordion-collapse collapse" data-bs-parent="#myAccordion">
                     <div class="card-body">
					 <p>The pass keyword represents a null operation in Python.<br> Without the pass statement in the following code, we may run into some errors during code execution.</p>
					 <pre class="code"><code>
def myEmptyFunc():
   # do nothing
   pass
myEmptyFunc()    # nothing happens
## Without the pass keyword
# File "<stdin>", line 3
# IndentationError: expected an indented block
					</code></pre>	
                     </div>
                  </div>
               </div>
			   
			   <div class="accordion-item">
                  <h2 class="accordion-header" id="headingTwo">
                     <button type="button" class="accordion-button collapsed" data-bs-toggle="collapse" data-bs-target="#self"><strong>Ques. </strong> What is the use of self in Python?</button>
                  </h2>
                  <div id="self" class="accordion-collapse collapse" data-bs-parent="#myAccordion">
                     <div class="card-body">
					 <p>Self is used to represent the instance of the class. With this keyword, you can access the attributes and methods of the class in python. It binds the attributes with the given arguments. self is used in different places and often thought to be a keyword. But unlike in C++, self is not a keyword in Python.</p>
                     </div>
                  </div>
               </div>
			   
			   	<div class="accordion-item">
                  <h2 class="accordion-header" id="headingTwo">
                     <button type="button" class="accordion-button collapsed" data-bs-toggle="collapse" data-bs-target="#__init__"><strong>Ques. </strong> What is __init__?</button>
                  </h2>
                  <div id="__init__" class="accordion-collapse collapse" data-bs-parent="#myAccordion">
                     <div class="card-body">
					 <p>__init__ is a contructor method in Python and is automatically called to allocate memory when a new object/instance is created. All classes have a __init__ method associated with them. It helps in distinguishing methods and attributes of a class from local variables.</p>
		<pre class="code"><code>			 
class Student:
   def __init__(self, fname, lname, age, section):
       self.firstname = fname
       self.lastname = lname
       self.age = age
       self.section = section
# creating a new object
stu1 = Student("Sara", "Ansh", 22, "A2")
</code></pre>
                     </div>
                  </div>
               </div>
			   
			   <div class="accordion-item">
                  <h2 class="accordion-header" id="headingTwo">
                     <button type="button" class="accordion-button collapsed" data-bs-toggle="collapse" data-bs-target="#break_continue_pass"><strong>Ques. </strong> What is break, continue and pass in Python?</button>
                  </h2>
                  <div id="break_continue_pass" class="accordion-collapse collapse" data-bs-parent="#myAccordion">
                     <div class="card-body">
					 <ul>
						<li><b>Break:-</b> The break statement terminates the loop immediately and the control flows to the statement after the body of the loop.</li>
						<li><b>Continue:-</b> The continue statement terminates the current iteration of the statement, skips the rest of the code in the current iteration and the control flows to the next iteration of the loop.</li>
						<li><b>Pass:-</b> As explained above, the pass keyword in Python is generally used to fill up empty blocks and is similar to an empty statement represented by a semi-colon in languages such as Java, C++, Javascript, etc.</li>
					 </ul>
                     </div>
                  </div>
               </div>
			   
			   
			   
               <div class="accordion-item">
                  <h2 class="accordion-header" id="headingTwo">
                     <button type="button" class="accordion-button collapsed" data-bs-toggle="collapse" data-bs-target="#membership_operator"><strong>Ques. </strong> What is membership operator and identity operator?</button>
                  </h2>
                  <div id="membership_operator" class="accordion-collapse collapse" data-bs-parent="#myAccordion">
                     <div class="card-body">
                        <p><strong>Membership Operators</strong> These operators help validate whether a given element is present in or is a member of the given sequence of data. This sequence of data can be a list, string or a tuple</p>
                        <p>There are 2 types of Membership operater</p>
                        <ul>
                           <li>in Operator:</li>
                           <pre class="code"><code>
lst1 = ['Ajay', 'Bobby','Ashok', 'Vijay', 'Anil', 'Rahul','Alex', 'Christopher']
if 'Ajay' in lst1: 
    print('Name Ajay exists in lst1')
//output:- Name Ajay exists in lst1
</code></pre>
                           <pre class="code"><code>
stri = "I love mohit"
print("ve" in stri)
//output:- True
                           </code></pre>
                           <li>not in Operator:</li>
                           <pre class="code"><code>
lst1 = ['Ajay', 'Bobby','Ashok', 'Vijay', 'Anil', 'Rahul','Alex', 'Christopher']
  if 'Raghav' not in lst1: print ('Name Raghav does not exists in lst1')
//output:- Name Raghav exists in lst1
</code></pre>
                           <pre class="code"><code>
stri = "I love mohit"
print("ve" not in stri)
//output:- False
</code></pre>
                        </ul>
                        <p><strong>Identity Operators</strong> These operators help in determining whether a value belongs to a certain class or a certain type, i.e they help in determining the identity of the object. It is useful in finding out the data type a variable holds.</p>
                        <ul>
                           <li>is</li>
                           <pre class="code"><code>                        
a = 'London'
b = 'London'

if a is b: print ('a is b')
else: print ('a is not b')

if a is c: print('a is c')
else: print ('a is not c')   
//output:- 
a is b
a is not c
</code></pre>
                           <li>is not</li>
                        </ul>
                     </div>
                  </div>
               </div>
               
               </div>
               <div class="accordion-item">
                  <h2 class="accordion-header" id="headingOne">
                     <button type="button" class="accordion-button collapsed" data-bs-toggle="collapse" data-bs-target="#memory"><strong>Ques. </strong> How is memory managed in Python?</button>
                  </h2>
                  <div id="memory" class="accordion-collapse collapse" data-bs-parent="#myAccordion">
                     <div class="card-body">
                        <ul>
                           <li>Python also has an inbuilt garbage collector, which recycles all the unused memory and so that it can be made available to the heap space.</li>
                           <li>Memory management in python is managed by Python private heap space. All Python objects and data structures are located in a private heap. The programmer does not have access to this private heap. The python interpreter takes care of this instead.</li>
                           <li>The allocation of heap space for Python objects is done by Python’s memory manager. The core API gives access to some tools for the programmer to code.</li>
                        </ul>
                     </div>
                  </div>
               </div>
               <div class="accordion-item">
                  <h2 class="accordion-header" id="headingOne">
                     <button type="button" class="accordion-button collapsed" data-bs-toggle="collapse" data-bs-target="#typedlang"><strong>Ques. </strong> What is a dynamically typed language?</button>
                  </h2>
                  <div id="typedlang" class="accordion-collapse collapse" data-bs-parent="#myAccordion">
                     <div class="card-body">
                        <p>
                           Typing refers to type-checking in programming languages.                       
                        </p>
                        <p>Type-checking can be done at two stages -</p>
                        <ul>
                           <li><strong>Static -</strong> Data Types are checked before execution.</li>
                           <li><strong>Dynamic -</strong> Data Types are checked during execution.</li>
                        </ul>
                        <p>Python is an interpreted language, executes each statement line by line and thus type-checking is done on the fly, during execution. Hence, Python is a Dynamically Typed Language.</p>
                     </div>
                  </div>
               </div>
               <div class="accordion-item">
                  <h2 class="accordion-header" id="headingOne">
                     <button type="button" class="accordion-button collapsed" data-bs-toggle="collapse" data-bs-target="#interpretedlang"><strong>Ques. </strong> What is an Interpreted language?</button>
                  </h2>
                  <div id="interpretedlang" class="accordion-collapse collapse" data-bs-parent="#myAccordion">
                     <div class="card-body">
                        <p>An Interpreted language executes its statements line by line. Languages such as Python, Javascript, R, PHP, and Ruby are prime examples of Interpreted languages.</p>
                     </div>
                  </div>
               </div>
              
              
               <div class="accordion-item">
                  <h2 class="accordion-header" id="headingOne">
                     <button type="button" class="accordion-button collapsed" data-bs-toggle="collapse" data-bs-target="#list_tuple"><strong>Ques. </strong> What is the difference between a list and a tuple?</button>                  
                  </h2>
                  <div id="list_tuple" class="accordion-collapse collapse" data-bs-parent="#myAccordion">
                     <div class="card-body">
                        <p>
                        <table class="table table-hover">
                           <thead>
                              <tr>
                                 <th scope="col">#</th>
                                 <th scope="col">List</th>
                                 <th scope="col">Tuple</th>
                              </tr>
                           </thead>
                           <tbody>
                              <tr>
                                 <th scope="row">1</th>
                                 <td>A list consists of <b>mutable</b> objects. (Objects which can be changed after creation)</td>
                                 <td>A tuple consists of <b>immutable</b> objects. (Objects which cannot change after creation)</td>
                              </tr>
                              <tr>
                                 <th scope="row">2</th>
                                 <td>List has a large memory.</td>
                                 <td>Tuple has a small memory.</td>
                              </tr>
                              <tr>
                                 <th scope="row">3</th>
                                 <td >List is stored in two blocks of memory (One is fixed sized and the other is variable sized for storing data)</td>
                                 <td>Tuple is stored in a single block of memory.</td>
                              </tr>
                              <tr>
                                 <th scope="row">4</th>
                                 <td >Creating a list is slower because two memory blocks need to be accessed.</td>
                                 <td>Creating a tuple is faster than creating a list.</td>
                              </tr>
                              <tr>
                                 <th scope="row">5</th>
                                 <td >An element in a list can be removed or replaced.</td>
                                 <td>An element in a tuple cannot be removed or replaced.</td>
                              </tr>
                              <tr>
                                 <th scope="row">6</th>
                                 <td>A list has data stored in  square brackets [] brackets. For example, [1,2,3]</td>
                                 <td>A tuple has data stored in parantheses () brackets. For example, (1,2,3)</td>
                              </tr>
                           </tbody>
                        </table>
                        </p>
                     </div>
                  </div>
               </div>
               <div class="accordion-item">
                  <h2 class="accordion-header" id="headingOne">
                     <button type="button" class="accordion-button collapsed" data-bs-toggle="collapse" data-bs-target="#list_into_tuple"><strong>Ques. </strong> How would you convert a list into a tuple?</button>
                  </h2>
                  <div id="list_into_tuple" class="accordion-collapse collapse" data-bs-parent="#myAccordion">
                     <div class="card-body">
                        <p><strong>1. Using tuple() builtin function</strong><br>
                        <div style="background: #ffffff; overflow: auto; width: auto; border: solid orange; border-width: .1em .1em .1em .8em; padding: .2em .6em;">
                           <pre style="margin: 0; line-height: 125%;">sample_list <span style="color: #333333;">=</span> [<span style="background-color: #fff0f0;">'Compile'</span>, <span style="background-color: #fff0f0;">'With'</span>, <span style="background-color: #fff0f0;">'Favtutor'</span>]

<span style="color: #888888;">#convert list into tuple</span>
tuple1 <span style="color: #333333;">=</span> <span style="color: #007020;">tuple</span>(sample_list)

<span style="color: #007020;">print</span>(tuple1)
<span style="color: #007020;">print</span>(<span style="color: #007020;">type</span>(tuple1))
</pre>
                        </div>
                        <strong>Output:-</strong><br>
                        <div style="background: #ffffff; overflow: auto; width: auto; border: solid green; border-width: .1em .1em .1em .8em; padding: .2em .6em;">
                           <pre style="margin: 0; line-height: 125%;"><span style="color: #888888;">('Compile', 'With', 'Favtutor')</span>
<span style="color: #888888;">&lt;class 'tuple'&gt;</span>
</pre>
                        </div>
                        <strong>2.  Using loop inside the tuple</strong>
                        <div style="background: #ffffff; overflow: auto; width: auto; border: solid orange; border-width: .1em .1em .1em .8em; padding: .2em .6em;">
                           <pre style="margin: 0; line-height: 125%;">sample_list <span style="color: #333333;">=</span> [<span style="background-color: #fff0f0;">'Compile'</span>, <span style="background-color: #fff0f0;">'With'</span>, <span style="background-color: #fff0f0;">'Favtutor'</span>]
tuple1 <span style="color: #333333;">=</span> <span style="color: #007020;">tuple</span>(i <span style="color: #008800; font-weight: bold;">for</span> i <span style="color: #000000; font-weight: bold;">in</span> sample_list)
<span style="color: #007020;">print</span>(tuple1)
</pre>
                        </div>
                        <strong>Output:-</strong>
                        <div style="background: #ffffff; overflow: auto; width: auto; border: solid green; border-width: .1em .1em .1em .8em; padding: .2em .6em;">
                           <pre style="margin: 0; line-height: 125%;"><span style="color: #888888;">('Compile', 'With', 'Favtutor')</span></pre>
                        </div>
                        <strong>3. Unpack list inside the parenthesis</strong>
                        <div style="background: #ffffff; overflow: auto; width: auto; border: solid orange; border-width: .1em .1em .1em .8em; padding: .2em .6em;">
                           <pre style="margin: 0; line-height: 125%;">sample_list <span style="color: #333333;">=</span> [<span style="background-color: #fff0f0;">'Compile'</span>, <span style="background-color: #fff0f0;">'With'</span>, <span style="background-color: #fff0f0;">'Favtutor'</span>]

<span style="color: #888888;">#unpack list items and form tuple</span>
tuple1 <span style="color: #333333;">=</span> (<span style="color: #333333;">*</span>sample_list,)

<span style="color: #007020;">print</span>(tuple1)
<span style="color: #007020;">print</span>(<span style="color: #007020;">type</span>(tuple1))
</pre>
                        </div>
                        <strong>Output:- </strong>
                        <div style="background: #ffffff; overflow: auto; width: auto; border: solid green; border-width: .1em .1em .1em .8em; padding: .2em .6em;">
                           <pre style="margin: 0; line-height: 125%;"><span style="color: #888888;">('Compile', 'With', 'Favtutor')</span>
<span style="color: #888888;">&lt;class 'tuple'&gt;</span>
</pre>
                        </div>
                        </p>
                     </div>
                  </div>
               </div>
               <div class="accordion-item">
                  <h2 class="accordion-header" id="headingOne">
                     <button type="button" class="accordion-button collapsed" data-bs-toggle="collapse" data-bs-target="#list_array"><strong>Ques. </strong> What is the difference between an array and a list?</button>                  
                  </h2>
                  <div id="list_array" class="accordion-collapse collapse" data-bs-parent="#myAccordion">
                     <div class="card-body">
                        <p>
                        <table class="table table-hover">
                           <thead>
                              <tr>
                                 <th scope="col">#</th>
                                 <th scope="col">List</th>
                                 <th scope="col">Array</th>
                              </tr>
                           </thead>
                           <tbody>
                              <tr>
                                 <th scope="row">1</th>
                                 <td>It Contains elements of different data types</td>
                                 <td>It Contains elements of same data types</td>
                              </tr>
                              <tr>
                                 <th scope="row">2</th>
                                 <td>Cannot handle arithmetic operations</td>
                                 <td>Can handle arithmetic operations</td>
                              </tr>
                              <tr>
                                 <th scope="row">3</th>
                                 <td>We can print the entire list without the help of an explicit loop</td>
                                 <td>To print or access array elements, we will require an explicit loop</td>
                              </tr>
                              <tr>
                                 <th scope="row">4</th>
                                 <td>It consumes a large memory.</td>
                                 <td>It is a more compact in memory size comparatively list.</td>
                              </tr>
                              <tr>
                                 <th scope="row">5</th>
                                 <td>---------------</td>
                                 <td>------------------</td>
                              </tr>
                              <tr>
                                 <th scope="row">6</th>
                                 <td>-----------</td>
                                 <td>-----------------</td>
                              </tr>
                           </tbody>
                        </table>
                        </p>
                     </div>
                  </div>
               </div>
               <div class="accordion-item">
                  <h2 class="accordion-header" id="headingOne">
                     <button type="button" class="accordion-button collapsed" data-bs-toggle="collapse" data-bs-target="#list_to_array"><strong>Ques. </strong> How would you convert a list to an array?</button>                  
                  </h2>
                  <div id="list_to_array" class="accordion-collapse collapse" data-bs-parent="#myAccordion">
                     <div class="card-body">
                        <p>Python list is a linear data structure that can hold heterogeneous elements. Python does not have a built-in array data type. If you want to create an array in Python, then use the numpy library.</p>
                        <p>To <em>install numpy</em> in your system, type the following command.</p>
                        <p>python3 -m pip install numpy</p>
                        <p><strong>1. Using numpy.array()</strong>
                        <div class="code_script">
                           <pre>import numpy as np

elon_list = [11, 21, 19, 18, 29]
elon_array = np.array(elon_list)

print(elon_array)
print(type(elon_array))</pre>
                        </div>
                        <strong>Output:- </strong>
                        <div class="code_script_ans">
                           <pre>[11 21 19 18 29]
&lt;class 'numpy.ndarray'&gt;</pre>
                        </div>
                        <strong>2. Using numpy.asarray()</strong>
                        <div class="code_script">
                           <pre>import numpy as np

elon_list = [11, 21, 19, 18, 29]
elon_array = np.asarray(elon_list)

print(elon_array)
print(type(elon_array))</pre>
                        </div>
                        <strong>Output:- </strong>
                        <div class="code_script_ans">
                           <pre>
   [11 21 19 18 29]
&lt;class 'numpy.ndarray'&gt;
</pre>
                        </div>
                        </p>
                     </div>
                  </div>
               </div>
           

              
               <div class="accordion-item">
                  <h2 class="accordion-header" id="headingOne">
                     <button type="button" class="accordion-button collapsed" data-bs-toggle="collapse" data-bs-target="#lambda"><strong>Ques. </strong> Python - Lambda Function?</button>                  
                  </h2>
                  <div id="lambda" class="accordion-collapse collapse" data-bs-parent="#myAccordion">
                     <div class="card-body">
                        <p>
                        <ul>
                           <li>A lambda function is a small anonymous function.</li>
                           <li>In Python, an anonymous function is a function that is defined without a name.</li>
                           <li>While normal functions are defined using the def keyword in Python, anonymous functions are defined using the lambda keyword.</li>
                           <li>Hence, anonymous functions are also called lambda functions.</li>
                        </ul>
                        <strong>Syntex:- </strong>lambda arguments: expression
                        <div class="code_script">
                           <pre>
def add(a,b):
   print(a+b)
add(5,10)
===Using Lambda function
x = lambda a: a + 10
print(x(5))
</pre>
                        </div>
                        <br>
                        <div class="code_script_ans">
                           <pre>
Output:- 15
                           </pre>
                        </div>
                        <h5>You can use lambda function in <em>filter()</em></h5>
                        <p>filter() function is used to filter a given iterable (list like object) using another function that defines the filtering logic.</p>
                        <p><strong>Syntex:-</strong>filter(object, iterable)</p>
                        <p>The object here should be a lambda function which returns a boolean value. </p>
                        <div class="code_script">
                           <pre>
mylist = [2,3,4,5,6,7,8,9,10]
list_new  = list(filter(lambda x : (x%2==0), mylist))
print(list_new)
</pre>
                        </div>
                        <br>
                        <div class="code_script_ans">
                           <pre>
Output:- [2, 4, 6, 8, 10]
                           </pre>
                        </div>
                        <h5>You can use lambda function in <em>map()</em></h5>
                        <p>map() function applies a given function to all the itmes in a list and returns the result. Similar to filter(), simply pass the lambda function and the list (or any iterable, like tuple) as arguments.</p>
                        <div class="code_script">
                           <pre>
mylist = [2,3,4,5,6,7,8,9,10]
list_new  = list(map(lambda x : x%2, mylist))
print(list_new)
</pre>
                        </div>
                        <br>
                        <div class="code_script_ans">
                           <pre>
Output:- [0, 1, 0, 1, 0, 1, 0, 1, 0]
                           </pre>
                        </div>
                        <h5>You can use lambda function in <em>reduce()</em>as well</h5>
                        <p>reduce() function performs a repetitive operation over the pairs of the elements in the list. Pass the lambda function and the list as arguments to the reduce() function. For using the reduce() function, you need to import reduce from <strong><em>functools</em></strong> librray.</p>
                        <div class="code_script">
                           <pre>
from functools import reduce
list1 = [1,2,3,4,5,6,7,8,9]
sum = reduce((lambda x,y: x+y), list1)
print(sum)
</pre>
                        </div>
                        <br>
                        <div class="code_script_ans">
                           <pre>
Output:- 45 //i.e 1+2, 1+2+3 , 1+2+3+4 and so on.
                           </pre>
                        </div>
                        <h5>How to use lambda function to manipulate a Dataframe</h5>
                        <p>You can also manipulate the columns of the dataframe using the lambda function. It’s a great candidate to use inside the apply method of a dataframe. I will be trying to add a new row in the dataframe in this section as example.</p>
                        <div class="code_script">
                           <pre>
import pandas as pd
df = pd.DataFrame([[1,2,3],[4,5,6]],columns = ['First','Second','Third'])
df['Forth']= df.apply(lambda row: row['First']*row['Second']* row['Third'], axis=1)
df
</pre>
                        </div>
                        <br>
                        <div class="code_script_ans">
                           <table class="dataframe" border="1">
                              <thead>
                                 <tr style="text-align:right">
                                    <th>&nbsp;</th>
                                    <th>First</th>
                                    <th>Second</th>
                                    <th>Third</th>
                                    <th>Forth</th>
                                 </tr>
                              </thead>
                              <tbody>
                                 <tr>
                                    <th>0</th>
                                    <td>1</td>
                                    <td>2</td>
                                    <td>3</td>
                                    <td>6</td>
                                 </tr>
                                 <tr>
                                    <th>1</th>
                                    <td>4</td>
                                    <td>5</td>
                                    <td>6</td>
                                    <td>120</td>
                                 </tr>
                              </tbody>
                           </table>
                        </div>
                        </p>
                     </div>
                  </div>
               </div>
	       
               <h1>OOPs Concepts</h1>
               <div class="accordion-item">
                  <h2 class="accordion-header" id="headingOne">
                     <button type="button" class="accordion-button collapsed" data-bs-toggle="collapse" data-bs-target="#Class"><strong>Ques. </strong> What is Class?</button>                  
                  </h2>
                  <div id="Class" class="accordion-collapse collapse" data-bs-parent="#myAccordion">
                     <div class="card-body">
                        <p>The class can be defined as a collection of objects. It is a logical entity that has some specific attributes and methods.<br>
                           <strong>For example:</strong> if you have an employee class, then it should contain an attribute and method, i.e. an email id, name, age, salary, etc.
                        </p>
                        <div>
                           <pre class="code">
class ClassName:     
  &lt;statement-1>     
            .     
            .      
  &lt;statement-N>
</pre>
                        </div>
                        </p>
                     </div>
                  </div>
               </div>
               <div class="accordion-item">
                  <h2 class="accordion-header" id="headingOne">
                     <button type="button" class="accordion-button collapsed" data-bs-toggle="collapse" data-bs-target="#Object"><strong>Ques. </strong> What is Object?</button>                  
                  </h2>
                  <div id="Object" class="accordion-collapse collapse" data-bs-parent="#myAccordion">
                     <div class="card-body">
                        <p>The object is an entity that has state and behavior. It may be any real-world object like the mouse, keyboard, chair, table, pen, etc.<br>
                           <strong>For example:</strong> if you have an employee class, then it should contain an attribute and method, i.e. an email id, name, age, salary, etc.
                        </p>
                        <div>
                           <pre class="code">
class car:  
    def __init__(self,modelname, year):  
        self.modelname = modelname  
        self.year = year  
    def display(self):  
        print(self.modelname,self.year)  
  
c1 = car("Toyota", 2016)  
c1.display()
//output:- Toyota 2016
</pre>
                        </div>
                        <p>Here, the <strong>self</strong> is used as a reference variable, which refers to the current class object. It is always the first argument in the function definition. However, using self is optional in the function call.</p>
                        <p>The <strong>self-parameter</strong> refers to the current instance of the class and accesses the class variables. We can use anything instead of self, but it must be the first parameter of any function which belongs to the class.</p>
                        <h3>Delete the Object</h3>
                        <p>We can delete the properties of the object or object itself by using the del keyword. Consider the following example.</p>
                        <pre class="code">
class Employee:  
  id = 10  
  name = "John"  
  def display(self):  
    print("ID: %d \nName: %s" % (self.id, self.name))  
      # Creating a emp instance of Employee class  
      emp = Employee()  
  
      # Deleting the property of object  
      del emp.id  

      # Deleting the object itself  
      del emp  
      emp.display()
</pre>
                     </div>
                  </div>
               </div>
			   
			               <div class="accordion-item">
                  <h2 class="accordion-header" id="headingOne">
                     <button type="button" class="accordion-button collapsed" data-bs-toggle="collapse" data-bs-target="#python_json"><strong>Ques. </strong> What is Python JSON?</button>                  
                  </h2>
                  <div id="python_json" class="accordion-collapse collapse" data-bs-parent="#myAccordion">
                     <div class="card-body">
                        <ul>
							<li>JSON is a syntax for storing and exchanging data.</li>
							<li>JSON is text, written with JavaScript object notation.</li>
							<li>Python has a built-in package called json, which can be used to work with JSON data.</li>
						</ul>
						#### Convert from JSON to Python
						<p>If you have a JSON string, you can parse it by using the __json.loads()__ method.</p>
                        <div>
                           <pre class="code">
import json

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
# the result is a Python dictionary:
print(y["age"])

//output:- 30
</pre>
                        </div>
						#### Convert from Python to JSON
						<p>If you have a Python object, you can convert it into a JSON string by using the __json.dumps()__ method.</p>
						
                        <div>
                        <pre class="code">
import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

//Output:- {"name": "John", "age": 30, "city": "New York"}
</pre>
                     </div>
                  </div>
               </div>
			   
			   
			   
               <div class="accordion-item">
                  <h2 class="accordion-header" id="headingOne">
                     <button type="button" class="accordion-button collapsed" data-bs-toggle="collapse" data-bs-target="#Method"><strong>Ques. </strong> What is Method?</button>                  
                  </h2>
                  <div id="Method" class="accordion-collapse collapse" data-bs-parent="#myAccordion">
                     <div class="card-body">
                        <p>The method is a function that is associated with an object. In Python, a method is not unique to class instances. Any object type can have methods.</p>
                     </div>
                  </div>
               </div>
               <div class="accordion-item">
                  <h2 class="accordion-header" id="headingOne">
                     <button type="button" class="accordion-button collapsed" data-bs-toggle="collapse" data-bs-target="#Inheritance"><strong>Ques. </strong> What is Inheritance?</button>                  
                  </h2>
                  <div id="Inheritance" class="accordion-collapse collapse" data-bs-parent="#myAccordion">
                     <div class="card-body">
                        <p>
                           <strong>Syntex:-</strong><br>
                        <pre class="code">
class class-name(parent class):  
    &lt;class-suite>  

class derive-class(&lt;base class 1>, &lt;base class 2>, ..... &lt;base class n>):  
    &lt;class - suite>  
  </pre>
                        </p>
                     </div>
                  </div>
               </div>
			   
				<div class="accordion-item">
                  <h2 class="accordion-header" id="headingOne">
                     <button type="button" class="accordion-button collapsed" data-bs-toggle="collapse" data-bs-target="#file_handling"><strong>Ques. </strong> What is File Handling?</button>                  
                  </h2>
                  <div id="file_handling" class="accordion-collapse collapse" data-bs-parent="#myAccordion">
                     <div class="card-body">
					 <p>The key function for working with files in Python is the <strong>open()</strong> function.<br>The open() function takes two parameters; filename, and mode.</p>
                        <p>Python has several functions for creating, reading, updating, and deleting files.</p>
						<p>Types Of File in Python</p>
						<ul>
							<li>Binary file</li>
								<ul>
									<li><b>Document files:</b> .pdf, .doc, .xls etc.</li>
									<li><b>Image files:</b> .png, .jpg, .gif, .bmp etc.</li>
									<li><b>Video files:</b> .mp4, .3gp, .mkv, .avi etc.</li>
									<li><b>Audio files:</b> .mp3, .wav, .mka, .aac etc.</li>
									<li><b>Database files:</b> .mdb, .accde, .frm, .sqlite etc.</li>
									<li><b>Archive files:</b> .zip, .rar, .iso, .7z etc.</li>
									<li><b>Executable files:</b> .exe, .dll, .class etc.</li>
								</ul>
							<li>Text file</li>
								<ul>
									<li><b>Web standards:</b>  html, XML, CSS, JSON etc.</li>
									<li><b>Source code:</b> c, app, js, py, java etc.</li>
									<li><b>Documents:</b> txt, tex, RTF etc.</li>
									<li><b>Tabular data:</b> csv, tsv etc</li>
									<li><b>Configuration:</b> ini, cfg, reg etc.</li>
								</ul>							
						</ul>
						
						<ul>
							<li>"r" - Read - Default value. Opens a file for reading, error if the file does not exist</li>
							<li>"a" - Append - Opens a file for appending, creates the file if it does not exist</li>
							<li>"w" - Write - Opens a file for writing, creates the file if it does not exist</li>
							<li>"x" - Create - Creates the specified file, returns an error if the file exists</li>
						</ul>
						syntex:-
						<pre class="code">
my_file = open(“C:/Documents/Python/test.txt”, “r”)
print(my_file.read(5))
</pre>
                     </div>
                  </div>
               </div>
			   
			   
			   
			   
			   
			   
            </div>
         </div>
      </div>
   </body>
</html>

f. What is repr()?
g. WAP to count from a string?
h. Write methods for the list.
i. List of zeros python without function or any method.
j. What are deep copy and shallow copy?
k. How to use deep copy?
l. Count occurrence of each number in list.
o. List_ = ['a', 'aa', 'aaa', 'ababa']. sort the list on the basis of length. 
p. Convert list element into string. 
q. Prime numbers program.
r. Print this Pattern (* * * ***)
s. Write a custom insert() function for list eg. def custom_insert (list, index, item).
t. Explain the join method.
w. Packing, unpacking in tuple?
x. What is reduce and filter? Examples
y. What is common between dictionary and set?
z. Sort in dictionary with key
aa. How do you add two dictionaries?
bb. Can we pass list or tuple as a key in dictionary?
cc. Unique dictionary from list.
dd. What is a decorator?
ee. What is property decorator?
ff. What is a generator?
gg. Iterator and iterable difference.
hh. Difference between generator and iterator in python.
ii. What is lazy evaluation in python?
jj. What is Monkey Patching in python?
kk. What is Magic method in python?
2. File Handling
a. What is pickling? Format of object stored in file?
b. Static file contains which type of file normally?
c. How can be file read in specific location?
d. How do you remove a file from a folder?
e. If user upload excel file check file format if it is valid or invalid.
f. What is context manager?
g. What is Garbage Collector?
h. Memory management in Python?
3. Object Oriented Programming
a. What is class and object?
b. Create a new class in oops?
c. What is constructor?
d. Why used constructor?
e. Advantage of constructor
f. What is the class method?
g. What is the difference between Static method and Class method?
h. Private variable and how we can access that?
i. Inheritance and types of inheritance.
j. Difference multilevel and multiple inheritance and drawback?
k. What is MRO?
l. What is  str?
4. Exception Handling
a. How can we handle errors in python ?
b. How many ways exception in python?
5. Multithreading
a. What is GIL?
6. Numpy
a. Tell me some python libraries .. Numpy
b. Convert a list into numpy

Local Scope
The Variables which are defined in the function are a local scope of the variable. These variables are defined in the function body.
Example:- 
def myfunc():
  x = 300
  print(x)

myfunc()

Output:- 300

Global Scope
The Variable which can be read from anywhere in the program is known as a global scope. These variables can be accessed inside and outside the function. 
x = 300

def myfunc():
  print(x)

myfunc()

print(x)

Output:- 300
300

NonLocal or Enclosing Scope
Built-in Scope
Global Keyword


Ques:- What are the common built-in data types in Python?
Python has the following data types built-in by default, in these categories:
<ul>
<li>Numbers
	<ul>
    	<li><b>int:-</b> int stores integers eg a=100, b=25, c=526, etc.</li>
        <li><b>long:-</b> long stores higher range of integers eg a=908090999L, b=-0x1990999L, etc.</li>
		<li><b>float:-</b> float stores floating-point numbers eg a=25.6, b=45.90, c=1.290, etc.</li>
		<li><b>complex:-</b> complex stores numbers eg a=3 + 4j, b=2 + 3j, c=complex(4,6), etc.</li>
    </ul>
</li>
<li>Sequence Types:
	<ul>
		<li><b>list:-</b> Mutable sequence used to store collection of items.</li>
		<li><b>tuple:-</b> Immutable sequence used to store collection of items.</li>
		<li><b>range:-</b> Represents an immutable sequence of numbers generated during execution.</li>
		<li><b>str:-</b> Immutable sequence of Unicode code points to store textual data.</li>
	</ul>
</li>
<li>Mapping Types:
	<ul>
		<li><b>dict:-</b> Stores comma-separated list of key: value pairs.</li>
	</ul>
</li>

</ul>


Check Prime Number
num = 19

Using Flag:- 

flag = False
# int(num/2)+1
if num >1 :
    for i in range(2, num):
        if(num%i) == 0:
            flag = True
            break
if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")
	
	
OutPut:- 3 is a prime number


Prime Number Print
==================
lower_value = int(input ("Please, Enter the Lowest Range Value: "))  
upper_value = int(input ("Please, Enter the Upper Range Value: "))  
print ("The Prime Numbers in the range are: ")
for i in range (lower_value, upper_value + 1):  
    if i > 1:  
        for j in range (2, i):
            if (i % j) == 0:  
                break  
        else:  
            print (i)  
			
Output:-
Please, Enter the Lowest Range Value: 1
Please, Enter the Upper Range Value: 20
The Prime Numbers in the range are: 
2
3
5
7
11
13
17
19







AbstractUser vs AbstractBaseUser
The default User model in Django uses a username to uniquely identify a user during authentication. If you'd rather use an email address, you'll need to create a custom User model by either subclassing AbstractUser or AbstractBaseUser.

Options:

AbstractUser: Use this option if you are happy with the existing fields on the User model and just want to remove the username field.
AbstractBaseUser: Use this option if you want to start from scratch by creating your own, completely new User model.




What is CRUD operations Django?
Django is a Python-based web framework that follows the MVT (Model View Template) pattern and allows you to quickly create web applications. It offers built-in class-based generic views for CRUD operations. CRUD in general means Creating, Retrieving, Updating and Deleting operations on a table in a database.

What is class based view in Django?
Class-based view is an alternative to function-based view. They do not replace function-based views, but have some distinct differences and advantages over function-based views.

What is generic views in Django?
Django generic views have been developed as shortcuts for common usage methods such as displaying object details.
They take some of the common methods found in view development and abstract them so that you can quickly write common views of data without writing too much code.

What is DetailView in Django?
Django DetailView should be used when you want to present detail of a single model instance. Its purpose is to use with only one object.



class Employee(models.Model):
	id = models.AutoField('Id', primary_key=True)
	
	first_name = models.CharField('First name', max_length=15, null = True)
	last_name = models.CharField('Last name', max_length=16, blank=True)
	email = models.EmailField(max_length = 255, unique=True, null = True)
	user_name   = models.CharField(max_length=50, unique=True, null = True, error_messages ={
                    "unique":"The User Name Field you entered is unique."
                    })
	dof = models.DateField('Birthday')
	
	
	gender = models.CharField('Gender', max_length=1)
	hire_date = models.DateField('hire date')

	class Meta:
		db_table = 'employees'

	def __str__(self):
		return "{} {}".formet(self.first_name, self.last_name)
		
		
		
		https://books.agiliq.com/projects/django-orm-cookbook/en/latest/null_vs_blank.html
		
		
		
		
title= models.CharField(max_length=300, unique=True)	


Deep Copy:- In deep copy any changes made to a copy of object do not reflect in the orginal object.
In case of shallow copy, a refrence of object 


