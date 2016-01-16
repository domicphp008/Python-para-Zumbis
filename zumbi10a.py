Python 3.5.1 (v3.5.1:37a07cee5969, Dec  5 2015, 21:12:44) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> 42
42
>>> 3.1415
3.1415
>>> type(42)
<class 'int'>
>>> type(3.1415)
<class 'float'>
>>> type('abacate')
<class 'str'>
>>> a = 42
>>> b = 'abacate'
>>> id(42)
4297539264
>>> id('abacate')
4390526176
>>> id(b)
4390526176
>>> 2 * a
84
>>> c = a + 3
>>> c
45
>>> 
==== RESTART: /Users/domiciosilva/Documents/Python para Zumbis/zumbi10.py ====
5
>>> 
==== RESTART: /Users/domiciosilva/Documents/Python para Zumbis/zumbi10.py ====
5
Traceback (most recent call last):
  File "/Users/domiciosilva/Documents/Python para Zumbis/zumbi10.py", line 7, in <module>
    print (a + b)
TypeError: Can't convert 'int' object to str implicitly
>>> 
==== RESTART: /Users/domiciosilva/Documents/Python para Zumbis/zumbi10.py ====
5
abacate e banana
>>> dir ('abacater')
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> help('abacate' .upper)
Help on built-in function upper:

upper(...) method of builtins.str instance
    S.upper() -> str
    
    Return a copy of S converted to uppercase.

>>> 
