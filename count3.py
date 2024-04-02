#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 16:00:33 2024

@author: xgg97
"""

import imageio
import numpy as np
import pandas as pd
import PIL
from PIL import Image
import matplotlib.pyplot as plt


id_volume_sort_low=np.loadtxt('id_volume_sort_low.csv')
unique_id_sort_low=np.loadtxt('uniqueid_sort_low.csv')
id_volume_sort_low=id_volume_sort_low[0:-1]

id_volume_high=np.loadtxt('id_volume_sort.csv')
unique_id_high=np.loadtxt('uniqueid_sort.csv')
id_volume_high=id_volume_high[0:-2]
unique_id_high=unique_id_high[0:-2]

slicen=np.random.choice(id_volume_high.shape[0],id_volume_sort_low.shape[0])
id_volume_high_random=id_volume_high[slicen]
unique_id_high_random=unique_id_high[slicen]

arrIndex=np.array(id_volume_high_random).argsort()
unique_id_sort_high_random=unique_id_high_random[arrIndex]
id_volume_sort_high_random=id_volume_high_random[arrIndex]

np.savetxt("uniqueid_sort_random_high.csv",unique_id_sort_high_random)
np.savetxt("id_volume_sort_random_high.csv",id_volume_sort_high_random)

early_volume_higher_than_150=0
late_volume_higher_than_150=0
for count in range(id_volume_sort_low.shape[0]-150):
 early_volume_higher_than_150=early_volume_higher_than_150+id_volume_sort_low[count+150]
 late_volume_higher_than_150=late_volume_higher_than_150+id_volume_sort_high_random[count+150]
print("early volume: ",early_volume_higher_than_150)
print("late volume: ",late_volume_higher_than_150)
print("rate:",early_volume_higher_than_150/late_volume_higher_than_150)
plt.plot(id_volume_sort_high_random,c='g',label='stage ?')
plt.plot(id_volume_sort_low,c='b',label='early')

plt.legend()
plt.show()


