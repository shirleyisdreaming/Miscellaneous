from math import sin, cos, acos, sqrt
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
rad2deg = 57.2957795130823

TricSym=[[1.00000,0.00000,0.00000,0.00000],[1.00000,0.00000,0.00000,0.00000]];
MonoSym=[[1.00000,0.00000,0.00000,0.00000],[0.00000,1.00000,0.00000,0.00000]];
OrtSym=[[1.00000,0.00000,0.00000,0.00000],[1.00000,1.00000,0.00000,0.00000],
		[0.00000,0.00000,1.00000,0.00000],[0.00000,0.00000,0.00000,1.00000]];
TetSym=[[1.00000,0.00000,0.00000,0.00000],[0.70711,0.00000,0.00000,0.70711],
		[0.00000,0.00000,0.00000,1.00000],[0.70711,-0.00000,-0.00000,-0.70711],
		[0.00000,1.00000,0.00000,0.00000],[0.00000,0.00000,1.00000,0.00000],
		[0.00000,0.70711,0.70711,0.00000],[0.00000,-0.70711,0.70711,0.00000]];
TrigSym=[[1.00000,0.00000,0.00000,0.00000],[0.50000,0.00000,0.00000,0.86603],
		[0.50000,-0.00000,-0.00000,-0.86603],[0.00000,0.50000,-0.86603,0.00000],
		[0.00000,1.00000,0.00000,0.00000],[0.00000,0.50000,0.86603,0.00000]];
HexSym=[[1.00000,0.00000,0.00000,0.00000],[0.86603,0.00000,0.00000,0.50000],
		[0.50000,0.00000,0.00000,0.86603],[0.00000,0.00000,0.00000,1.00000],
		[0.50000,-0.00000,-0.00000,-0.86603],[0.86603,-0.00000,-0.00000,-0.50000],
		[0.00000,1.00000,0.00000,0.00000],[0.00000,0.86603,0.50000,0.00000],
		[0.00000,0.50000,0.86603,0.00000],[0.00000,0.00000,1.00000,0.00000],
		[0.00000,-0.50000,0.86603,0.00000],[0.00000,-0.86603,0.50000,0.00000]];
CubSym=[[1.00000,0.00000,0.00000,0.00000],[0.70711,0.70711,0.00000,0.00000],
		[0.00000,1.00000,0.00000,0.00000],[0.70711,-0.70711,0.00000,0.00000],
		[0.70711,0.00000,0.70711,0.00000],[0.00000,0.00000,1.00000,0.00000],
		[0.70711,0.00000,-0.70711,0.00000],[0.70711,0.00000,0.00000,0.70711],
		[0.00000,0.00000,0.00000,1.00000],[0.70711,0.00000,0.00000,-0.70711],
		[0.50000,0.50000,0.50000,0.50000],[0.50000,-0.50000,-0.50000,-0.50000],
		[0.50000,-0.50000,0.50000,0.50000],[0.50000,0.50000,-0.50000,-0.50000],
		[0.50000,0.50000,-0.50000,0.50000],[0.50000,-0.50000,0.50000,-0.50000],
		[0.50000,-0.50000,-0.50000,0.50000],[0.50000,0.50000,0.50000,-0.50000],
		[0.00000,0.70711,0.70711,0.00000],[0.00000,-0.70711,0.70711,0.00000],
		[0.00000,0.70711,0.00000,0.70711],[0.00000,0.70711,0.00000,-0.70711],
		[0.00000,0.00000,0.70711,0.70711],[0.00000,0.00000,0.70711,-0.70711]];

def QuaternionProduct(q,r):
	Q = [0,0,0,0]
	Q[0] = r[0]*q[0] - r[1]*q[1] - r[2]*q[2] - r[3]*q[3]
	Q[1] = r[1]*q[0] + r[0]*q[1] + r[3]*q[2] - r[2]*q[3]
	Q[2] = r[2]*q[0] + r[0]*q[2] + r[1]*q[3] - r[3]*q[1]
	Q[3] = r[3]*q[0] + r[0]*q[3] + r[2]*q[1] - r[1]*q[2]
	if (Q[0] < 0):
		Q[0] = -Q[0]
		Q[1] = -Q[1]
		Q[2] = -Q[2]
		Q[3] = -Q[3]
	return Q

def MakeSymmetries(SGNr):
	if (SGNr <= 2):
		NrSymmetries = 1
		Sym = TricSym
	elif (SGNr <= 15):
		NrSymmetries = 2
		Sym = MonoSym
	elif (SGNr <= 74):
		NrSymmetries = 4
		Sym = OrtSym
	elif (SGNr <= 142):
		NrSymmetries = 8
		Sym = TetSym
	elif (SGNr <= 167):
		NrSymmetries = 6
		Sym = TrigSym
	elif (SGNr <= 194):
		NrSymmetries = 12
		Sym = HexSym
	elif (SGNr <= 230):
		NrSymmetries = 24
		Sym = CubSym
	return NrSymmetries,Sym

def BringDownToFundamentalRegionSym(QuatIn,NrSymmetries,Sym):
	maxCos = -10000.0
	q2 = [0,0,0,0]
	for i in range(NrSymmetries):
		q2[0] = Sym[i][0]
		q2[1] = Sym[i][1]
		q2[2] = Sym[i][2]
		q2[3] = Sym[i][3]
		qt = QuaternionProduct(QuatIn,q2)
		if (maxCos < qt[0]):
			maxCos = qt[0]
			QuatOut = qt
	return QuatOut

def OrientMat2Quat(OrientMat):
	Quat = [0,0,0,0]
	trace = OrientMat[0] + OrientMat[4] + OrientMat[8]
	if (trace > 0):
		s = 0.5/sqrt(trace+1.0)
		Quat[0] = 0.25/s
		Quat[1] = (OrientMat[7]-OrientMat[5])*s
		Quat[2] = (OrientMat[2]-OrientMat[6])*s
		Quat[3] = (OrientMat[3]-OrientMat[1])*s
	else:
		if (OrientMat[0]>OrientMat[4] and OrientMat[0]>OrientMat[8]):
			s = 2.0*sqrt(1.0+OrientMat[0]-OrientMat[4]-OrientMat[8])
			Quat[0] = (OrientMat[7]-OrientMat[5])/s
			Quat[1] = 0.25*s
			Quat[2] = (OrientMat[1]+OrientMat[3])/s
			Quat[3] = (OrientMat[2]+OrientMat[6])/s
		elif (OrientMat[4] > OrientMat[8]):
			s = 2.0*sqrt(1.0+OrientMat[4]-OrientMat[0]-OrientMat[8])
			Quat[0] = (OrientMat[2]-OrientMat[6])/s
			Quat[1] = (OrientMat[1]+OrientMat[3])/s
			Quat[2] = 0.25*s
			Quat[3] = (OrientMat[5]+OrientMat[7])/s
		else:
			s = 2.0*sqrt(1.0+OrientMat[8]-OrientMat[0]-OrientMat[4])
			Quat[0] = (OrientMat[3]-OrientMat[1])/s
			Quat[1] = (OrientMat[2]+OrientMat[6])/s
			Quat[2] = (OrientMat[5]+OrientMat[7])/s
			Quat[3] = 0.25*s
	if (Quat[0] < 0):
		Quat[0] = -Quat[0]
		Quat[1] = -Quat[1]
		Quat[2] = -Quat[2]
		Quat[3] = -Quat[3]
	QNorm = sqrt(Quat[0]*Quat[0] + Quat[1]*Quat[1] + Quat[2]*Quat[2] + Quat[3]*Quat[3])
	Quat[0] /= QNorm
	Quat[1] /= QNorm
	Quat[2] /= QNorm
	Quat[3] /= QNorm
	return Quat

def Euler2OrientMat(Euler):
	m_out = [0]*9
	psi = Euler[0]
	phi = Euler[1]
	theta = Euler[2]
	cps = cos(psi)
	cph = cos(phi)
	cth = cos(theta)
	sps = sin(psi)
	sph = sin(phi)
	sth = sin(theta)
	m_out[0] = cth * cps - sth * cph * sps
	m_out[1] = -cth * cph * sps - sth * cps
	m_out[2] = sph * sps
	m_out[3] = cth * sps + sth * cph * cps
	m_out[4] = cth * cph * cps - sth * sps
	m_out[5] = -sph * cps
	m_out[6] = sth * sph
	m_out[7] = cth * sph
	m_out[8] = cph
	return m_out

def eul2omMat(euler):
	m_out = np.zeros((euler.shape[0],9))
	cps = np.cos(euler[:,0])
	cph = np.cos(euler[:,1])
	cth = np.cos(euler[:,2])
	sps = np.sin(euler[:,0])
	sph = np.sin(euler[:,1])
	sth = np.sin(euler[:,2])
	m_out[:,0] = cth * cps - sth * cph * sps
	m_out[:,1] = -cth * cph * sps - sth * cps
	m_out[:,2] = sph * sps
	m_out[:,3] = cth * sps + sth * cph * cps
	m_out[:,4] = cth * cph * cps - sth * sps
	m_out[:,5] = -sph * cps
	m_out[:,6] = sth * sph
	m_out[:,7] = cth * sph
	m_out[:,8] = cph
	return m_out

# Euler angles must be in radians, answer in radians as well
def GetMisOrientationAngle(euler1,euler2,SGNum):
	quat1 = OrientMat2Quat(Euler2OrientMat(euler1))
	quat2 = OrientMat2Quat(Euler2OrientMat(euler2))
	NrSymmetries,Sym = MakeSymmetries(SGNum)
	q1FR = BringDownToFundamentalRegionSym(quat1,NrSymmetries,Sym)
	q2FR = BringDownToFundamentalRegionSym(quat2,NrSymmetries,Sym)
	q1FR = quat1
	q2FR = quat2
	q1FR[0] = -q1FR[0]
	QP = QuaternionProduct(q1FR,q2FR)
	MisV = BringDownToFundamentalRegionSym(QP,NrSymmetries,Sym)
	if (MisV[0] > 1):
		MisV[0] = 1
	return 2*acos(MisV[0])

# OM is 9 length vector
def GetMisOrientationAngleOM(OM1,OM2,SGNum):
	quat1 = OrientMat2Quat(OM1)
	quat2 = OrientMat2Quat(OM2)
	NrSymmetries,Sym = MakeSymmetries(SGNum)
	q1FR = BringDownToFundamentalRegionSym(quat1,NrSymmetries,Sym)
	q2FR = BringDownToFundamentalRegionSym(quat2,NrSymmetries,Sym)
	q1FR = quat1
	q2FR = quat2
	q1FR[0] = -q1FR[0]
	QP = QuaternionProduct(q1FR,q2FR)
	MisV = BringDownToFundamentalRegionSym(QP,NrSymmetries,Sym)
	if (MisV[0] > 1):
		MisV[0] = 1
	return 2*acos(MisV[0])


euler_1_traditional=np.fromfile("/Users/xiaoxu.guo/Desktop/fullsize/tr/EulerAngles1.bin",dtype=float)

euler_2_traditional=np.fromfile("/Users/xiaoxu.guo/Desktop/fullsize/tr/EulerAngles2.bin",dtype=float)

euler_3_traditional=np.fromfile("/Users/xiaoxu.guo/Desktop/fullsize/tr/EulerAngles3.bin",dtype=float)
print

euler_1_n2v=np.fromfile("/Users/xiaoxu.guo/Desktop/fullsize/n2v/EulerAngles1.bin",dtype=float)

euler_2_n2v=np.fromfile("/Users/xiaoxu.guo/Desktop/fullsize/n2v/EulerAngles2.bin",dtype=float)

euler_3_n2v=np.fromfile("/Users/xiaoxu.guo/Desktop/fullsize/n2v/EulerAngles3.bin",dtype=float)

gid_tr_raw=np.fromfile("/Users/xiaoxu.guo/Desktop/fullsize/tr/GrainNrs.bin",dtype=np.int32)

gsize_tr=np.fromfile("/Users/xiaoxu.guo/Desktop/fullsize/tr/GrainSizes.bin",dtype=np.int32)


gid_n2v_raw=np.fromfile("/Users/xiaoxu.guo/Desktop/fullsize/n2v/GrainNrs.bin",dtype=np.int32)

gsize_n2v=np.fromfile("/Users/xiaoxu.guo/Desktop/fullsize/n2v/GrainSizes.bin",dtype=np.int32)


array_size=euler_1_traditional.shape
m=0
g_n2v=0
g_tr=0
gid_tr=[]
gid_tr_unique=[]
gid_n2v=[]
gid_n2v_unique=[]


for i in range(array_size[0]):
 if gid_tr_raw[i]>=0 and gsize_tr[i]>4:
  gid_tr.append(gid_tr_raw[i])
  g_tr=g_tr+1
 if gid_n2v_raw[i]>=0 and gsize_n2v[i]>4:
  gid_n2v.append(gid_n2v_raw[i])
  g_n2v=g_n2v+1
  
gid_tr_unique=np.unique(gid_tr)
array_size_gid_tr_unique=gid_tr_unique.shape
gid_n2v_unique=np.unique(gid_n2v)
array_size_gid_n2v_unique=gid_n2v_unique.shape

gid_n2v_record=np.zeros(array_size[0])
gid_tr_record=np.zeros(array_size[0])
size_diff=np.full(array_size_gid_tr_unique[0],100000000)
size_change=np.full(array_size[0],0)
FN=open('grain_size_diff.txt','w')
print("Tr total grain number:",array_size_gid_tr_unique[0])
print("How many points in Tr have value and the size > 4:",g_tr)
print("How many points in Tr don't have value or size <= 4:",array_size[0]-g_tr)

print("N2V total grain number:",array_size_gid_n2v_unique[0])
print("How many points in N2V have value and size > 4:",g_n2v)
print("How many points in N2V don't have value or size <= 4:",array_size[0]-g_n2v)
l=0
for i in range(array_size_gid_tr_unique[0]):
 gid_tr_raw_now_index=[]
 gid_tr_raw_now_index.append(np.where(gid_tr_raw==gid_tr_unique[i]))
 #gid_tr_raw_now_index=np.asarray(gid_tr_raw_now_index)
 n=0
 for j in gid_tr_raw_now_index[0][0]:
  Euler_now_Traditional=[euler_1_traditional[j],euler_2_traditional[j],euler_3_traditional[j]]
  #print(Euler_now_Traditional)
  Euler_now_n2v=[euler_1_n2v[j],euler_2_n2v[j],euler_3_n2v[j]]
  miso=GetMisOrientationAngle(Euler_now_Traditional,Euler_now_n2v,225)
  if miso < 0.03:
   size_diff[i]=gsize_n2v[j]-gsize_tr[j]
   size_change[j]=gsize_n2v[j]-gsize_tr[j]
   gsize_n2v_now=gsize_n2v[j]
   gsize_tr_now=gsize_tr[j]
   gid_n2v_record[j]=1
   if n==0:
    gid_n2v_now=gid_n2v_raw[j]
    gid_n2v_now_index=[]
    gid_n2v_now_index.append(np.where(gid_n2v_raw==gid_n2v_now))
    gid_n2v_now_index=np.asarray(gid_n2v_now_index)
    gid_tr_now=gid_tr_raw[j]
    gid_tr_now_index=[]
    gid_tr_now_index.append(np.where(gid_tr_raw==gid_tr_now))
    gid_tr_now_index=np.asarray(gid_tr_now_index)
    l=l+1
   # print(gid_n2v_now_index.shape)
    for k in gid_n2v_now_index[0][0]:
     #print(k)
     gid_n2v_record[k]=1
    for ktr in gid_tr_now_index[0][0]:
     #print(k)
     gid_tr_record[ktr]=1
    n=n+1
    FN.write('%lf %lf %lf\n'%(size_diff[i],gsize_tr_now,gsize_n2v_now))
    
   m=m+1
  
print("How many points in Tr remain the same grain in N2V:",m)
print("How many grains in Tr still can be found in N2V:",l)
print("How many grains in Tr can't be found in the N2V:",array_size_gid_tr_unique[0]-l)

fig=plt.figure()
#plt.figure()

size_change=size_change.reshape(400,400)

norm=mcolors.TwoSlopeNorm(vmin=-10, vmax = 10, vcenter=0)
plt.imshow(size_change,cmap='bwr',norm=norm)

plt.colorbar()
plt.show()

fig.savefig('Fig17.pdf',dpi=fig.dpi)
'''

gid_n2v_rest=[]
gid_tr_rest=[]
for i in range(array_size[0]):
 if (gid_n2v_record[i]==0)and(gsize_n2v[i]>=0):
  gid_n2v_rest.append(gid_n2v_raw[i])
print("How many points in N2V are new:",len(gid_n2v_rest))
gid_n2v_rest_unique=np.unique(gid_n2v_rest)
print("How many grains in N2V are new:",gid_n2v_rest_unique.shape[0])
for i in gid_n2v_rest_unique:
 gid_n2v_rest_now_index=[]
 gid_n2v_rest_now_index.append(np.where(gid_n2v_raw==i))
 FN.write('%lf %lf 0\n'%(gsize_n2v[gid_n2v_rest_now_index[0][0][0]],gsize_n2v[gid_n2v_rest_now_index[0][0][0]]))

#for i in range(array_size[0]):
 #if (gid_tr_record[i]==0)and(gsize_tr[i]>=0):
  #gid_tr_rest.append(gid_tr_raw[i])
#print("How many points in Tr disappear:",len(gid_tr_rest))
#gid_tr_rest_unique=np.unique(gid_tr_rest)
#print("How many grains in Tr are disappear:",gid_tr_rest_unique.shape[0])


FN.close()

FN=open('PIXELGO.txt','w')
'''
