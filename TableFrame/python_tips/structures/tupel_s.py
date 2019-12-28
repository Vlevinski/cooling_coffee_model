#    heterogeneous immutable sequence
#    Once created, cannot be updated
#    surrounded by parenthesis, rather than brackets

a = (5, 6.54, "United States")
print (type(a))
print (a[1])
print (len(a))

b = (1, 1.25, ("US", "UK"))
print (b[2][0])
c = (a,)
print (c)

a, b = (5, 6)
a, b = b, a

d = [1, 2, 3, 4, 5]
e = tuple(d)
print (tuple('strings'))
