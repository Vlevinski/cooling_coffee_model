#!/usr/bin/python3.8
#               @vlevinski
#
# Get the first 20 hits for: "Breaking Code" WordPress blog
#       https://github.com/MarioVilas/googlesearch
#       https://python-googlesearch.readthedocs.io/en/latest/   Doc's
#from googlesearch import search
try:
    from googlesearch import search
except ImportError:
    print ( " no module named 'google' found")

for url in search('"Breaking Code" WordPress blog', stop=5):
    print(url)
