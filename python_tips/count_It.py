# count Data list string words
data =["python", "java", "C" ,"python", "Ruby", "java","python", "swift", "C++"]

def countIt(data):
    import collections as coll
    return coll.Counter(data)

print (countIt(data))
