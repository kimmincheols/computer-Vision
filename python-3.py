Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> d = {'user':'bozo', 'pswd':1234}
>>> d['user']
'bozo'
>>> d['pswd']
1234
>>> d['bozo']
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    d['bozo']
KeyError: 'bozo'
>>> d['user'] = 'clown'
>>> d
{'user': 'clown', 'pswd': 1234}
>>> d['id'] = 45
>>> d
{'user': 'clown', 'pswd': 1234, 'id': 45}
>>> d = {'user':'bozo', 'p':1234, 'i':34}
>>> del d['user']
>>> d
{'p': 1234, 'i': 34}
>>> d.clear()
>>> d
{}
>>> a=[1,2]
>>> del a[1]
>>> a
[1]
>>> d={'user':'bozo', 'p':1234, 'i':34}
>>> d.keys()
dict_keys(['user', 'p', 'i'])
>>> d.values()
dict_values(['bozo', 1234, 34])
>>> d.items()
dict_items([('user', 'bozo'), ('p', 1234), ('i', 34)])
>>> 
