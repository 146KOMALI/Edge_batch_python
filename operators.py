Python 3.14.7 (tags/v3.14.7:823f032, Aug  5 2026, 10:51:32) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#arithmatic
a=8
b=5
print(a+b)
13
print(a-b)
3
print(a*b)
40
print(a//b)
1
print(a/b)
1.6
print(a%b)
3
print(a**b)
32768
#8**3 means a power b
#assignment
a=45
b=40
print(a+=b)
SyntaxError: invalid syntax
a+=b
a
85
a-=b
a
45
a*=b
a
1800
a//=b
a
45
a/=b
a
1.125
a%=b
a
1.125
a**=b
a
111.19900414606003
a=12
b=12
b+=a
b
24
a-=b
b
24
b-=a
b
36
a*=b
b
36
a
-432
b//=a
b
-1
b/=a
b
0.0023148148148148147
b%=a
b
-431.99768518518516
b**=a
b
0.0
#comparision
a=12
b=90
a<b
True
b>a
True
a>b
False
b<a
False
a<=b
True
b>=a
True
a>=b
False
b<=a
False
a!=b
True
#!==not equal to
a==b
False
logical
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    logical
NameError: name 'logical' is not defined
#logical
a=56
b=45
a>b and b<a
True
a>=b and b<=a
True
a!=0 and a==0
False
a>b or b<a
True
a>=b or b<=a
True
>>> a!=b or a==b
True
>>> not true
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    not true
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> not True
False
>>> not False
True
>>> #identify
>>> a=56
>>> type(a) is int
True
>>> type(a) is not int
False
>>> type(a) is not float
True
>>> typ(a) is float
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    typ(a) is float
NameError: name 'typ' is not defined. Did you mean: 'type'?
>>> type(a) is  float
False
>>> #membership
>>> a=7,8,9,10,30
>>> 1 in a
False
>>> 40 is not in a
SyntaxError: invalid syntax
>>> 40 not in a
True
>>> 8 in a
True
>>> 30 in a
True
