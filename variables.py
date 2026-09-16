Python 3.14.7 (tags/v3.14.7:823f032, Aug  5 2026, 10:51:32) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#variables
a=10
print(a)
10
print(30)
30
b=20
print(b)
20
print(C)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print(C)
NameError: name 'C' is not defined
c=56
prin(C)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    prin(C)
NameError: name 'prin' is not defined. Did you mean: 'print'?
print(c)
56
4=36
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
a3=45
print(a3)
45
f4=89
print(f4)
89
print(a1234567890)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print(a1234567890)
NameError: name 'a1234567890' is not defined
a1234567890=100
print(a1234567890)
100
a=3,g=8
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
a=6
b=9
print(a+b)
15
a,b=1,2
print(a-b)
-1
@=3
SyntaxError: invalid syntax
%8=8
SyntaxError: invalid syntax
_a=34
print(_a)
34
_60
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    _60
NameError: name '_60' is not defined
_=60
print(_)
60
if=56
SyntaxError: invalid syntax
else=89
SyntaxError: invalid syntax
first name=8
SyntaxError: invalid syntax
first_name=8
print(first_name)
8
firstname=3
print(firstname)
3
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
SyntaxError: invalid syntax
a=2;d=9
print(a*d)
18
a=2,7,9,0,6,9
print(a)
(2, 7, 9, 0, 6, 9)
a,b,c=123
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    a,b,c=123
TypeError: cannot unpack non-iterable int object
a,b,c=1,2,3
print(a,b,c)
1 2 3
a,b,c
(1, 2, 3)
a,g,j=2,6,7,8,9
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    a,g,j=2,6,7,8,9
ValueError: too many values to unpack (expected 3, got 5)
>>> #case sensitive
>>> city=6
>>> CITY=7
>>> City=8
>>> print(city,CITY,City)
6 7 8
>>> a=8
>>> b=9
>>> print(a)
8
>>> del b
>>> print(b)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    print(b)
NameError: name 'b' is not defined
