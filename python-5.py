Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> if x == 3:
print "X equals 3."
elif x == 2:
print "X equals 2."
else:
print "X equals something else."
print "This is outside the ‘if’."
SyntaxError: expected an indented block
>>> x = 3
>>> while x < 5:
print x, "still in the loop"
x = x + 1
3 still in the loop
4 still in the loop
>>> x = 6
>>> while x < 5:
print x, "still in the loop"
SyntaxError: multiple statements found while compiling a single statement
>>> assert(number_of_players < 5)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    assert(number_of_players < 5)
NameError: name 'number_of_players' is not defined
>>> 
