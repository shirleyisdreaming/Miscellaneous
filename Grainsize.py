import numpy as np

 
 
gn=np.fromfile("/Users/xiaoxu.guo/Desktop/test/GrainSizes.bin",dtype=np.int32)
newgn=[]

eu=np.fromfile("/Users/xiaoxu.guo/Desktop/test/EulerAngles1.bin",dtype=float)
print(min(eu))
print(eu.shape)
n=0
for i in range(160000):
 if eu[i]==-15.0:
  n=n+1
print(n)

for i in gn:
 if i >=0:
  newgn.append(i)
  
gid=np.fromfile("/Users/xiaoxu.guo/Desktop/test/GrainNrs.bin",dtype=np.int32)
newgid=[]
nan=[]
for i in gid:
 if i >=0:
  newgid.append(i)
 else:
  nan.append(i)

npgid=np.asarray(gid)
#print(npgid.shape)


nan=np.asarray(nan)
print(nan.shape)


npnewgid=np.asarray(newgid)
npnewgn=np.asarray(newgn)
npnewgidunique=np.unique(npnewgid)
#print(npnewgid.shape)
indexgid=[]


'''

for i in npnewgidunique:
 indexgid.append(np.where(npnewgid==i)[0][0])
npindexgid=np.asarray(indexgid)
grainsize=[]
for i in npindexgid:
 grainsize.append(npnewgn[i])
npgrainsize=np.asarray(grainsize)
print("median:",np.median(grainsize)," ", "mean:",np.mean(grainsize)," ","average:",np.average(grainsize)," ","std:",np.std(grainsize))
np.savetxt("/Users/xiaoxu.guo/Desktop/LSHRparaview/Traditional/npgrainsize.txt",npgrainsize,delimiter=' ',fmt='%d')

'''
