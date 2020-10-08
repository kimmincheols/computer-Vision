Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> li = ['abc', 45, 4.34, 23]
>>> li[1] = 45
>>> li
['abc'. 45, 4.34, 23]
>>> t = (23, 'abc', 4.56, (2,3), 'def')
>>> t[2] = 3.14
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    t[2] = 3.14
TypeError: 'tuple' object does not support item assignment
>>> t = (23, 'abc', 3.14, (2,3), 'def')
>>> li = [1, 11, 3, 4, 5]
>>> li
[1, 11, 3, 4, 5]
>>> li.append('a')
>>> li
[1, 11, 3, 4, 5, 'a']
>>> li.insert(2, 'i')
>>> li
[1, 11, 'i', 3, 4, 5, 'a']
>>> li.extend([9, 8, 7])
>>> li
[1, 11, 'i', 3, 4, 5, 'a', 9, 8, 7]
>>> li.append([10, 11, 12])
>>> li
[1, 11, 'i', 3, 4, 5, 'a', 9, 8, 7, [10, 11, 12]]
>>> li = ['a','b','c','b']
>>> li.index('b')
1
>>> li.count('b')
2
>>> li.remove('b')
>>> li
['a', 'c', 'b']
>>> li = [5, 2, 6, 8]
>>> li.reverse()
>>> li
[8, 6, 2, 5]
>>> li.sort()
>>> li
[2, 5, 6, 8]
>>> li.sort(some_function)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    li.sort(some_function)
NameError: name 'some_function' is not defined
>>> li = list(tu)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    li = list(tu)
NameError: name 'tu' is not defined
>>> tu = tuple(li)
>>> li = list(tu)
>>> 
