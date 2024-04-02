# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

Input_filename=input("please type the file path:")

X_left,X_right,Y_lower,Y_upper=map(int,input("please type values of X_left, X_right, Y_lower, Y_upper:").split())
df=pd.read_csv(Input_filename,skiprows=3,sep='\t')
df2=df[(df['X']>=X_left)&(df['X']<=X_right)&(df['Y']>=Y_lower)&(df['Y']<=Y_upper)]
Output_filename='X_left%sX_right%sY_lower%sY_upper%s.mic' % (X_left,X_right,Y_lower,Y_upper)
df2.to_csv(Output_filename,sep='\t',float_format='%.6f',index=False)

with open(Output_filename,'r+') as f:
    content=f.read()
    f.seek(0,0)
    f.write('%TriEdgeSize 3.000000\n%NumPhases 1\n%GlobalPosition 0.000000\n'+content)
    

    


