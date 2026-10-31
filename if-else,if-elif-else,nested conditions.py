#if-else condition by using comparision operators
'''a=4
b=8
if a<b:
    print("less")
else:
    print("more")'''

'''a=10
b=20
if a>b:
    print("true")
else:
    print("false")'''

'''a=10
b=13
if a<=b:
    print("less")
else:
    print("more")'''

'''a=20
b=90
if a>=b:
    print("false")
else:
    print("true")'''

'''a=4
b=9
if a==b:
    print("equal")
else:
    print("not equal")'''

'''a=8
b=9
if a!=b:
    print("not equal")
else:
    print("equal")'''

'''a="python"
if a=="java":
    print("true")
else:
    print("false")'''

'''a=int(input("a value"))
b=int(input("b value"))
if a<b:
    print("hello")
else:
    print("hii")'''

'''a=int(input("a value"))
if a==40:
    print("bye")
else:
    print("hello")'''

#if condition by using logical operator
#and,or,not
'''a=5
b=10
if a>b and a<b:
    print("hii")
else:
    print("hello")'''

'''a=90
b=89
if a>b and b<a:
    print("true")
else:
    print("hello")'''

'''a=19
b=90
if a>=b and b>=a :
    print("true")'''

'''a=3
b=6
if a!=b and a==b:
    print("true")'''

'''a=20
b=80
if a<b or b>a:
    print("true")'''

'''a=13
b=155
if a>=b or a<=b:
    print("komali")'''

'''a=10
b=20
if a!=b or a==b:
    print("komal")'''

'''a=4
b=9
if not a<b:
    print("true")
else:
    print("false")'''

'''a=4
b=9
if not a>b:
    print("true")
else:
    print("false")'''

'''a=9
b=11
if not a<b and b>a:
    print("hasini")
else:
    print("false")'''



#if-conditions by using identify operators
#is,is not
'''a=9
if type(a) is int:
    print("it is int")
else:
    print("false")'''

'''a=65.6
if type is not int:
    print("it is int")
else:
    print("false")'''

'''a=float(input("any value"))
if type(a) is float:
        print("it is float")
    else:
    print("false")'''

#if-condition by using membership operators
#in,not in
'''a=2,3,4,5,6,7,8,9,10
if 10 in a:
    print("true")
else:
    print("false")'''

'''a=3,4,5,6,7,8,9,10
if 30 in a:
    print("true")
else:
    print("false")'''

'''a=3,4,5,6,7,8,9,10
if 30 not in a:
    print("true")
else:
    print("false")'''

'''a=int(nput("a value"))
if 50 in a:
    print("true")
else:
    print("false")'''#error

'''a=[5,6,7,8,9,10]
b=int(input("value"))
if b in a:
    print("true")
else:
    print("false")'''
#if-elif-else conditional statements
'''a=4
b=8
if a<b:
    print("less")
elif b>a:
    print("greater")
else:
    print("true")'''

'''a=10
b=90
if a==b:
    print("less")
elif b>a:
    print("greater")
else:
    print("true")'''

'''a=4
b=8
if a<b:
    print("less")
elif b>a:
    print("greater")

elif a!=b:
    print("not equal")
else:
    print("true")'''

#nested -if
'''a=5
b=10
if a<b:
    print("less")
    if b>a:
        print("greater")'''

'''a=5
b=10
if a==b:
    print("less")
    if b>a:
        print("greater")'''
'''a=5
b=10
if a==b:
    print("less")
if b>a:
        print("greater")'''#multiple if

'''a=5
b=10
if a<b:
    print("less")
    if b==a:
        print("greater")
    else:
        print("true")'''
'''a=12
b=15
if a==b:
    print("less")
    if b>a:
        print("greater")
    else:
        print("true")
else:
    print("false")'''

'''a=7
b=11
if a<b:
    print("less")
    if b==a:
        print("greater")
    elif a!=b:
        print("true")'''

#voting--> age 18 and above -->eligible for vote
          # age 18 and below -->not eligible for vote

'''a=int(input("enter ur age"))
if a>18:
    print("eligible for vote")
else:
    print("not eligible for vote")'''

#even or odd

a=int(input("enter any number"))
if a%2==0 :
    print("it is an even number")
else:
    print("it is an odd number")



    
    



