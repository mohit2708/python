### Table of Contents

|  No.  | Questions                                                                                               |
| :---: | ------------------------------------------------------------------------------------------------------- |
|   1   | [swap two variables](#swap-two-variables)                                                               |
|   2   | [check if a number is Even or odd](#program-to-check-if-a-number-is-even-or-odd)                        |
|       | [To Check if a String is a Palindrome](#To-Check-if-a-String-is-a-Palindrome)                           |
|       | [To Check if a Number is a Palindrome](#To-Check-if-a-Number-is-a-Palindrome)                           |
|       | [Find the Factorial of a Number](#Find-the-Factorial-of-a-Number)                                       |
|       | [find Fibonacci series up to n](#find-Fibonacci-series-up-to-n)                                         |
|       | [check if the number is an Armstrong number or not](#check-if-the-number-is-an-Armstrong-number-or-not) |
|       | [generate a random number between 0 and 9](#Program-to-generate-a-random-number-between-0-and-9)        |
|       | [Get a Substring of a String](#Get-a-Substring-of-a-String)                                             |


# String Program
|       | [How to reverse a sentence in Python input by User?](#How-to-reverse-a-sentence-in-Python-input-by-User)  |
|       | [Count number of characters in a string](#count-number-of-characters-in-a-string)                |
|       | [convert a list to string](#program-to-convert-a-list-to-string)                                 |

### swap two variables?
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

# XOR swap
P = P ^ Q    
Q = P ^ Q   
P = P ^ Q  
   
print ("The Value of P after swapping: ", P)  
print ("The Value of Q after swapping: ", Q)
```

### Program to check if a number is Even or odd
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

### To Check if a String is a Palindrome
```python
def isPalindrome(string):
    rev = string[::-1]
    # rev = ''.join(reversed(s))    # 2nd Option to reversed string
    if(rev == string):
        print("The string is a palindrome!");
    else:
        print("The string isn't a palindrome!");

s = "malayalam"
isPalindrome(s)

Output:- The string is a palindrome!
=========================================================
x = "malayalam"
 
w = ""
for i in x:
    w = i + w 
if (x == w):
    print("Yes")
else:
    print("No")

Output:- Yes
```

### To Check if a Number is a Palindrome
```python
num = int(input("Enter a number:"))
temp = num
reverse = 0
while temp > 0:
    remainder = temp%10
    reverse = (reverse*10)+remainder
    temp = temp//10
if num == reverse:
  print('Palindrome')
else:
  print("Not Palindrome")
```

### Prime Number Print between lower to upper
```python
lower = int(input(" Please Enter the Minimum Value: "))
upper = int(input(" Please Enter the Maximum Value: "))

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)

Output:- 
11
13
17
19
```

### Find the Factorial of a Number
* factorial of 6 is 6*5*4*3*2*1 which is 720.
```python
num = int(input("Enter a number: "))    
factorial = 1    
if num < 0:    
   print(" Factorial does not exist for negative numbers")    
elif num == 0:    
   print("The factorial of 0 is 1")    
else:    
   for i in range(1,num + 1):    
       factorial = factorial*i    
   print("The factorial of",num,"is",factorial) 

Output:- 
Enter a number: 6
The factorial of 6 is 720
```

### Find Fibonacci series up to n
```python
def fibonacci(n):
    first = 0
    second = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1:
        return second
    else:
        print(first)
        print(second)
        for i in range(2, n):
            third = first + second
            first = second
            second = third
            print(third)

fibonacci(9)

Output:- 0 1 1 2 3 5 8 13 21
=======================================================
# Using While Loop
def fibonacci(n):
    first = 0
    second = 1
    count = 0
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1:
        return second
    else:
        while count < n:
            print(first)  
            third = first + second  
           # At last, we will update values  
            first = second  
            second = third  
            count += 1
fibonacci(9)
```

### check if the number is an Armstrong number or not?
* 153 = 1*1*1 + 5*5*5 + 3*3*3 = 153
* 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 + 4*4*4*4 = 1634
```python
num = int(input("Enter a number: "))
len = len(str(num))
sum = 0
temp = num

while temp > 0:
   digit = temp % 10
   sum = sum + digit ** len
   temp = temp//10

if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")

Output:- 
Enter a number: 1634
1634 is an Armstrong number
```

### Check Prime Number Or Not
```python
num = int(input("Enter a number: "))
if num > 1:
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           break
   else:
       print(num,"is a prime number")
       
else:
   print(num,"is not a prime number")

Output:- 3
3 is a prime number
```

### print prime numbers from 1 to N.
```python
lower_value = int(input ("Please, Enter the Lowest Range Value: "))  
upper_value = int(input ("Please, Enter the Upper Range Value: "))  
  
print ("The Prime Numbers in the range are: ")  
for number in range (lower_value, upper_value + 1):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            print (number)  

Output:-
Please, Enter the Lowest Range Value: 1
Please, Enter the Upper Range Value: 10
The Prime Numbers in the range are: 
2
3
5
7
```

### Extract numbers from string?
```python
new_string = "Germany26China47Australia88"
 
emp_str = ""
for m in new_string:
    if m.isdigit():
        emp_str = emp_str + m
print("Find numbers from string:",emp_str)

Output:- Find numbers from string: 264788

# 2 Example
new_str = "Micheal 89 George 94"

emp_lis = []
for z in new_str.split():
   if z.isdigit():
      emp_lis.append(int(z))

print("Find number in string:",emp_lis)
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

### program to convert a list to string
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


### Program to generate a random number between 0 and 9?
```python
import random
print(random.randint(0,9))

Output:- 0 se 9 tak ka koi bhi number aa sakta hai.
```

### Get a Substring of a String
```python
my_string = "I love python."

print(my_string[2:6])   # You need to specify the starting index and the ending index of the substring. In this case, love starts at index 2 and ends at index 6.

print(my_string[2:])    # All the text from index 2 to the end are selected

print(my_string[:-1])   # All the text before the last index is selected.

Output:-
love
love python.
I love python
```



### 



### 


## String Programes

### How to reverse a sentence in Python input by User?
```python
inputsentence = input("Please input  a sentence : ")
splitString = inputsentence.split()      # ['i', 'love', 'Mohit', 'Saxena']
reversedString = reversed(splitString)
print(" ".join(reversedString))

Output:- i love Mohit Saxena
Saxena Mohit love i

# 2 Option 

```

### How to reverse a Word, String or Sentence in Python input by User?
```python
my_str = input("Please enter your own String : ")
str = ''
for i in my_str:
    str = i + str
print("\nThe Original String is: ", my_str)
print("The Reversed String is: ", str)

Output:-
The Original String is:  i love Mohit Saxena
The Reversed String is:  anexaS tihoM evol i
```

### Find repeated characters in a string python?
```python
string = "Great responsibility";  
  
for i in range(0, len(string)):  
    count = 1;  
    for j in range(i+1, len(string)):  
        if(string[i] == string[j] and string[i] != ' '):  
            count = count + 1;  
            string = string[:j] + '0' + string[j+1:];  
 
    if(count > 1 and string[i] != '0'):  
        print(string[i]);

output:- r
e
t
s
i
```

### String Pattern
```python
str1 = input("enter the string: ")
len = len(str1)
for i in range(len):
    for j in range(i+1):
        print(str1[i], end="")
    print()

Output:-
enter the string: Mohit
M
oo
hhh
iiii
ttttt
========================================================================
str1 = input("enter the string: ")
len = len(str1)
for i in range(len):
    for j in range(i+1):
        print(str1[j], end="")
    print()

Output:-
enter the string: mohit
m
mo
moh
mohi
mohit
```







https://prepinsta.com/python-program/find-a-number-is-palindrome-or-not/
