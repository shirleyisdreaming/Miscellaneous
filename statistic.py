import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



df=pd.read_table(r'/Users/xiaoxu.guo/Desktop/LSHRparaview/Traditional/npgrainsize.txt')

 
dfn2v=pd.read_table(r'/Users/xiaoxu.guo/Desktop/LSHRparaview/n2v/npgrainsize.txt')

df_last=df.sort_values('Traditional')
dfn2v_last=dfn2v.sort_values('N2V')

def get_size_bin(Traditional):
 #if Traditional>=1000:
#return '>=1000'
#elif Traditional>=900:
#return '900-1000'
#elif Traditional>=800:
#return '800-900'
#elif Traditional>=700:
#return '700-800'
#elif Traditional>=600:
#return '600-700'
 if Traditional>=500:
  return '>=500'
 elif Traditional>=400:
  return '400-500'
 elif Traditional>=300:
  return '300-400'
 elif Traditional>=200:
  return '200-300'
 elif Traditional>=100:
  return '100-200'
 elif Traditional>=50:
  return '50-100'
 elif Traditional>=40:
  return '40-50'
 elif Traditional>=30:
  return '30-40'
 elif Traditional>=20:
  return '20-30'
 elif Traditional>=10:
  return '10-20'
 elif Traditional>=0:
  return '0-10'
  
  
df_last['grain size level']=df_last['Traditional'].apply(lambda Traditional:get_size_bin(Traditional))
dfn2v_last['grain size level']=dfn2v_last['N2V'].apply(lambda Traditional:get_size_bin(Traditional))
df_last_new=df_last.groupby('grain size level').count()
dfn2v_last_new=dfn2v_last.groupby('grain size level').count()
print(df_last_new)
print(dfn2v_last_new)

df_all= pd.merge(dfn2v_last_new, df_last_new, how='left', on='grain size level')
df_all['Difference']=df_all['N2V']-df_all['Traditional']



print(df_all)
#ax=df.plot.hist(bins=,alpha=0.5)
#dfn2v.plot.hist(bins=15,alpha=0.5,ax=ax)


#ax.set_xlabel('Grain Size Range')
#ax.set_ylabel('Difference of Number of Grain')
#plt.show()

