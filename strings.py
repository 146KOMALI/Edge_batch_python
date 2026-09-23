Python 3.14.7 (tags/v3.14.7:823f032, Aug  5 2026, 10:51:32) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#strings
#1.lenght--> len
a="python"
len(a)
6
b="komala hasini"
len(b)
13
c=''
len(c)
0
d=" "
len(d)
1
a=123456
a"123456"
SyntaxError: invalid syntax
a="1233456"
len(a)
7
#2.Count()
a="twinkle twinkle little star"
a.count("twinkle")
2
>>> a.count('t')
5
>>> a.count("i")
3
>>> a.count(" ")
3
>>> a.count('')
28
>>> #find a string
>>> a="python"
>>> a[3]
'h'
>>> a.find("h")
3
>>> #in slicing or striding we can the position no the output is char but in find we give input in char the ouput is in position no
>>> b="hello"
>>> b.find("ll")
2
>>> #escape sequences
>>> #\n --> new line
>>> #\t --> tab space
>>> a="name\nmoblie no\tcity\nmail id"
>>> print(a)
name
moblie no	city
mail id
>>> a="name:komala hasini\nmobile no:9063807105\tcity:rjy\nmail id komali@gmail.com"
>>> print(a)
name:komala hasini
mobile no:9063807105	city:rjy
mail id komali@gmail.com
>>> #replace()
>>> a="wait untill you suceed"
>>> a.replace("wait","work")
'work untill you suceed'
>>> b="python ml"
>>> b.replace("ml","ai")
'python ai'
