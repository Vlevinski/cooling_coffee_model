#!python3.7


from collections import Counter
from csv_methods.data import CustomCsv

#  Read file
cs = CustomCsv()
data = cs.load("data/income.csv")

# Count values
vals = [float(v['Value']) for v in data]
print("Counted values:", Counter(vals))

# Replace empty values if needed
# total = [{**c, 'Total':c['Total'].replace('', '0')} for c in data]   or None

# Calculate the sum
for v in data:
    v['Total'] = round(float(v['Value']) * float(v['Column']), 2)
total = [v['Total'] for v in data]
print("Column sum: ", round(sum(total), 2))
