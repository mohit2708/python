### swap two variables in Python
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
