import pandas as pd
df = pd.DataFrame([[2,3],[3,2]],columns=['A', 'B'])
#print (df)
#print (df.columns)
doIt = lambda x: x*2
print (df[['A','B']].apply(doIt))
