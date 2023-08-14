import pandas as pd

df=pd.DataFrame({'a':[11,21,31],'b':[21,22,23]})
#print (df.idxmax(0,0))
# print (df.head(3))


df1=pd.DataFrame({'a':[1,2,1],'b':[1,1,1]})

print (df1['a'].unique())
print (df1['a']>=2)

