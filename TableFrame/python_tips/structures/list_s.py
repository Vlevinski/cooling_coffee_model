# A mutable collection of ordered items
# Enclosed on squared brackets


l = ['A', 'Quick', 'Brown', 'Fox']
print (l)
print (l[1])
print (l[-1])
print (l[-2])

slice  = l[:3]
print (l[1:3])

full_slice = l[:]
print (full_slice)         #True
print (l is full_slice)    #False

a = [1, 0]
print (a * 4)

print (l.index('Brown'))
del l[1]
l.remove('Quick')
l.insert(1, 'Healthy')

a = [1, 2, 3]
a = a + [4, 5]
a += [4, 5]
a.extend([4, 5])

a = [1, 2, 3]
a.reverse()
a.sort()

l = 'A quick brown box jumps over the lazy dog'.split()
l.sort(key=len)

a = [1, 4,2, 7]
b = sorted(a)
