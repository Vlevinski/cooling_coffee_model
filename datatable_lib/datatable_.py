import datatable as dt
import numpy as np

class DT():
    '''
    DT class as functionality and commands taht you can run with datatable lib
    '''

    def __init__(self):
        self.name = ''

    def create(self, size=1000000):
        np.random.seed(1)
        return dt.Frame(np.random.randn(size))

    def createColumn(self, name = "A",size=1000):
        import pandas as pd
        return dt.Frame(pd.DataFrame({name: range(size)}))

    def createJson(self, foo):
        return dt.Frame(foo)

    def out(self, data):
        print (data)

dtn = DT()

#generate data
data =  dtn.create()
dtn.out(data)

#generate from pandas frame
df = dtn.createColumn()
dtn.out(df)

#generate fron json
df = dtn.createJson({"n":[1,2,3],"s":["foo","bar","why"]})
dtn.out(df)
