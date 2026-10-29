Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s='python'
s
'python'
''
''
s
'python'
t='programming'
t
'programming'
s+t
'pythonprogramming'
t*3
'programmingprogrammingprogramming'
s*3
'pythonpythonpython'
'*'*20
'********************'
s='python java sql dsa'
s
'python java sql dsa'
#acess the particular charater
s(1)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    s(1)
TypeError: 'str' object is not callable
s[1]
'y'
s[5]
'n'
s[-3]
'd'
s[-6]
'q'
s[10]
'a'
#sliceling
s='raghu raghava surya teja'
s
'raghu raghava surya teja'
s[0:4]
'ragh'
s[7:9]
'ag'
s[-1:-10]
''
s[-1:-4]
''
s[-1:-3]
''
s[7:9]
'ag'
s[7:9:1]
'ag'
s[-1::-10]
'a h'
s[::-1]
'ajet ayrus avahgar uhgar'
s[-3::-7]
'esar'
s[-6::-11]
'aa'
s[-6::-11:1]
SyntaxError: invalid syntax
s[-6:-11:-1]
'ayrus'
s[-10:-13:-1]
's a'
#membership operations
s='pyhton java c++ sql dsa'
s
'pyhton java c++ sql dsa'
'java' in s
True
'flask' in s
False
'python' in s
False
'my sql' not in s
True
#methods
s='python java dsa sql flask'
s
'python java dsa sql flask'
len(s)
25
ord('a')
97
ord('s)
    
SyntaxError: unterminated string literal (detected at line 1)
ord('s')
    
115
ord('c')
    
99
sorted(s)
    
[' ', ' ', ' ', ' ', 'a', 'a', 'a', 'a', 'd', 'f', 'h', 'j', 'k', 'l', 'l', 'n', 'o', 'p', 'q', 's', 's', 's', 't', 'v', 'y']
min(s)
    
' '
max(s)
    
'y'
chr(10)
    
'\n'
s='andra telangana kerala goa'
    
s
    
'andra telangana kerala goa'
s.upper()
    
'ANDRA TELANGANA KERALA GOA'
s.lower()
    
'andra telangana kerala goa'
s.title()
    
'Andra Telangana Kerala Goa'
s.swapecase()
    
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    s.swapecase()
AttributeError: 'str' object has no attribute 'swapecase'. Did you mean: 'swapcase'?
s.swapcase
    
<built-in method swapcase of str object at 0x0000019DC7470710>
s.swapecase()
    
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    s.swapecase()
AttributeError: 'str' object has no attribute 'swapecase'. Did you mean: 'swapcase'?
s.swapcase()
    
'ANDRA TELANGANA KERALA GOA'
s.capitalize()
    
'Andra telangana kerala goa'
# Fromating Methods
    
s='raghu'
    
s
    
'raghu'
s.center(30,'-')
    
'------------raghu-------------'
s.ljust(30,'-')
    
'raghu-------------------------'
s.r.just(40,'-')
    
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    s.r.just(40,'-')
AttributeError: 'str' object has no attribute 'r'
s.rjust(40,'.')
    
'...................................raghu'

#Finding Methods
    
s='andra telangna kerala chennai'
    
s
    
'andra telangna kerala chennai'
s.find(10)
    
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    s.find(10)
TypeError: must be str, not int
s.find('k')
    
15
s.find('c')
    
22
s.index('t')
    
6
s.index('g')
    
11
s.rfind('r')
    
17
s.find('b')
    
-1
s.count('c')
    
1
s.count('a')
...     
7
>>> #Strip operartor
...     
>>> s='Godavri guntur'
...     
>>> s
...     
'Godavri guntur'
>>> 
... s='       Godavri   guntur          '
...     
>>> s
...     
'       Godavri   guntur          '
>>> s.strip()
...     
'Godavri   guntur'
>>> s.lstrip()
...     
'Godavri   guntur          '
>>> s.rstrip()
...     
'       Godavri   guntur'
>>> #replace method
...     
>>> s='guntur vijawada narasarpoet'
...     
>>> s
...     
'guntur vijawada narasarpoet'
>>> s.replace('a','*')
...     
'guntur vij*w*d* n*r*s*rpoet'
>>> s.maketrans('raghu','12345')
...     
{114: 49, 97: 50, 103: 51, 104: 52, 117: 53}
>>> s.translate(s.maketrans('raghu','12345'))
...     
'35nt51 vij2w2d2 n212s21poet'
>>> s.translate(s.maketrans('aeiou','&'))
...     
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    s.translate(s.maketrans('aeiou','&'))
ValueError: the first two maketrans arguments must have equal length
