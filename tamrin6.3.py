from functools import reduce
li = [1 , 55 , 10 , -9 , 105]

print(reduce(lambda x,y: max(x,y) , li))
print(reduce(lambda x,y: min(x,y) , li))