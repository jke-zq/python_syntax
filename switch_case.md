switch－case

python中无switch，主要可以通过dict来代替。
下面介绍几种用法：
1.构造dict + get方法
choices = {'a': (1, 2, 3), 'b': (4, 5, 6)}
(result1, result2, result3) = choices.get(key, ('default1', 'default2', 'default3'))
2.context managers
class Switch:
    def __init__(self, value): self._val = value
    def __enter__(self): return self
    def __exit__(self, type, value, traceback): return False # Allows traceback to occur
    def __call__(self, cond, *mconds): return self._val in (cond,)+mconds

from datetime import datetime
with Switch(datetime.today().weekday()) as case:
    if case(0):
        # Basic usage of switch
        print("I hate mondays so much.")
        # Note there is no break needed here
    elif case(1,2):
        # This switch also supports multiple conditions (in one line)
        print("When is the weekend going to be here?")
    elif case(3,4): print("The weekend is near.")
    else:
        # Default would occur here
        print("Let's go have fun!") # Didn't use case for example purposes
3.构造dict + get方法 ＋ lambda
result = {
  'a': lambda x: x * 5,
  'b': lambda x: x + 7,
  'c': lambda x: x - 2
}
x = 4
lambda_x = result.get(key, None)
return default_value if lambda_x == None else lambda_x(x)

4.其他一些case from：http://code.activestate.com/recipes/langs/python/
Readable switch construction without lambdas or dictionaries：
# This class provides the functionality we want. You only need to look at
# this if you want to know how this works. It only needs to be defined
# once, no need to muck around with its internals.
class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration
    
    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args: # changed for v1.5, see below
            self.fall = True
            return True
        else:
            return False


# The following example is pretty much the exact use-case of a dictionary,
# but is included for its simplicity. Note that you can include statements
# in each suite.
v = 'ten'
for case in switch(v):
    if case('one'):
        print 1
        break
    if case('two'):
        print 2
        break
    if case('ten'):
        print 10
        break
    if case('eleven'):
        print 11
        break
    if case(): # default, could also just omit condition or 'if True'
        print "something else!"
        # No need to break here, it'll stop anyway

# break is used here to look as much like the real thing as possible, but
# elif is generally just as good and more concise.

# Empty suites are considered syntax errors, so intentional fall-throughs
# should contain 'pass'
c = 'z'
for case in switch(c):
    if case('a'): pass # only necessary if the rest of the suite is empty
    if case('b'): pass
    # ...
    if case('y'): pass
    if case('z'):
        print "c is lowercase!"
        break
    if case('A'): pass
    # ...
    if case('Z'):
        print "c is uppercase!"
        break
    if case(): # default
        print "I dunno what c was!"

# As suggested by Pierre Quentel, you can even expand upon the
# functionality of the classic 'case' statement by matching multiple
# cases in a single shot. This greatly benefits operations such as the
# uppercase/lowercase example above:
import string
c = 'A'
for case in switch(c):
    if case(*string.lowercase): # note the * for unpacking as arguments
        print "c is lowercase!"
        break
    if case(*string.uppercase):
        print "c is uppercase!"
        break
    if case('!', '?', '.'): # normal argument passing style also applies
        print "c is a sentence terminator!"
        break
    if case(): # default
        print "I dunno what c was!"

# Since Pierre's suggestion is backward-compatible with the original recipe,
# I have made the necessary modification to allow for the above usage.

Exception-based Switch-Case

import sys

class case_selector(Exception):
   def __init__(self, value): # overridden to ensure we've got a value argument
      Exception.__init__(self, value)

def switch(variable):
   raise case_selector(variable)

def case(value):
   exclass, exobj, tb = sys.exc_info()
   if exclass is case_selector and exobj.args[0] == value: return exclass
   return None

def multicase(*values):
   exclass, exobj, tb = sys.exc_info()
   if exclass is case_selector and exobj.args[0] in values: return exclass
   return None

if __name__ == '__main__':
   print

   def InputNumber():
      while 1:
         try:
            s = raw_input('Enter an integer')
         except KeyboardInterrupt:
            sys.exit()
         try:
            n = int(s)
         except ValueError, msg:
            print msg
         else:
            return n

   while 1:
      n = InputNumber()
      try:
         switch(n)
      except ( case(1), case(2), case(3) ):
         print "You entered a number between 1 and 3"
      except case(4):
         print "You entered 4"
      except case(5):
         print "You entered 5"
      except multicase(6, 7, 8, 9):
         print "You entered a number between 6 and 9"
      except:
         print "Youe entered a number less then 1 or grater then 9"
