class CustomCsv():
    #csv class for data analysis

    def __init__(self):
        self.filename = "example.csv"

    def load(self, name):
        import csv
        # open file as list of dicts
        return list(csv.DictReader(open(name)))

    def first5(self, data):
        # get starting items
        return (data[:5])

    def last5(self, data):
        #get last items
        return data[-5:]

    def item(self, data, idx):
        #get column values
        for k,v in data[idx].items():
            print (k, ':', v)

    def itemline(self, data, idx):
        # print column items
        for k,v in data[idx].items():
            print (k, ':', v, end=", ")
        print ("")

    def select(self, data, column, value):
        #create list of value in slected column
        return [m for m in data if value in m[column]]

    def replace(self, data, column, value, newvalue):
        # clear the value
        return   [{**c, column:c[column].replace(value, newvalue)} for c in data if c[column] == value]

    def empty(self, data, column, value):
        # select the list for concrete value in the column
        return [c[column] for c in data if c[column] == value]

    def counter(self, data, column):
        # count value in column
        from collections import Counter
        return Counter(t[column] for t in data)

    def common(self, data, column, num):
        # list of mnost common int in the column
        from collections import Counter
        lst =  Counter(t[column] for t in data)
        return lst.most_common(num)
