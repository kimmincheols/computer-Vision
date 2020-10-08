Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> li = [3,6,2,7]
>>> [elem*2 for elem in li]
[6, 12, 4, 14]
>>> li = [('a',1),('b',2),('c',7)]
>>> [n*3 for (x,n) in li]
[3, 6, 21]
>>> li=[3,2,4,1]
>>> [elem*2 for elem in[item+1 for item in li]]
[8, 6, 10, 4]
>>> 