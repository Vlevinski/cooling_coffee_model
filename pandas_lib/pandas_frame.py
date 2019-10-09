import pandas as pd
import numpy as np

class DF():
    '''
    DF class as functionality and commands that you can run with pandas lib
    '''

    def __init__(self):
        self.name = ''

    def create(self, size=1000000):
        '''

        :param size:  DataFrame size
        :return:
        '''
        np.random.seed(1)
        return pd.DataFrame(np.random.randn(size))

    def out(self, data):
        '''
        print out data DataFrame
        :param data:
        :return:
        '''
        print (data)

    def round(self,df, dec=2):
        '''
        round to dec decimals df DataFrame
        :param df:
        :param dec:
        :return:
        '''
        df.iloc[:,0]= round(df.iloc[:,0], dec)

df = DF()

#generate data
data =  df.create()
df.out(data)
df.out(data.iloc[0,0])

#round data to 2 decimals
df.round(data)
df.out(data)
df.out(data.iloc[0,0])
