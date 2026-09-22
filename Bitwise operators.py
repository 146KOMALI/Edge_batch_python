Python 3.14.7 (tags/v3.14.7:823f032, Aug  5 2026, 10:51:32) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #bitwise operators
>>> #&-->and
>>> a=2
>>> b=3
>>> a&b
2
>>> #because binary of a=0010,b=0011 in &-->0,1= 0; 1,0= 0; 0,0= 0; 1,1= 1
>>> #and then a,b = 0010 * 8421 =2
>>> a=13
>>> b=12
>>> a&b
12
>>> bin(a)
'0b1101'
>>> bin(b)
'0b1100'
>>> #here b is taken as 0
>>> #|-->or
>>> a=2
>>> a=3
>>> a|b
15
>>> #because binary of a=0010,b=0011 in |-->0,1= 1; 1,0= 1; 0,0= 0; 1,1= 1
... #and then a,b = 0011 =1*1+1*2=3
>>> a=3
>>> b=6
>>> a|b
7
>>> a=2
>>> b=3
>>> a|b
3
>>> #^--->cap
>>> a=2
>>> b=3
>>> a^b
1
>>> #because binary of a=0010,b=0011 in |-->0,1= 1; 1,0= 1; 0,0= 0; 1,1= 0
... #and then a,b = 0001 =1*1+2*0+4*0+8*0=1
>>> a=8
>>> b=7
a^b
15
#~-->nagotiation
a= 4
~a
-5
#because ~a=(-a+1)
b=90
~b
-91
c=-56
~c
55
#<<---> left shift
a=3
a<<2
12
