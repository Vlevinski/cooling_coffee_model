#!/usr/bin/python3.8
#               @vlevinski
#

#from googlesearch import search
try:
    from googlesearch import search
except ImportError:
    print ( " no module named 'google' found")

for url in search('"Breaking Code" WordPress blog', stop=5):
    print(url)
