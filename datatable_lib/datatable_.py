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

    def out(self, data):
        print (data)

dtn = DT()

#generate data
data =  dtn.create(size=10)
dtn.out(data)

