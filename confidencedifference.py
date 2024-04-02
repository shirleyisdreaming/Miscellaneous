import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from matplotlib.colors import TwoSlopeNorm

df=pd.read_csv("/Users/xiaoxu.guo/Desktop/400/tr/Layer1/MicrostructureText_Layer1.mic",skiprows=[0,1,2],sep='\t')
df.rename(columns={'%OrientationRowNr':'OrientationRowNr'},inplace=True)
df2=pd.read_csv("/Users/xiaoxu.guo/Desktop/400/denoise/MicrostructureText_Layer1_400.mic",skiprows=[0,1,2],sep='\t')
df2.rename(columns={'%OrientationRowNr':'OrientationRowNr'},inplace=True)
df_noise=df[['X','Y','Confidence']]
df_denoise=df2[['X','Y','Confidence']]
meantr=df['Confidence'].mean()
meandenoise=df2['Confidence'].mean()
print((meandenoise-meantr)/meantr)
df3=pd.merge(df_noise,df_denoise,on=['X','Y'])
df3.rename(columns={'Confidence_x':'Confidence_noise','Confidence_y':'Confidence_denoise'},inplace=True)
df3['Confidence_difference']=df3['Confidence_denoise']-df3['Confidence_noise']
df4=df3[['X','Y','Confidence_difference']]

mean=df4['Confidence_difference'].mean()
print(mean)

df4.to_csv('Confidence_Difference.txt',index=False)

npdf4=df4.to_numpy()
X=npdf4[:,0:1]
Y=npdf4[:,1:2]
Confidence_difference=npdf4[:,2:3]
#Confidence_difference=Confidence_difference.reshape(400,400)

norm = TwoSlopeNorm(vmin=-0.2, vcenter=0.0,  vmax=0.2)

#plt.imshow(Confidence_difference,cmap='bwr',norm=norm)
#plt.scatter(X,Y,c=Confidence_difference,norm=norm,cmap="jet",s=0.1)
plt.scatter(X,Y,c=Confidence_difference,norm=norm,cmap="RdGy",s=0.1)
plt.colorbar()
plt.show()

