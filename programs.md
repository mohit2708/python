### Table of Contents

|  No.  | Questions                                                                         |
| :---: | --------------------------------------------------------------------------------- |
|   1   | [swap two variables](#swap-two-variables)                                         |
|   2   | [prime or not](#program-to-check-if-a-number-is-even-or-odd)                      |
|       | [Count number of characters in a string](#count-number-of-characters-in-a-string) |
|       | [convert a list to string](#python-program-to-convert-a-list-to-string)           |
|       | [Reverse a Number](#reverse-a-number)                                             |


https://www.sanfoundry.com/python-problems-solutions/#python-basic-programs

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

### Prime Number Print
```python
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
```

### Reverse a Number
```python
# using a while loop
Number = int(input("Please Enter any Number: "))
Reverse = 0
while(Number > 0):
    Reminder = Number %10
    Reverse = (Reverse *10) + Reminder
    Number = Number //10

print("Reverse of entered number is = %d" %Reverse)

Output:-
Please Enter any Number: 68765
Reverse of entered number is = 56786

# Using String slicing
num = 9412
print(str(num)[::-1])

Output:-
num = 2149

# Using Recursion
num = int(input("Enter the number: "))  
revr_num = 0    # initial value is 0. It will hold the reversed number  
def recur_reverse(num):  
    global revr_num   # We can use it out of the function  
    if (num > 0):  
        Reminder = num % 10  
        revr_num = (revr_num * 10) + Reminder  
        recur_reverse(num // 10)  
    return revr_num  
  
  
revr_num = recur_reverse(num)  
print("Reverse of entered number is = %d" % revr_num)

Output:- 
Enter the number: 1284
Reverse of entered number is = 4821
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


### program to count the frequency of each character
```python
# using "in" operater
str1 = input ("Enter the string: ")
d = dict()
for c in str1:
    if c in d:
        d[c] = d[c] + 1
    else:
        d[c] = 1
print(d)

Output:- 
Enter the string: HheLlo
{'H': 1, 'h': 1, 'e': 1, 'L': 1, 'l': 1, 'o': 1}
Enter the string: Hello My name is Mohit Saxena
{'H': 1, 'e': 3, 'l': 2, 'o': 2, ' ': 5, 'M': 2, 'y': 1, 'n': 2, 'a': 3, 'm': 1, 'i': 2, 's': 1, 'h': 1, 't': 1, 'S': 1, 'x': 1}
----------------------------------------------------------------------------

# Use of “get()” function

```
