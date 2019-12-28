#!
#  CSV primary ops
#

from collections import Counter, OrderedDict
import csv

#  Read file
data = list(csv.DictReader(open('income.csv')))


# Count values
vals = [float(v['Value']) for v in data]
print ("Counted values:", Counter(vals))


# Calculate values replace empty values if needed
#total = [{**c, 'Total':c['Total'].replace('', '0')} for c in data]   or None
for v in data:
    v['Total'] = round(float(v['Value']) * float(v['Column']),2)
total = [v['Total'] for v in data]
print ("Column sum: ", round(sum(total),2))
