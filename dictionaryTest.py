
#Different kinds of dictionary initialization
a = dict(one = 1, two = 2, three = 3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})

#Check for equality
print (a == b == c == d == e)
