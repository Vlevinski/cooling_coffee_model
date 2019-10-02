#!/usr/bin/python3.7

import pandas as pd
pd.options.display.max_colwidth = 20

filename = "table.csv"

class MyTable():

    def __init__(self):
        '''
        Create pandas Data Frame class
        '''
        self.filename= ""

    def read(self, name = None):
        '''
        get DataFrame from csv file
        '''
        df = pd.read_csv(name)
        self.filename = name
        return df

    def fields(self,df):
        '''
        get fields names
        '''
        return list(df.columns)

    def info(self, df):
        '''
        gen Table info
        '''
        print ("Data shape: ", df.shape )
        print ("Fields number: ", len(fields))
        return df.shape


mt = MyTable()
print (help(MyTable))

df = mt.read(name = filename)
fields = mt.fields(df)
rows, columns = mt.info(df)
