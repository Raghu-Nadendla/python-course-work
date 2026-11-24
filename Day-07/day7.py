Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#checkig methods
s="guntur andrapradesh"
s
'guntur andrapradesh'
s.startswith('g')
True
s.startswith('e')
False
s.endswith('h')
True
s.endswith('q')
False
's'.isupper()
False
'U'.isupper()
True
'l'.islower()
True
'N'.islower()
False
s='raghu'
s.isalpha()
True
'1234'.isdigit()
True
'raghu@'. isalpha()
False
'raghu123'.isalnum()
True
'raghu'.istitle()
False
'Raghu'.istitle()
True
#spliting & joiing
'a b c d'.split()
['a', 'b', 'c', 'd']
'raghu'.split()
['raghu']
'raghu'.split('-')
['raghu']
'r,a,g,h,u'.split('*')
['r,a,g,h,u']
s=""""
hello
world
python
"""
s
'"\nhello\nworld\npython\n'
>>> s.splitlines()
['"', 'hello', 'world', 'python']
>>> l=['r','a','g','h','u']
>>> '-'.join(l)
'r-a-g-h-u'
>>> '@'.join(l)
'r@a@g@h@u'
>>> ''.join(l)
'raghu'
>>> s='a-b-c-d'
>>> s.partition('b')
('a-', 'b', '-c-d')
>>> 'python.py'.partition('.')
('python', '.', 'py')
>>> 'pyth.hon.py'.rpartition('.')
('pyth.hon', '.', 'py')
>>> #encode & decode
>>> s="raghu"
>>> s.encode()
b'raghu'
>>> t='hello😀'
>>> t.encode()
b'hello\xf0\x9f\x98\x80'
>>> t.decode()
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    t.decode()
AttributeError: 'str' object has no attribute 'decode'. Did you mean: 'encode'?
>>> # List
>>> l=[1,2,3,4]
>>> l
[1, 2, 3, 4]
>>> type(l)
<class 'list'>
>>> #mut orderd dup het dym
>>> l=[2,2,2,3,3,4,5]
>>> l
[2, 2, 2, 3, 3, 4, 5]
>>> l=[1,1,1,1]
>>> l
[1, 1, 1, 1]
>>> l=[1,2,3,3,3,4,45,6,6,7,3+7j,"str",[1,23],(1,2),{1,23},{1:3},False,None]
>>> l
[1, 2, 3, 3, 3, 4, 45, 6, 6, 7, (3+7j), 'str', [1, 23], (1, 2), {1, 23}, {1: 3}, False, None]
>>> #operatitions
>>> #concatition
[1,2,3,4]+[5,6,7]
[1, 2, 3, 4, 5, 6, 7]
[1,2,3]*5
[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
#indexing
l=['guntur','vij','amaravathi','narasaraopet']
l[0]
'guntur'
l[-1]
'narasaraopet'
l[-4]
'guntur'
l[4]
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    l[4]
IndexError: list index out of range
l[3]
'narasaraopet'
l[2]
'amaravathi'
#slicing
l=['guntur','vij','amaravathi','narasaraopet']
l
['guntur', 'vij', 'amaravathi', 'narasaraopet']
l[:3]
['guntur', 'vij', 'amaravathi']
l[-3:]
['vij', 'amaravathi', 'narasaraopet']
l[2:3]
['amaravathi']
l=[-1:-3]
SyntaxError: invalid syntax
l[::-1]
['narasaraopet', 'amaravathi', 'vij', 'guntur']
l[-2:-4:-1]
['amaravathi', 'vij']
#membership
l=['raghu','raghava']
'raghu' in
SyntaxError: invalid syntax
'raghu' not in
SyntaxError: invalid syntax
l
['raghu', 'raghava']
'raghu' in l
True
'ramesh' not in l
True
#methods
l=['pyhton','java','aws','dsa']
len(l)
4
sorted(l)
['aws', 'dsa', 'java', 'pyhton']
max(l)
'pyhton'
min(l)
'aws'
l=['guntur','vij','amaravathi']
l
['guntur', 'vij', 'amaravathi']
id(l)
2296543319168
l[1]
'vij'
l['amaravathi']
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    l['amaravathi']
TypeError: list indices must be integers or slices, not str
l[1]='narasaropet'
l
['guntur', 'narasaropet', 'amaravathi']
id(l)
2296543319168
l[2]='aws'
l
['guntur', 'narasaropet', 'aws']
id(l)
2296543319168
l.append('d')
l
['guntur', 'narasaropet', 'aws', 'd']
l.extand([1,2,3,4])
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    l.extand([1,2,3,4])
AttributeError: 'list' object has no attribute 'extand'. Did you mean: 'extend'?
l.extend([1,2,3,4)]
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
l.extend([1,2,3,4,5])
l
['guntur', 'narasaropet', 'aws', 'd', 1, 2, 3, 4, 5]
l.insert(2,'a')
l
['guntur', 'narasaropet', 'a', 'aws', 'd', 1, 2, 3, 4, 5]
id(l)
2296543319168
