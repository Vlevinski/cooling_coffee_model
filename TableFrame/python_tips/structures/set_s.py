# An unordered collection of unique, immutable objects
#
#     enclosed by {}
#     use set() to create an empty set
#     a common use is to efficiently remove duplicates


s = {1, 2, 3, 5}
l = [1, 2, 2, 3, 4, 4, 5]
j = set(l)
j.add(6)
j.update([7, 8, 9, 10])
j.remove(1)   # remove with error exception if
j.discard(1)  # remove with no errors
