#if __name__ == 'main':
There is nothing special about if __name__ == '__main__' block whatsoever. That is to say, its scope is determined by the place it occurs. Since such blocks typically occur at top-level, their scope is global.
If this block were to occur in a function, which is perfectly legal, its scope would be local—except that __name__ would still resolve to the global value defined in the module.

Example 1:
>>> if __name__ == '__main__':
...     x = 1
... print 'x' in globals()
True
edit: user4815162342 makes the excellent point that this if-statement can be written in any scope. It's most often written in the global scope.

Here it is inside a function:

>>> def foo():
...     if __name__ == '__main__':
...         bar = 1
... foo()
... print 'bar' in globals()
False

Example 2:
localhost:python_syntax zhaoqing$ python test.py
test.py:9: SyntaxWarning: name 'session' is assigned to before global declaration
  global session
localhost:python_syntax zhaoqing$ cat test.py

session = None

if __name__ == 'main':
    global session
    session = 'new session'
    print session