import datatable as dt
import numpy as np

class DT():
    '''
    DT class as functionality and commands taht you can run with datatable lib
    '''

    def __init__(self):
        self.name = ''

    def create(self, size=10):
        return dt.Frame(np.random.randn(size))

    def from_csv(self, file = "in.csv"):
        return dt.fread(file)

    def names(self, table):
        return table.names

out = lambda x: print(x)

tb = DT()
table = tb.from_csv()

out(table)
out(table.sum())
#out(data.names)
#out(data.shape)
#out(data.head(1))
#data.sum()      data.nunique()
#data.sd()       data.max()
#data_df.mode()  data_df.min()
#data.nmodal()   data_df.mean()

