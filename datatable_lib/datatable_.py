import datatable as dt
import numpy as np

class DT():
    def __init__(self):
        self.name = ''

    def create(self, size=1000000):
        np.random.seed(1)
        return dt.Frame(np.random.randn(size))

    def out(self, data):
        print (data)

dtn = DT()
data =  (dtn.create(size=10))
dtn.out(data)
