Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=10
type(a)
<class 'int'>
b=1.2
type(b)
<class 'float'>
c=2+6K
SyntaxError: invalid decimal literal
c=2+5j
type(c)
<class 'complex'>
s="code"
type(s)
<class 'str'>
id(s)
140736629438136
l=[1,2,3]
type(l)
<class 'list'>
id(s)
140736629438136
id(l)
1790813737152
l.append(35)
l.pop(2)
3
id(l)
1790813737152
l=[1,2,3,'56']
l.append(12)
id(l)
1790765080448
print(l)
[1, 2, 3, '56', 12]
l.pop(56)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    l.pop(56)
IndexError: pop index out of range
l.pop('56')
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    l.pop('56')
TypeError: 'str' object cannot be interpreted as an integer
l=[1,1,1,1,1]
l
[1, 1, 1, 1, 1]
t=(10,20,30)
type(t)
<class 'tuple'>
t.append(40)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    t.append(40)
AttributeError: 'tuple' object has no attribute 'append'
s="R"
id(s)
140736629449656
t=
SyntaxError: invalid syntax
t=(1,1,1,1)
t
(1, 1, 1, 1)
s="r"
s+="a"
>>> print(s)
ra
>>> id(s)
1790812177136
>>> s={123,345,123,123,456,678}
>>> s
{456, 345, 123, 678}
>>> type(s)
<class 'set'>
>>> student{
...     
SyntaxError: '{' was never closed
>>> 
>>> student{
...     
SyntaxError: '{' was never closed
>>> student{}
SyntaxError: invalid syntax
>>> d={1,'one',34,5,6,[1,2]}
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    d={1,'one',34,5,6,[1,2]}
TypeError: unhashable type: 'list'
>>> d={"student":'name',"age":21,"course":'b.tech'}
>>> d
{'student': 'name', 'age': 21, 'course': 'b.tech'}
>>> type(d)
<class 'dict'>
>>> s=True
>>> s
True
>>> type(s)
<class 'bool'>
>>> s=False
>>> type(s)
<class 'bool'>
>>> # none
>>> s={}
>>> s=none
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    s=none
NameError: name 'none' is not defined. Did you mean: 'None'?
>>> s=None
>>> type(s)
<class 'NoneType'>
