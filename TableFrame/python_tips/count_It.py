#!/usr/bin/python3
#       by @vlevinski

# count Data list string words
data =["python", "java", "C" ,"python", "Ruby", "java","python", "swift", "C++"]
numbers = [ 1,2,3,4,5,6,7,3,8,4,5,3,3,4,2,6,7]

def countIt(data):
    import collections as coll
    return dict(coll.Counter(data))

showIt = lambda data: print(countIt(data))

print (countIt(data))
showIt(numbers)
