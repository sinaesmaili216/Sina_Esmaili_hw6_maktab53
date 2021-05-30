class MyCustomerror(Exception):
    def __init__(self, massage):
        self.massage = massage

def checktype(t):
    def wrraper1(func):
        def wrraper2(arg):
            if not isinstance(arg, t):
                raise MyCustomerror('your type is not valid!')
            else:
                return arg
        return wrraper2
    return wrraper1


@checktype(int)
def func(n):
    print(n)

print(func(3))
#print(func('sina'))