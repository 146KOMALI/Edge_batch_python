Python 3.14.7 (tags/v3.14.7:823f032, Aug  5 2026, 10:51:32) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #List[]
>>> a=[2,4.5,"python",6+9j,True,False]
>>> print(a)
[2, 4.5, 'python', (6+9j), True, False]
>>> type(a)
<class 'list'>
>>> b=6.7
>>> type(b)
<class 'float'>
>>> c=[6.7]
>>> type(c)
<class 'list'>
>>> a=["python","java","c","c++"]
>>> a.append("ml")
>>> a
['python', 'java', 'c', 'c++', 'ml']
>>> a.append("ai","ds")
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    a.append("ai","ds")
TypeError: list.append() takes exactly one argument (2 given)
>>> a.append(["ai","ds"])
>>> a
['python', 'java', 'c', 'c++', 'ml', ['ai', 'ds']]
>>> #extend()
>>> a=["ai","ml","ds"]
>>> a.extend(["python","java"])
>>> a
['ai', 'ml', 'ds', 'python', 'java']
>>> #insert()
>>> b=["black","white"]
>>> b.insert(1,"red")
>>> b
['black', 'red', 'white']
>>> a=["apple","banana","grapes"]
>>> a.index("banana")
1
>>> a.copy()
['apple', 'banana', 'grapes']
>>> b=a.copy()
>>> b
['apple', 'banana', 'grapes']
>>> #sort
>>> a=["python","java","ds","ml","ai"]
>>> a.sort()
>>> a
['ai', 'ds', 'java', 'ml', 'python']
>>> b=[7,3,9,11,30,50,2,0,6]
>>> b.sort()
>>> b
[0, 2, 3, 6, 7, 9, 11, 30, 50]
>>> #reverse()
>>> a=["chocolates","icecream","briyani","kfc"]
>>> a.reverse()
b
[0, 2, 3, 6, 7, 9, 11, 30, 50]
a.reverse()
a
['chocolates', 'icecream', 'briyani', 'kfc']
b=[6,8,3,4,0,1,20]
b.reverse()
b
[20, 1, 0, 4, 3, 8, 6]
#pop()
a=["red","black","white","blue"]
a.pop()
'blue'
a
['red', 'black', 'white']
a.pop("white")
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    a.pop("white")
TypeError: 'str' object cannot be interpreted as an integer
a.pop(1)
'black'
a
['red', 'white']
a.remove("red")
a
['white']
a=["hyb","vja","vzg"]
len(a)
3
b="hyb"
len(b)
3
c=["hyb"]
len(c)
1
a.count("vzg","hyb","vzg","vja"]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
a.count("vzg")
1
b=["vzg","hyb","vzg","vja"]
b.count("vzg")
2
#clear
a=["moulika","harika","harini","geethika"]
a.clear()
a
[]
b=[]
b.append("hello")
b
['hello']
#tuple
a=(3,5.6,"pooja",7+9j,True,False)
print(a)
(3, 5.6, 'pooja', (7+9j), True, False)
type(a)
<class 'tuple'>
len(a)
6
a.count(True)
1
a.index(7+9j)
3
