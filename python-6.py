Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> for <item> in <collection>:<starements>
SyntaxError: invalid syntax
>>> for(x,y) in [(a,1), (b,2), (c,3), (d,4)]
SyntaxError: invalid syntax
>>> for(x,y) in [(a,1), (b,2), (c,3), (d,4)	print x
	     
SyntaxError: invalid syntax
>>> range(5) returne[0,1,2,3,4]
SyntaxError: invalid syntax
>>> for x in range(5):
	print x
	
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(x)?
>>> for i in range(len(mylist)):
	print i, mylist[i]
	
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(i, mylist[i])?
>>> for (i, item) in enumerate(mylist):
	print i, item
	
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(i, item)?
>>> 