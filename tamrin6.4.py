from functools import reduce

class InvalidInput(Exception):
    def __init__(self, massage):
        self.massage = massage


def fibonacci_generator(n1, n2):
    if n1 < 1 or n2 < 1:
        try:
            raise InvalidInput('Invalid input')
        except:
            try:
                raise InvalidInput('Invalid input')
            except InvalidInput as e:
                print(e.massage)
    else:
        fib = lambda n: reduce(lambda x: x+[x[-1]+x[-2]], range(n-2), [0,1])
        f0, f1 = fib(n1)[-1], fib(n1+1)[-1]
        for i in range(n1, n2):
            yield f0
            f0, f1 = f1, f0+f1

for i in fibonacci_generator(1,10):
    print(i)
