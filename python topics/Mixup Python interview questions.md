### Ques. Difference between List and Tuples in Python?
|                                                     List                                                     |                                            Tuples                                             |
| :----------------------------------------------------------------------------------------------------------: | :-------------------------------------------------------------------------------------------: |
|                                   List is mutable. i.e they can be edited.                                   |                 Tuple is immutable. (tuples are lists which can’t be edited).                 |
|                               List iteration is slower and is time consuming.                                |                                  Tuple iteration is faster.                                   |
|                            List is useful for insertion and deletion operations.                             |               Tuple is useful for readonly operations like accessing elements.                |
|                                           List has a large memory.                                           |                                   Tuple has a small memory.                                   |
| List is stored in two blocks of memory (One is fixed sized and the other is variable sized for storing data) |                         Tuple is stored in a single block of memory.                          |
|                                     List provides many in-built methods.                                     |                              Tuples have less in-built methods.                               |
|                                     List operations are more error prone                                     |                                  Tuples operations are safe.                                  |
|      A list has data stored in  square brackets [] brackets. For example, list_1 = [10, ‘Chelsea’, 20]       | A tuple has data stored in parantheses () brackets. For example, tup_1 = (10, ‘Chelsea’ , 20) |


### Ques. Convert a list into a tuple?
* Using **tuple()** builtin function 
```python
list = [1,2,3,4]
result = tuple(list)
print(type(result))

Output:- <class 'tuple'>
```
* Using **loop** inside the tuple
```python
sample_list = ['Compile', 'With', 'Favtutor']
tuple1 = tuple(i for i in sample_list)
print(tuple1)

Output:- ('Compile', 'With', 'Favtutor')
```
* **Unpack** list inside the parenthesis
```python
sample_list = ['Compile', 'With', 'Favtutor']

#unpack list items and form tuple
tuple1 = (*sample_list,)

print(tuple1)
print(type(tuple1))

Output:- 
('Compile', 'With', 'Favtutor')
<class 'tuple'>
```

### Ques. What is Monkey Patching?
* The term monkey patching refers to dynamic(or run time) modifictaion of class or method.
* A class or method can be changed at the runtime.
```python
class A:  
   def hello(self):  
      print ("The hello() function is being called") 
      
def monkey_f():
    print ("monkey_f() is being called")

#normal class method call   
obj = A()
obj.hello()

#calling class method after monkey patch
obj.hello = monkey_f
obj.hello()

Output:- 
The hello() function is being called
monkey_f() is being called
```