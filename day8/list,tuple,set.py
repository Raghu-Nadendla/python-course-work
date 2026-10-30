Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#modifying methods in list
l=[23,1,24,45,67,90]
l.pop()
90
l.pop()
67
l.pop()
45
l.pop(0)
23
l
[1, 24]
l.clear()
l
[]
l=[1,2,35555]
l
[1, 2, 35555]
l.remove(2)
l
[1, 35555]
l=[23,45,56,67,89,90]
l.count(45)
1
l.count(90)
1
l.count(67)
1
l
[23, 45, 56, 67, 89, 90]
l.count(23)
1
l.count(45)
1
l.reverse()
l
[90, 89, 67, 56, 45, 23]
l.sort(reverse=True)
l
[90, 89, 67, 56, 45, 23]
a=[1,2]
c=a
c
[1, 2]
c.append(3)
c
[1, 2, 3]
# any and all function
l=[90,56,1,2,3]
l
[90, 56, 1, 2, 3]
any(l)
True
l.append(0)
l
[90, 56, 1, 2, 3, 0]
any(l)
True
all(l)
False
k=[0,0.0,'']
k
[0, 0.0, '']
any(k)
False
all(k)
False
# tuple is collection of multiple values
# it is mutable ,allow dublicates ,orderd ,heteroginous
t=()
t=tuple()
t=(1,2,3,4,5)
t
(1, 2, 3, 4, 5)
type(t)
<class 'tuple'>
t=1,2,3,4
t
(1, 2, 3, 4)
t=(1)
t
1
t=(2,)
t
(2,)
t=(1,2,3,4,4,4,4,4)
t
(1, 2, 3, 4, 4, 4, 4, 4)
t=(1,1.1,'hyty',[1,2,3,4],{1,2,3},{1:1},False)
t
(1, 1.1, 'hyty', [1, 2, 3, 4], {1, 2, 3}, {1: 1}, False)
#packing and unpacking
t=(1,2,3,4,5)
t
(1, 2, 3, 4, 5)
a,b,c,d,e=t
a
1
c
3
e
5
d
4
a,b,c=(1,1,1,2,3,4,4,4,6)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    a,b,c=(1,1,1,2,3,4,4,4,6)
ValueError: too many values to unpack (expected 3)
a,b,c=(1,2,3)
a
1
b
2
c
3
t=(1,2,3,4)
t
(1, 2, 3, 4)
t=(1,1.1,'hyty',[1,2,3,4],{1,2,3},{1:1},False)
t
(1, 1.1, 'hyty', [1, 2, 3, 4], {1, 2, 3}, {1: 1}, False)
len(t)
7
t[3]
[1, 2, 3, 4]
t[3].append(1)
t
(1, 1.1, 'hyty', [1, 2, 3, 4, 1], {1, 2, 3}, {1: 1}, False)
#tuple operatitons
a=(1,2,3,5)
a
(1, 2, 3, 5)
b=(5,6,7)
b
(5, 6, 7)
a+b
(1, 2, 3, 5, 5, 6, 7)
a*2
(1, 2, 3, 5, 1, 2, 3, 5)
t=(1,1.1,'hyty',[1,2,3,4],{1,2,3},{1:1},False)
t
(1, 1.1, 'hyty', [1, 2, 3, 4], {1, 2, 3}, {1: 1}, False)
t[2]
'hyty'
t[6]
False
t[4]
{1, 2, 3}
t[-1]
False
t[-4]
[1, 2, 3, 4]
t[-1:]
(False,)
t[3:6]
([1, 2, 3, 4], {1, 2, 3}, {1: 1})
t[-2:]
({1: 1}, False)
t[::-1]
(False, {1: 1}, {1, 2, 3}, [1, 2, 3, 4], 'hyty', 1.1, 1)
l in t
False
False not in t
False
5 not in t
True
#tuple methods
l=(23,1,24,45,67,90)
l
(23, 1, 24, 45, 67, 90)
l.len()
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    l.len()
AttributeError: 'tuple' object has no attribute 'len'
len(l)
6
max(l)
90
min(l)
1
count(l)
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    count(l)
NameError: name 'count' is not defined. Did you mean: 'round'?
l.count()
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    l.count()
TypeError: tuple.count() takes exactly one argument (0 given)
t.count()
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    t.count()
TypeError: tuple.count() takes exactly one argument (0 given)
l.count(45)
1
l.index(23)
0
l.index(90)
5
any(l)
True
all(l)
True
l
(23, 1, 24, 45, 67, 90)
sum(l)
250
#set is a collections of values ()
#undorderd uni mut het(con) dyn
s={90,56,78,45,87}
s
{87, 56, 90, 45, 78}
s={1,1,1,1,1,1,1}
s
{1}
s=set()
s.add(1)
s
{1}
s.add(1.0)
s
{1}
s.add(1.2)
s
{1, 1.2}
s.add('str')
s
{1, 'str', 1.2}
 s.add(2+6j)
 
SyntaxError: unexpected indent
s.add(2+8j)
s
{1, (2+8j), 'str', 1.2}
#set operators
a={1,4,6,8}
b={2,5,6}
a+b
Traceback (most recent call last):
  File "<pyshell#138>", line 1, in <module>
    a+b
TypeError: unsupported operand type(s) for +: 'set' and 'set'
# in set there is no conacatin repuation indexing slicing
 a
 
SyntaxError: unexpected indent
a
{8, 1, 4, 6}
b
{2, 5, 6}
4 in a
True
5 in 5
Traceback (most recent call last):
  File "<pyshell#144>", line 1, in <module>
    5 in 5
TypeError: argument of type 'int' is not iterable
5 in b
True
a
{8, 1, 4, 6}
b
{2, 5, 6}
a | b
{1, 2, 4, 5, 6, 8}
a & b
{6}
a^b
{1, 2, 4, 5, 8}
a=b
a-b
set()
a
{2, 5, 6}
>>> b
{2, 5, 6}
>>> a={1,2,3,5,6}
>>> b=7,8,5,6,1}
SyntaxError: unmatched '}'
>>> a={1,2,3,5,6}b={7,8,5,6,1}
SyntaxError: invalid syntax
>>> a={1,2,3,5,6}
>>> b={7,8,5,6,1}
>>> a
{1, 2, 3, 5, 6}
>>> b
{1, 5, 6, 7, 8}
>>> a.isdisjoint(b)
False
>>> b.disjoint(a)
Traceback (most recent call last):
  File "<pyshell#163>", line 1, in <module>
    b.disjoint(a)
AttributeError: 'set' object has no attribute 'disjoint'. Did you mean: 'isdisjoint'?
>>> b.isdisjoint(a)
False
>>> a
{1, 2, 3, 5, 6}
>>> b
{1, 5, 6, 7, 8}
>>> {8}.issubset(a)
False
>>> {100,99}.issubset(a)
False
>>> False
False
>>> a = {1, 2, 3, 5, 6}
... 
... b = {1, 5, 6, 7, 8}
... 
... print(b.issuperset(a))
SyntaxError: multiple statements found while compiling a single statement
>>> False
... a = {1, 2, 3, 5, 6}
SyntaxError: multiple statements found while compiling a single statement
>>> a = {1, 2, 3, 5, 6}
>>> b = {1, 5, 6, 7, 8}
>>> b.issuperset(a)
False
