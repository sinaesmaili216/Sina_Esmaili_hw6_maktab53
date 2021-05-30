li = [1, None, "hi", 55, -9, None, None, 1.1]
remove_none = filter(lambda x: x != None , li)
print(list(remove_none))
