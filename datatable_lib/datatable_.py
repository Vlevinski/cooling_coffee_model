import datatable as dt
import numpy as np
import pandas as pd

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

    def to_csv(self, file = 'out.csv'):
        return pd.to_csv()

    def names(self, table):
        return table.names

out = lambda x: print(x)

tb = DT()
t = tb.from_csv(file ='datatable_lib/in.csv') # or t = tb.create
out(t)
out(type(t))
t.to_csv('datatable_lib/out.csv')

#tpd = t.to_pandas()
#out(type(tpd))


## statistics
#out(t.names)
#out(t.shape)
#out(t.head(1))

## more dt methods
#data.sum()      data.nunique()
#data.sd()       data.max()
#data_df.mode()  data_df.min()
#data.nmodal()   data_df.mean()

## selecting rows/columns
#t[:,'column']
#t[:,:]

## sorting
#t.sort['column']

## deleting rows/columns
#del t[:,'column']

## groupby
#f stands for frame proxy, and provides a simple way to refer to the Frame that we are currently operating upon.
#for i in range(100):
#    datatable_df[:, dt.sum(dt.f.funded_amnt), dt.by(dt.f.grade)]

##filtering rows
#datatable_df[dt.f.loan_amnt>dt.f.funded_amnt,"loan_amnt"]

#Saving the Frame
#datatable_df.to_csv('output.csv')

# more links
# https://github.com/Rdatatable/data.table/wiki
# https://datatable.readthedocs.io/en/latest/using-datatable.html
# https://datatable.readthedocs.io/en/latest/index.html
# https://datatable.readthedocs.io/en/latest/using-datatable.html
# https://www.kaggle.com/sudalairajkumar/getting-started-with-python-datatable
