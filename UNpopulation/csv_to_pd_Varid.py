import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data/WPP2019_TotalPopulationBySex.csv", encoding = "ISO-8859-1")
mld = data[(data['Location']=='Republic of Moldova')] # & (data['VarID']==2)]
mld = mld.set_index(['Time'])
#data.reset_index()
print (mld[0:5])

#i = 2; j = 3
#print("#1", data.loc[i:j,['VarID','Variant']])
#print("#1", mld.loc[:,['VarID','Variant']])
#print (len(data))
varid = []
variant={}

print ('#999')

for i in mld.items():
    print (i)

exit(999)


#    varid.append[i]
#    variant.append[ data.loc[i,'Variant']]
#varid = [i for i in data['VarID']]
print( len(varid), len(variant))

varid = list(set(varid))
print(varid)
print(len(varid))

'''
variant = [i for i in mld['Variant']]
variant = list(set(variant))
print (variant)
print (mld[0:5].to_string())
'''
#my_dict ={}
#my_keys= []

#for k,v in mld[0].items():
#    print (k,v)
#print( mld.loc[0,"VarID"], mld.loc[0,"Variant"])
'''
for row in mld.items():
    print (row)
    k = row["VarID"]
    v = row['Variant']
    if k not in my_keys:
        my_keys.append(k)
        my_dict[k] = v

print (len(my_keys),len(my_dict))
print (my_keys)
print (my_dict)'''
#mld = mld.set_index(['Time'])

#del mld['LocID']; del mld['VarID']; del mld['MidPeriod']
#mld.plot()
#plt.savefig("MDpopulation.png")
#plt.show()
