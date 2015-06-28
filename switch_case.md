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