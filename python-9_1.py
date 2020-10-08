Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def myfun(x,y):
	return x*y

>>> myfun(3,4)
12
>>> def myfun(x):
	return x*3

>>> def apply(q,x):
	return q(x)

>>> apply(myfun, 7)
21
>>> def myfun(b, c=3, d="hello"):
	return b+c

>>> myfun(5,3,"hello")
8
>>> myfun(5,3)
8
>>> myfun(5)
8
>>> def myfun(a,b,c):
	return a-b

>>> myfun(2,1,43)
1
>>> myfun(c=43,b=1,a=2)
1
>>> myfun(2,c=43,b=1)
1
>>> 