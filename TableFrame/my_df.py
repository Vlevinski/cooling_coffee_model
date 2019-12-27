import pandas as pd

iname = "name1"
ipassword = "password1"
iemail = "email@domain.com"
df = pd.DataFrame([[iname, ipassword, iemail]],columns=['A', 'B', 'C'])
print(df.to_string())
row = [iname, ipassword, iemail]
df.loc[len(df)] = row
print ("==")
print (df.to_string())
