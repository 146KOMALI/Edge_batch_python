Python 3.14.7 (tags/v3.14.7:823f032, Aug  5 2026, 10:51:32) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Upper()
a="python"
a.upper()
'PYTHON'
#lower()
b="CODE"
b.lower
<built-in method lower of str object at 0x000002C95DC69D10>
b.lower()
'code'
#capitalize
c="python course"
c.capitalize()
'Python course'
#Title
d=" i am in class"
d.title()
' I Am In Class'
d.capitalize
<built-in method capitalize of str object at 0x000002C95DC847F0>
d.capitalize()
' i am in class'
d=" i am in class"
d.capitalize()
' i am in class'
#boolean in this strings
a="data science"
a.isupper()
False
a.islower()
True
>>> a.startswith("d")
True
>>> a.endwith("e")
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    a.endwith("e")
AttributeError: 'str' object has no attribute 'endwith'. Did you mean: 'endswith'?
>>> a.endswith("e")
True
>>> a.isalpha()
False
>>> a.isalpha("s")
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    a.isalpha("s")
TypeError: str.isalpha() takes no arguments (1 given)
>>> b="datascience"
>>> b.isalpha
<built-in method isalpha of str object at 0x000002C95C0C4FF0>
>>> a.isalpha()
False
>>> b.isalpha()
True
>>> a.isdigit()
False
>>> a.isalnum()
False
>>> c="12345"
>>> c.isdigit()
True
>>> f="hello"
>>> f.isalnum()
True
>>> #strip()
>>> #lstrip()
>>> #rstrip()
>>> a="       pooja      "
>>> a.strip()
'pooja'
>>> a.lstrip()
'pooja      '
>>> a.rstrip()
'       pooja'
#split()
a="python java c c++"
a.split()
['python', 'java', 'c', 'c++']
b="i am learning python full stack"
b.split()
['i', 'am', 'learning', 'python', 'full', 'stack']
#concentration()
#concatenation()
a="python"
b="course"
print(a+b)
pythoncourse
print(a+" "+b)
python course
a="code"
b="gnan"
print(a+b)
codegnan
fname="pooja"
lname="ch"
print(fname+lname)
poojach
print(fname.title()+" "+lname.title())
Pooja Ch
print(fname+" "+lname.title())
pooja Ch
#formatting
a=4
b=7
print(a+b)
11
print("the sum is ",a+b)
the sum is  11
print("the sum is,a+b")
the sum is,a+b
city+"vij"
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    city+"vij"
NameError: name 'city' is not defined
city="vij"
print("city is",city)
city is vij
#format method
a="motu"
b="patlu"
print("hello {} {}".format(a,b))
hello motu patlu
print("hello {}{}".format(a,b))
hello motupatlu
print("hello {} hello {}".format(a,b))
hello motu hello patlu
#fstring
a="virat"

b="kohli"
print(f"hello {a}{b}")
hello viratkohli
print(f"hello {a} {b}")
hello virat kohli
print(f"hello {a} hello {b}")
hello virat hello kohli
