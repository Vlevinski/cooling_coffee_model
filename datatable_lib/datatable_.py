#!/usr/bin/python3.7
'''
 Links
 https://github.com/Rdatatable/data.table/wiki
 https://datatable.readthedocs.io/en/latest/using-datatable.html
 https://datatable.readthedocs.io/en/latest/index.html
 https://datatable.readthedocs.io/en/latest/using-datatable.html
 https://www.kaggle.com/sudalairajkumar/getting-started-with-python-datatable
 https://github.com/Rdatatable/data.table/wiki
 https://towardsdatascience.com/an-overview-of-pythons-datatable-package-5d3a97394ee9
                                @vlevinski
'''

import datatable as dt
import numpy as np
#import pandas as pd

class MyDT():
    '''
    DT class as functionality for datatable library
# ===========================
## Datatable commands :
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
    '''

    def __init__(self):
        '''
        Deafaul in csv file
        '''
        self.infile = "in.csv"
        self.outfile = "out.csv"

    def create(self, size=10):
        '''
        create DataTable frame
        :param size:
        :return:
        '''
        return dt.Frame(np.random.randn(size))

    def in_csv(self, file = "in.csv"):
        '''
        read DataTable from csv file
        :param file:  file name
        :return:
        '''
        return dt.fread(file)

    def out_csv(self, frame, file ='out.csv'):
        '''
        write DataTable to csv file
        :param frame:  DataTable frame
        :param file:  csv file name
        :return:
        '''
        return dt.DataTable.to_csv(frame, file)

    def names(self, table):
        '''
        list DataTable names
        :param table:
        :return:
        '''
        return table.names

tb = MyDT()

#read csv filie
t = tb.in_csv(file ='datatable_lib/in.csv') # or t = tb.create
print("DataTable shape", t.shape)

#write csv
tb.out_csv(t,'datatable_lib/out.csv')


