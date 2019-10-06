#!/usr/bin/python3.7

import pandas as pd
pd.options.display.max_colwidth = 20

filename = "table.csv"

class MyTable():

    def __init__(self):
        '''
        Create pandas Data Frame class
        '''
        self.filename = ""

    def read(self, name=None):
        '''
        get DataFrame from csv file
        '''
        df = pd.read_csv(name)
        self.filename = name
        return df

    def fields(self, df):
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

    def out(self, df,dfNames):
        '''
        print selected columns
        :param df:  Data Frame
        :param dfNames: selected names
        '''
        print (df[dfNames].to_string())
        return True

    def colFunction(self, df, col, f):
        '''
        :param df: DataFrame
        :param col:  column name, string
        :param f:    operation, function
        :return:
        '''
        return df[col].apply(f)

    def multiplyColumns(self, df, col1, col2, col3):
        df[col3] = round(df[col1]* df[col2],2)
        return df

    def colSum(self,df,col):
        '''
        :param df:
        :param col1:
        :param col2:
        :param col3:
        :return:
        '''
        return df[col].sum()

    def colMax(self,df,*args):
        '''
        :param df:
        :param col1:
        :param col2:
        :param col3:
        :return:
        '''
        return df[[*args]].max()

    def colMin(self,df,col):
        return df[col].min()

    def addRowLast(self,df):
        df.loc[len(df)] = None
        return (df)

    def deleteRowLast(self,df,):
        df.drop(df.tail(1).index,inplace=True)   # or last n rows


#declare
mt = MyTable()
#print (help(MyTable))

#load
df = mt.read(name = filename)
print (mt.filename)
fields = mt.fields(df)
rows, columns = mt.info(df)  #rows, columns = mt.info(df)

#report
dfNames = ["#Shares","CurrCost","AUDCost"]
#mt.out(df,dfNames)
mt.out(df,fields)

