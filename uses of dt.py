Python 3.14.7 (tags/v3.14.7:823f032, Aug  5 2026, 10:51:32) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> int(4)
4
>>> int(5.7)
5
>>> int("hasini")
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    int("hasini")
ValueError: invalid literal for int() with base 10: 'hasini'
>>> int(5+6j)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int(5+6j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
>>> int(True)
1
>>> int(False)
0
>>> int
<class 'int'>
>>> float(34)
34.0
>>> float(56.98)
56.98
>>> float("host")
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    float("host")
ValueError: could not convert string to float: 'host'
>>> float(45+5j)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    float(45+5j)
TypeError: float() argument must be a string or a real number, not 'complex'
>>> float(True)
1.0
float(False)
0.0
str(45)
'45'
str(56.9)
'56.9'
str("donkey")
'donkey'
str(34-7j)
'(34-7j)'
str(True)
'True'
str(False)
'False'
complex(56)
(56+0j)
complex(7.98)
(7.98+0j)
complex("rat")
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    complex("rat")
ValueError: complex() arg is a malformed string
complex(567+45j)
(567+45j)
complex(True)
(1+0j)
compex(False)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    compex(False)
NameError: name 'compex' is not defined. Did you mean: 'complex'?
complex(False)
0j
bool(45)
True
bool(78.6)
True
bool('fox')
True
bool(45-9j)
True
bool(True)
True
bool(False)
False
