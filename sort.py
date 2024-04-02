
import imageio
import numpy as np
import pandas as pd
import PIL
from PIL import Image
import matplotlib.pyplot as plt


input_path='/home/xgg97/Desktop/rector low/3dsegst/'
total_slice=200
totalmito=0
mitoarray=[]

for slice_number in range(total_slice):
    number_digit="%04d"%slice_number
    input_filename=input_path+'3DSEG'+number_digit+'.tif'
    im=Image.open(input_filename)
    im_array=np.array(im)
    mitoarray.extend(im_array)
unique_id,id_volume=np.unique(mitoarray,return_counts=True)

arrIndex=np.array(id_volume).argsort()
unique_id_sort=unique_id[arrIndex]
id_volume_sort=id_volume[arrIndex]

np.savetxt("uniqueid_sort.csv",unique_id_sort)
np.savetxt("id_volume_sort.csv",id_volume_sort)
'''
np.savetxt("id_volume_id_sort.csv",unique_id_sort,id_volume_sort)
'''

for slice_number in range(total_slice):
    number_digit="%04d"%slice_number
    input_filename=input_path+'3DSEG'+number_digit+'.tif'
    im=Image.open(input_filename)
    im_array=np.array(im)
    for number in range(unique_id_sort.shape[0]):
        print(number)
        im_array[im_array==unique_id_sort[number]]=number
    imageio.imwrite('/home/xgg97/Desktop/rector low/sort_image/sort'+number_digit+'.tif',im_array)

    
   
'''
plt.plot(unique_id,id_volume)
'''






