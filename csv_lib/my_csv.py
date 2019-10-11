import csv

fname = "example.csv"

class MyCsv():
    '''
    csv class for data analysis
    '''

    def __init__(self):
        self.filename = ''

    def load(self, name):
        '''
        read csv file
        :param name:  csv file name
        :return:   list of Dict reader rows
        '''
        self.filename = name
        return list(csv.DictReader(open(name)))

    def first5(self, data):
        return (data[:5])

    def last5(self, data):
        return data[-5:]

    def item(self, data, idx):
        for k,v in data[idx].items():
            print (k, ':', v)

    def itemline(self, data, idx):
        for k,v in data[idx].items():
            print (k, ':', v, end=", ")
        print ("")

    def select(self, data, column, value):
        return [m for m in data if value in m[column]]

    def replace(self, data, column, value, newvalue):
        return   [{**c, column:c[column].replace(value, newvalue)} for c in data if c[column] == value]

    def counter(self, data, column):
        from collections import Counter
        return Counter(t[column] for t in data)

    def common(self, data, column, num):
        from collections import Counter
        lst =  Counter(t[column] for t in data)
        return lst.most_common(num)

# class inheritance
mc = MyCsv()
data = mc.load(fname)

# get head and tail 5 rows
print (mc.first5(data))
print (mc.last5(data))

# print items of the idx row of data
mc.item(data, 5)
mc.itemline(data, 5)

# select rows
cm = mc.select(data,'first_name', 'Lydie')
print (len(cm))

# replace column value
cmi = mc.replace(cm,'email', '','NULL')
print (cmi)

# count columns of csv file
lst = mc.counter(data,'first_name')
print (dict(lst.most_common(3)))
