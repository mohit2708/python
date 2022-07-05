### Table of Contents

| No. | Questions |
|:----:| ---------
| 1 | [swap two variables](#swap-two-variables) |
| 2 | [prime or not](#program-to-check-if-a-number-is-even-or-odd) |
|   | [Count number of characters in a string](#count-number-of-characters-in-a-string) |
|   | [convert a list to string](#python-program-to-convert-a-list-to-string) |

### swap two variables
__Using a temporary variable__
```python
a = 11
b = 7

temp = a
a = b
b = temp

print(a) # 7
print(b) # 11
```
__Without a temporary variable__
```python
a = 11
b = 7

a, b = b, a

print(a) # 7
print(b) # 11
```
__Using arithmetic operators__
```python
a = 11
b = 7

a = a + b # a = 18, b = 7
b = a - b # a = 18, b = 11
a = a - b # a = 7,  b = 11

print(a) # 7
print(b) # 11
```
__Using multiplication and division operator__
```python
P = int( input("Please enter value for P: "))  
Q = int( input("Please enter value for Q: "))  
   
# To Swap the values of two variables using Addition and subtraction operator  
P = P * Q    
Q = P / Q   
P = P / Q  
   
print ("The Value of P after swapping: ", P)  
print ("The Value of Q after swapping: ", Q)
```

### Program to check if a number is Even or odd
```python
```python
# 1 Option
num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))

# 2 option
def evenOrOdd(n):
    if n%2 == 0:
        print('even Number hai')
    else:
        print('Odd Number hai')
evenOrOdd(6)
```

### Count number of characters in a string
```python
 string = "My Name is Mohit Saxena";
count = 0;

for i in range(0, len(string)):
    if(string[i] != ' '):
        count = count + 1;
print("Total number of characters in a string: " + str(count));

Output:- 19
```
### Python program to convert a list to string
```python
def listToString(s):
    blank =""
    for element in s:
        blank = blank + ' ' + element
    print(blank)

s = ['Hello', 'mohit', 'saxena']
listToString(s)

Output:- Hellomohitsaxena
------------------------------------------------------------------

# Using list comprehension 
s = ['I', 'want', 4, 'apples', 'and', 18, 'bananas']
listToStr = ' '.join([str(elem) for elem in s])
print(listToStr)

Output:- I want 4 apples and 18 bananas
----------------------------------------------------------------

# Using .join() method 
def listToString(s):
    str1 = " "
    return (str1.join(s))
    
s = ['Hello', 'Mohit', 'Saxena']
print(listToString(s))

Output:- Hello Mohit Saxena
----------------------------------------------------------------

# Using map()
s = ['I', 'want', 4, 'apples', 'and', 18, 'bananas']
listToStr = ' '.join(map(str, s))
print(listToStr)
```
