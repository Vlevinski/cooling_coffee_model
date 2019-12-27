#!/usr/bin/python3.7
#

import pandas as pd
import matplotlib.pyplot as plt

## create Data Drame by reading *.csv file see the link: https://population.un.org/wpp/Download/Standard/CSV/
data = pd.read_csv("data/WPP2019_TotalPopulationBySex.csv", encoding = "ISO-8859-1")

## filter Data Frame for selected "Location' and "Medium" forecat. Print and clear the Data Frame columns
mld = data[(data['Location']=='Republic of Moldova') & (data['VarID']==2)]
mld = mld.set_index(['Time'])
print(data.loc[0:3,['VarID','Variant']])
del mld['LocID']; del mld['VarID']; del mld['MidPeriod']

## plot graphic of selcted data with matplotlib library
mld.plot()                        # simple plot

#plt.savefig("MDpopulation.png")  # save plot data in the case you need, uncomment intruction
plt.show()

