#!python3.7
#       Demo example 2


from csv_methods.data import CustomCsv

file_name = "data/example.csv"

# get data from file
mc = CustomCsv()
data = mc.load(file_name)

# print oata
print(mc.first5(data))
print(mc.last5(data))
mc.item(data, 4)
mc.itemline(data, 4)
cm = mc.select(data, 'first_name', 'Lydie')
print(cm, len(cm))
print(mc.replace(cm, 'email', '', 'Empty'))
lst = mc.counter(data, 'first_name')
print(dict(lst.most_common(3)))
print("Empty values: ", len(mc.empty(data, 'email', '')))
