# A dictionary — Unordered mapping of unique immutable keys to mutable values.
#
#     Keys must be unique in a dictionary
#     enclosed in {}
#     comma-separated key-value pairs joined by a colon

d = {'Google': 'www.google.com', 'Facebook': 'www.facebook.com'}
print (d['Google'])

#Iterating a dictionary
for k, v in d.items():
    print(f'{k} -> {v}')
