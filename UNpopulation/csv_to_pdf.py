import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("/home/val/PycharmProjects/coolingCoffee/UNpopulation/data/WPP2019_TotalPopulationBySex.csv", encoding = "ISO-8859-1")
mld = data[(data['Location']=='Republic of Moldova') & (data['VarID']==2)]
mld = mld.set_index(['Time'])

del mld['LocID']; del mld['VarID']; del mld['MidPeriod']
mld.plot()
plt.savefig("MDpopulation.png")
plt.show()

