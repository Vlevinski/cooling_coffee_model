# a homogenous immutable sequence of Unicode characters

a = 'A quick brown fox jumps over the lazy dog'
print (len(a))

b ='Quick' + 'Brown' + 'Fox'

c = ' '.join(['Quick', 'Brown', 'Fox'])
d =  'Quick Brown Fox'.split(' ')

e = 'Singapore:New York'.partition(':')
source, separator, destination = 'Singapore:New York'.partition(':')

print ('Its {0} {1} birthday on {1} {2}'.format("Nathan's",'5th', 'November'))
