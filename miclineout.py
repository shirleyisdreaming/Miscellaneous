import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



data=np.fromfile("/Users/xiaoxu.guo/Desktop/LSHRparaview/grain_size_diff.txt",dtype=float,sep=" ")

data_tr=[]
data_n2v=[]
data_tr_tot=np.zeros(6)

data_diff_incr=np.zeros(6)
data_diff_same=np.zeros(6)
data_diff_decr=np.zeros(6)
data_diff_mean=np.zeros(6)
data_diff_mean_in=np.zeros(6)
data_diff_mean_de=np.zeros(6)


print(len(data))
for i in range(len(data)):
 #if i%3==0:
  #print(i)
  #data_diff.append(data[i])
  #print(data_diff)
 if i%3==1:
  data_tr.append(data[i])
 if i%3==2:
  data_n2v.append(data[i])

data_diff=np.zeros(len(data_tr))
for i in range(len(data_tr)):
   data_tr[i]=2*np.sqrt(0.3849*data_tr[i]*7.79422/2)
   data_n2v[i]=2*np.sqrt(0.3849*data_n2v[i]*7.79422/2)
   data_diff[i]=data_n2v[i]-data_tr[i]

#print(data_tr)
#print(len(data_diff))
'''
for i in range(len(data_diff)):
  if data_tr[i]>=0 and data_tr[i]<3:
   j=0
   data_tr_tot[j]=data_tr_tot[j]+1
   data_diff_mean[j]=data_diff_mean[j]+data_diff[i]
   if data_diff[i]>0:
    data_diff_incr[j]=data_diff_incr[j]+1
    data_diff_mean_in[j]=data_diff_mean_in[j]+data_diff[i]
   if data_diff[i]<0:
    data_diff_decr[j]=data_diff_decr[j]+1
    data_diff_mean_de[j]=data_diff_mean_de[j]+data_diff[i]
   if data_diff[i]==0:
    data_diff_same[j]=data_diff_same[j]+1
  elif data_tr[i]>=3 and data_tr[i]<6:
   j=1
   data_tr_tot[j]=data_tr_tot[j]+1
   data_diff_mean[j]=data_diff_mean[j]+data_diff[i]
   if data_diff[i]>0:
    data_diff_incr[j]=data_diff_incr[j]+1
    data_diff_mean_in[j]=data_diff_mean_in[j]+data_diff[i]
   if data_diff[i]<0:
    data_diff_decr[j]=data_diff_decr[j]+1
    data_diff_mean_de[j]=data_diff_mean_de[j]+data_diff[i]
   if data_diff[i]==0:
    data_diff_same[j]=data_diff_same[j]+1
  elif data_tr[i]>=6 and data_tr[i]<9:
   j=2
   data_tr_tot[j]=data_tr_tot[j]+1
   data_diff_mean[j]=data_diff_mean[j]+data_diff[i]
   if data_diff[i]>0:
    data_diff_incr[j]=data_diff_incr[j]+1
    data_diff_mean_in[j]=data_diff_mean_in[j]+data_diff[i]
   if data_diff[i]<0:
    data_diff_decr[j]=data_diff_decr[j]+1
    data_diff_mean_de[j]=data_diff_mean_de[j]+data_diff[i]
   if data_diff[i]==0:
    data_diff_same[j]=data_diff_same[j]+1
  elif data_tr[i]>=9 and data_tr[i]<12:
   j=3
   data_tr_tot[j]=data_tr_tot[j]+1
   data_diff_mean[j]=data_diff_mean[j]+data_diff[i]
   if data_diff[i]>0:
    data_diff_incr[j]=data_diff_incr[j]+1
    data_diff_mean_in[j]=data_diff_mean_in[j]+data_diff[i]
   if data_diff[i]<0:
    data_diff_decr[j]=data_diff_decr[j]+1
    data_diff_mean_de[j]=data_diff_mean_de[j]+data_diff[i]
   if data_diff[i]==0:
    data_diff_same[j]=data_diff_same[j]+1
  elif data_tr[i]>=12 and data_tr[i]<15:
   j=4
   data_tr_tot[j]=data_tr_tot[j]+1
   data_diff_mean[j]=data_diff_mean[j]+data_diff[i]
   if data_diff[i]>0:
    data_diff_incr[j]=data_diff_incr[j]+1
    data_diff_mean_in[j]=data_diff_mean_in[j]+data_diff[i]
   if data_diff[i]<0:
    data_diff_decr[j]=data_diff_decr[j]+1
    data_diff_mean_de[j]=data_diff_mean_de[j]+data_diff[i]
    
   if data_diff[i]==0:
    data_diff_same[j]=data_diff_same[j]+1
  elif data_tr[i]>=15 and data_tr[i]<18:
   j=5
   data_tr_tot[j]=data_tr_tot[j]+1
   data_diff_mean[j]=data_diff_mean[j]+data_diff[i]
   if data_diff[i]>0:
    data_diff_incr[j]=data_diff_incr[j]+1
    data_diff_mean_in[j]=data_diff_mean_in[j]+data_diff[i]
   if data_diff[i]<0:
    data_diff_decr[j]=data_diff_decr[j]+1
    data_diff_mean_de[j]=data_diff_mean_de[j]+data_diff[i]
   if data_diff[i]==0:
    data_diff_same[j]=data_diff_same[j]+1
  elif data_tr[i]>=18 and data_tr[i]<21:
   j=6
   data_tr_tot[j]=data_tr_tot[j]+1
   data_diff_mean[j]=data_diff_mean[j]+data_diff[i]
   if data_diff[i]>0:
    data_diff_incr[j]=data_diff_incr[j]+1
    data_diff_mean_in[j]=data_diff_mean_in[j]+data_diff[i]
   if data_diff[i]<0:
    data_diff_decr[j]=data_diff_decr[j]+1
    data_diff_mean_de[j]=data_diff_mean_de[j]+data_diff[i]
    
   if data_diff[i]==0:
    data_diff_same[j]=data_diff_same[j]+1
  elif data_tr[i]>=21 and data_tr[i]<24:
   j=7
   data_tr_tot[j]=data_tr_tot[j]+1
   if data_diff[i]>0:
    data_diff_incr[j]=data_diff_incr[j]+1
    data_diff_mean_in[j]=data_diff_mean_in[j]+data_diff[i]
   if data_diff[i]<0:
    data_diff_decr[j]=data_diff_decr[j]+1
    data_diff_mean_de[j]=data_diff_mean_de[j]+data_diff[i]
    
   if data_diff[i]==0:
    data_diff_same[j]=data_diff_same[j]+1
  elif data_tr[i]>=24 and data_tr[i]<27:
   j=8
   data_tr_tot[j]=data_tr_tot[j]+1
   data_diff_mean[j]=data_diff_mean[j]+data_diff[i]
   if data_diff[i]>0:
    data_diff_incr[j]=data_diff_incr[j]+1
    data_diff_mean_in[j]=data_diff_mean_in[j]+data_diff[i]
   if data_diff[i]<0:
    data_diff_decr[j]=data_diff_decr[j]+1
    data_diff_mean_de[j]=data_diff_mean_de[j]+data_diff[i]
    
   if data_diff[i]==0:
    data_diff_same[j]=data_diff_same[j]+1
  elif data_tr[i]>=27 and data_tr[i]<30:
   j=9
   data_tr_tot[j]=data_tr_tot[j]+1
   data_diff_mean[j]=data_diff_mean[j]+data_diff[i]
   if data_diff[i]>0:
    data_diff_incr[j]=data_diff_incr[j]+1
    data_diff_mean_in[j]=data_diff_mean_in[j]+data_diff[i]
   if data_diff[i]<0:
    data_diff_decr[j]=data_diff_decr[j]+1
    data_diff_mean_de[j]=data_diff_mean_de[j]+data_diff[i]
    
   if data_diff[i]==0:
    data_diff_same[j]=data_diff_same[j]+1
  #elif data_tr[i]>=500:
  # j=10
  # data_tr_tot[j]=data_tr_tot[j]+1
  # if data_diff[i]>0:
   # data_diff_incr[j]=data_diff_incr[j]+1
  # if data_diff[i]<0:
  #  data_diff_decr[j]=data_diff_decr[j]+1
  # if data_diff[i]==0:
   # data_diff_same[j]=data_diff_same[j]+1
'''

for i in range(len(data_diff)):
  if data_tr[i]>=0 and data_tr[i]<10:
   j=0
   data_tr_tot[j]=data_tr_tot[j]+1
   data_diff_mean[j]=data_diff_mean[j]+data_diff[i]
   if data_diff[i]>0:
    data_diff_incr[j]=data_diff_incr[j]+1
    data_diff_mean_in[j]=data_diff_mean_in[j]+data_diff[i]
   if data_diff[i]<0:
    data_diff_decr[j]=data_diff_decr[j]+1
    data_diff_mean_de[j]=data_diff_mean_de[j]+data_diff[i]
   if data_diff[i]==0:
    data_diff_same[j]=data_diff_same[j]+1
  elif data_tr[i]>=10 and data_tr[i]<20:
   j=1
   data_tr_tot[j]=data_tr_tot[j]+1
   data_diff_mean[j]=data_diff_mean[j]+data_diff[i]
   if data_diff[i]>0:
    data_diff_incr[j]=data_diff_incr[j]+1
    data_diff_mean_in[j]=data_diff_mean_in[j]+data_diff[i]
   if data_diff[i]<0:
    data_diff_decr[j]=data_diff_decr[j]+1
    data_diff_mean_de[j]=data_diff_mean_de[j]+data_diff[i]
   if data_diff[i]==0:
    data_diff_same[j]=data_diff_same[j]+1
  elif data_tr[i]>=20 and data_tr[i]<30:
   j=2
   data_tr_tot[j]=data_tr_tot[j]+1
   data_diff_mean[j]=data_diff_mean[j]+data_diff[i]
   if data_diff[i]>0:
    data_diff_incr[j]=data_diff_incr[j]+1
    data_diff_mean_in[j]=data_diff_mean_in[j]+data_diff[i]
   if data_diff[i]<0:
    data_diff_decr[j]=data_diff_decr[j]+1
    data_diff_mean_de[j]=data_diff_mean_de[j]+data_diff[i]
   if data_diff[i]==0:
    data_diff_same[j]=data_diff_same[j]+1
  elif data_tr[i]>=30 and data_tr[i]<40:
   j=3
   data_tr_tot[j]=data_tr_tot[j]+1
   data_diff_mean[j]=data_diff_mean[j]+data_diff[i]
   if data_diff[i]>0:
    data_diff_incr[j]=data_diff_incr[j]+1
    data_diff_mean_in[j]=data_diff_mean_in[j]+data_diff[i]
   if data_diff[i]<0:
    data_diff_decr[j]=data_diff_decr[j]+1
    data_diff_mean_de[j]=data_diff_mean_de[j]+data_diff[i]
   if data_diff[i]==0:
    data_diff_same[j]=data_diff_same[j]+1
  elif data_tr[i]>=40 and data_tr[i]<50:
   j=4
   data_tr_tot[j]=data_tr_tot[j]+1
   data_diff_mean[j]=data_diff_mean[j]+data_diff[i]
   if data_diff[i]>0:
    data_diff_incr[j]=data_diff_incr[j]+1
    data_diff_mean_in[j]=data_diff_mean_in[j]+data_diff[i]
   if data_diff[i]<0:
    data_diff_decr[j]=data_diff_decr[j]+1
    data_diff_mean_de[j]=data_diff_mean_de[j]+data_diff[i]
    
   if data_diff[i]==0:
    data_diff_same[j]=data_diff_same[j]+1
  elif data_tr[i]>=50 and data_tr[i]<60:
   j=5
   data_tr_tot[j]=data_tr_tot[j]+1
   data_diff_mean[j]=data_diff_mean[j]+data_diff[i]
   if data_diff[i]>0:
    data_diff_incr[j]=data_diff_incr[j]+1
    data_diff_mean_in[j]=data_diff_mean_in[j]+data_diff[i]
   if data_diff[i]<0:
    data_diff_decr[j]=data_diff_decr[j]+1
    data_diff_mean_de[j]=data_diff_mean_de[j]+data_diff[i]
    
   if data_diff[i]==0:
    data_diff_same[j]=data_diff_same[j]+1
    
  




print(data_diff_incr)
print(data_diff_decr)
print(data_diff_same)

for i in range(6):
 if(data_tr_tot[i]!=0):
  data_diff_mean[i]=data_diff_mean[i]/data_tr_tot[i]
 if(data_diff_incr[i]!=0):
  data_diff_mean_in[i]=data_diff_mean_in[i]/data_diff_incr[i]
 if(data_diff_decr[i]!=0):
  data_diff_mean_de[i]=data_diff_mean_de[i]/data_diff_decr[i]
 
x=np.arange(6)
labels=['0-10','10-20','20-30','30-40','40-50','50-60']

#x=np.arange(8)
#labels=['15-30','30-60','60-90','90-120','120-150','150-300','300-600','600-900']


'''
plt.bar(x,data_diff_same,width=0.2,label='size remained same',color='gainsboro')
for a, b in zip(x,data_diff_same):
 plt.text(a,b,int(b),ha='center',va='bottom',fontsize=8)

plt.bar(x+0.2,data_diff_incr,width=0.2,tick_label=labels,label='size increased by N2V',color='red')
for a, b in zip(x,data_diff_incr):
 plt.text(a+0.2,b,int(b),ha='center',va='bottom',fontsize=8)
 
 
plt.bar(x+0.4,data_diff_decr,width=0.2,label='size decreased by N2V',color='blue')
for a, b in zip(x,data_diff_decr):
 plt.text(a+0.4,b,int(b),ha='center',va='bottom',fontsize=8)
 
 
plt.xlabel('Range of the grain size in \u03bcm reconstructed by traditional routine')
plt.ylabel('Number of Grains')


plt.legend()
plt.show()

'''
#ax2=plt.twinx()
plt.xticks(x,labels)
plt.ylabel('Mean changed size in \u03bcm')
plt.plot(x,data_diff_mean[0:6],marker='.',c='g',ms=5,linewidth='1',label='Mean changed size of the total grains')
for a, b in zip(x,data_diff_mean[0:6]):
 plt.text(a,b,round(b,2),ha='center',va='top',fontsize=8)


plt.plot(x,data_diff_mean_in[0:6],marker='.',c='r',ms=5,linewidth='1',label='Mean increased size of the increased grains')
for a, b in zip(x,data_diff_mean_in[0:6]):
 plt.text(a,b,round(b,2),ha='center',va='top',fontsize=8)


plt.plot(x,data_diff_mean_de[0:6],marker='.',c='b',ms=5,linewidth='1',label='Mean decreased size of the decreased grains')


for a, b in zip(x,data_diff_mean_de[0:6]):
 plt.text(a,b,round(b,2),ha='center',va='top',fontsize=8)

plt.xlabel('Range of the grain size in \u03bcm reconstructed by traditional routine')
plt.legend()
plt.show()


