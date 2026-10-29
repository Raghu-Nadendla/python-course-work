Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=10
a
10
float(a)
10.0
complex(a)
(10+0j)
str(a)
'10'
list(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
b=10.0
b
10.0
int(b)
10
complex(b)
(10+0j)
str(b)
'10.0'
tlist(b)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    tlist(b)
NameError: name 'tlist' is not defined. Did you mean: 'list'?
tuple(b)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    tuple(b)
TypeError: 'float' object is not iterable
set(b)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    set(b)
TypeError: 'float' object is not iterable
dict(b)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    dict(b)
TypeError: 'float' object is not iterable
bool(b)
True
c=10+j
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    c=10+j
NameError: name 'j' is not defined
c=10+0j
c
(10+0j)
int(c)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(c)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    float(c)
TypeError: float() argument must be a string or a real number, not 'complex'
str(c)
'(10+0j)'
list(c)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    list(c)
TypeError: 'complex' object is not iterable
tuple(c)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    tuple(c)
TypeError: 'complex' object is not iterable
set(c)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    set(c)
TypeError: 'complex' object is not iterable
dict(c)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    dict(c)
TypeError: 'complex' object is not iterable
boolan(c)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    boolan(c)
NameError: name 'boolan' is not defined. Did you mean: 'bool'?
str='codegan'
str
'codegan'
int(str)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    int(str)
ValueError: invalid literal for int() with base 10: 'codegan'
str='1234"
SyntaxError: unterminated string literal (detected at line 1)
str='1234'
str
'1234'
int(str)
1234
float(str)
1234.0
complex(str)
(1234+0j)
list(str)
['1', '2', '3', '4']
tuple(str)
('1', '2', '3', '4')
set(str)
{'1', '4', '3', '2'}
dict(str)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    dict(str)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
bool(str)
True
tuple=[1,2,3,67,89]
int(tuple)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    int(tuple)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
list=[1,2,34,5,6,67,]
int(list)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    int(list)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
List=[1,2,3,4,5]
int(List)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    int(List)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
float(List)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    float(List)
TypeError: float() argument must be a string or a real number, not 'list'
complex(List)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    complex(List)
TypeError: complex() first argument must be a string or a number, not 'list'
str(List)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    str(List)
TypeError: 'str' object is not callable
string(List)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    string(List)
NameError: name 'string' is not defined
bool(List)
True
set(List)
{1, 2, 3, 4, 5}
dict(List)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    dict(List)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
tuple=(1,2,3,5)
int(tuple)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    int(tuple)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
float(tuple)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    float(tuple)
TypeError: float() argument must be a string or a real number, not 'tuple'
str(tuple)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    str(tuple)
TypeError: 'str' object is not callable
list(tupl)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    list(tupl)
NameError: name 'tupl' is not defined. Did you mean: 'tuple'?
list(tuple)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    list(tuple)
TypeError: 'list' object is not callable
set(tuple)
{1, 2, 3, 5}
dict(list)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    dict(list)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
bool(tuple)
True
set={1,2,3,4}
set
{1, 2, 3, 4}
str(set)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    str(set)
TypeError: 'str' object is not callable
list(set)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    list(set)
TypeError: 'list' object is not callable
tuple(set)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    tuple(set)
TypeError: 'tuple' object is not callable
dict(set)
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    dict(set)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
bool(set)
True
dict={"raghu":'name',"age":2}
dict
{'raghu': 'name', 'age': 2}
str(dict)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    str(dict)
TypeError: 'str' object is not callable
list(dict)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    list(dict)
TypeError: 'list' object is not callable
int(dic)
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    int(dic)
NameError: name 'dic' is not defined. Did you mean: 'dict'?
int(dict)
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    int(dict)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'dict'
bool(dic)
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    bool(dic)
NameError: name 'dic' is not defined. Did you mean: 'dict'?
bool(dict)
True
str="codegan"
str
'codegan'
int(str)
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    int(str)
ValueError: invalid literal for int() with base 10: 'codegan'
tuple(str)
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    tuple(str)
TypeError: 'tuple' object is not callable
list(str)
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    list(str)
TypeError: 'list' object is not callable
set(str)
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    set(str)
TypeError: 'set' object is not callable
>>> dict(str)
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    dict(str)
TypeError: 'dict' object is not callable
>>> bool=1
>>> bool
1
>>> int(bool)
1
>>> float(bool)
1.0
>>> complex(bool)
(1+0j)
>>> str(bool)
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    str(bool)
TypeError: 'str' object is not callable
>>> list(bool)
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    list(bool)
TypeError: 'list' object is not callable
>>> tuple(bool)
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    tuple(bool)
TypeError: 'tuple' object is not callable
>>> set(bool)
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    set(bool)
TypeError: 'set' object is not callable
>>> dict(bool)
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    dict(bool)
TypeError: 'dict' object is not callable
>>> '''
... int	->float, complex, str, bool
float->	int, complex, str, bool
complex->	str, bool
str	->int, float, complex, bool, list, tuple, set
list->	str, bool, tuple, set
tuple-->	str, bool, list, set
set	->str, bool, list, tuple
dict->	str, bool, list, tuple, set
bool	int, float, complex, str
