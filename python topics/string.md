### Ques. Python Strings?
* Once a string object has been created, it cannot be changed. “Modifying” that string creates a whole new object in memory.
* 'hello' is the same as "hello".

##### Assign String to a Variable
```python
a = "Hello"
print(a)

Output:- Hello
```

##### Multiline Strings
You can assign a multiline string to a variable by using three quotes:
```python
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

Output:-
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
```

##### Slicing Strings
```python
b = "Hello, World!" 

print(b[2:5])   # Slice from the start position and end position
Output:- llo

print(b[:5])    # Slice From the Start: Get the characters from the start to position (5 not included)
Output:- Hello

print(b[2:])    # Slice To the End: Get the characters from position 2, and all the way to the end.
Output:- llo, World!

print(b[-5:-2]) # Negative Indexing: Get the characters from position 2, and all the way to the end.
Output:- orl
```

##### Modify Strings
* The **replace()** method replaces a string with another string.
```python
a = "Hello, World!"
print(a.replace("H", "J"))

Output:- Jello, World!
```
* The **split()** method splits the string into substrings if it finds instances of the separator
```python
a = "Hello, World!"
b = a.split(",")

Output:- ['Hello', ' World!']
```
* Upper Case
```python
b = "Hello, World!"
print(a.upper())

Output:- HELLO, WORLD!
```
* Lower Case
```python
b = "Hello, World!"
print(a.lower())

Output:- hello, world!
```
* Remove Whitespace :- The **strip()** method removes any whitespace from the beginning or the end.
```python
b = "      Hello, World!     "
print(a.strip())

Output:- Hello, World!
``` 

##### String Concatenation
* To concatenate, or combine, two strings you can use the **plus(+)** operator.
```python
a = "Hello"
b = "World"
c = a + b
print(c)

Output:- HelloWorld 
```
* To add a space between them, add a " "
```python
a = "Hello"
b = "World"
c = a+" "+b

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
 
##### Ques. What is an f-string and how do you use it?
New in python 3.6, f-strings make string interpolation really easy. Using f-strings is similar to using format(). and F-strings are denoted by an f before the opening quote.
```python
name = 'Chris'
food = 'creme brulee'
print(f'Hello. My name is {name} and I like {food}.')

Output:- Hello. My name is Chris and I like creme brulee.
```


##### Escape Characters
* An escape character is a backslash \ followed by the character you want to insert.
```python
txt = "We are the so-called \"Vikings\" from the north."
print(txt) 

Output:- We are the so-called "Vikings" from the north.

# Single Quote
txt = 'It\'s alright.'
print(txt)  

Output:- It's alright.

# Backslash
txt = "This will insert one \\ (backslash)."
print(txt)   

Output:- This will insert one \ (backslash).

# New Line
txt = "Hello\nWorld!"
print(txt)    

Output:- 
Hello
World!

# Carriage Return
txt = "Hello\rWorld!"
print(txt)

Output:-
Hello
World!

# Tab
txt = "Hello\tWorld!"
print(txt)

Output:- Hello   World!

# Backspace
txt = "Hello \bWorld!"
print(txt)

Output:- HelloWorld!

# Octal value	
txt = "\110\145\154\154\157"
print(txt)

Output:- Hello

# Hex value
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) 

Output:- Hello
```


##### Ques. How would you confirm that 2 strings have the same identity?
The <b>is</b> operator returns True if 2 names point to the same location in memory.
```python
animals           = ['python','gopher']
more_animals      = animals

print(animals == more_animals) #=> True
print(animals is more_animals) #=> True
Output:-
True
True
-------------------------------------------------
animals           = ['python','gopher']
even_more_animals = ['python','gopher']
print(animals == even_more_animals) #=> True
print(animals is even_more_animals) #=> False
Output:-
True
False
```

##### Ques. How would you check if each word in a string begins with a capital letter?
The <b>istitle()</b> function checks if each word is capitalized.
```python
print( 'The Hilton'.istitle() ) #=> True
print( 'The dog'.istitle() ) #=> False
print( 'sticky rice'.istitle() ) #=> False
```

##### Ques. Check if a string contains a specific substring?
The <b>in</b> operator will return <b>True</b> if a string contains a substring.
```python
str = "My name is mohit saxena"

print( 'saxena' in str ) #=> True
print( 'car' in 'The worlds fastest plane' ) #=> False
```

##### Ques. Count the number of a specific character in a string?
* <b>count()</b> will return the number of occurrences of a specific character.
```python
print('The first president of the organization..'.count('o')) # 3

Output:- 3
```

##### Ques. Remove vowels from a string?
```python
string = 'Hello mohit saxena'
vowels = ('a','e','i','o','u')
new_string = ''
for ele in string:
    if ele not in vowels:
        new_string = new_string + ele
print(new_string)

# Using comprehension
print(''.join([c for c in string if c not in vowels]))

Output:- Hll mht sxn
```

##### Ques. When would you use rfind() ?
* <b>rfind()</b> is like find() but it starts searching from the right of a string and return the first matching substring.
```python
story = 'The price is right said Bob. The price is right.'
story.rfind('is')

Output:- 39
```