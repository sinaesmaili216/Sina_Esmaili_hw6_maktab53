from functools import reduce
import math

def mysum(*args):
    li = [i for i in args if isinstance(i, int)]
    li = map(lambda x: math.sqrt(x), li)
    res = reduce(lambda x, y: x+y, li)
    return math.ceil(res)

print(mysum(2, 68, 9, 0, 13))

