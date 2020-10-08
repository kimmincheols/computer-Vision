Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = "abc"
>>> y=34
>>> "%s xyz %d"%(x,y)
'abc xyz 34'
>>> "%s xyz %d" % ("abc",34)
'abc xyz 34'
>>> ";".join(["abc","def","ghi"])
'abc;def;ghi'
>>> "abc;def;ghi".split(";")
['abc', 'def', 'ghi']
>>> "hello" + str(2)
'hello2'
>>> 