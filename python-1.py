Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>>  tu = (23, 'abc', 4.56, (2.3), 'def')
>>> li = ["abc", 34, 4.34, 23]
>>> st = "hello world"
>>> st = 'hello world'
>>> st = """this is a multi-line string that uses triple quotes."""
>>> tu = (23, 'abc', 4.56, (2.3), 'def')
>>> tu[1]
'abc'
>>> li = ["]
  File "<stdin>", line 1
    li = ["]
           ^
SyntaxError: EOL while scanning string literal
>>> li["abc", 34, 4.34, 23]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: list indices must be integers or slices, not tuple
>>> li = ["abc", 34, 4.34, 23]
>>> li[1]
34
>>> st = "hello world"
>>> st[1]
'e'
>>> t = (23, 'abc', 4.56, (2,3), 'def')
>>> t[1]
'abc'
>>> t[-3]
4.56
>>> t = (23, 'abc', 4.56, (2.3), 'def')
>>> t[1:4]
('abc', 4.56, 2.3)
>>> t[1:-1]
('abc', 4.56, 2.3)
>>> t[1:-1:2]
('abc', 2.3)
>>> t = (23, 'abc', 4.56, (2.3), 'def')
>>> t[:2]
(23, 'abc')
>>> t[2:]
(4.56, 2.3, 'def')
>>> t[:]
(23, 'abc', 4.56, 2.3, 'def')
>>> list2 = list1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'list1' is not defined
>>> list2 = list1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'list1' is not defined
>>> list2 = list1[:]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'list1' is not defined
>>> t = [1, 2, 4, 5]
>>> 3 in t
False
>>> 4 in t
True
>>> 4 not in t
False
>>> a = 'abcde'
>>> 'c' in a
True
>>> 'cd' in a
True
>>> 'ac' in a
False
>>> (1, 2, 3) + (4, 5, 6)
(1, 2, 3, 4, 5, 6)
>>> [1, 2, 3]  + [4, 5, 6]
[1, 2, 3, 4, 5, 6]
>>> "hello" + "" +"world"]
  File "<stdin>", line 1
    "hello" + "" +"world"]
                         ^
SyntaxError: unmatched ']'
>>> "Hello" + " "+ "World"
'Hello World'