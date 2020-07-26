from glob import glob
import cv2

pngs = glob('C:/Users/Blue Bird/Desktop/New folder/*.png')
# use glob('./**/*.png', recursive=True) for all sub folders.

for j in pngs:
    img = cv2.imread(j)
    cv2.imwrite(j[:-3] + 'jpg', img)



## Remove a particular file type, here we are removing png files.

import os

dirname = 'C:/Users/Blue Bird/Desktop/New folder/'
png_files = os.listdir(dirname)   # This list out the files in the directory

for item in png_files:
    if item.endswith('.png'):
        os.remove(dirname + item)  # Prepend the directory to the file name. Which is same as below line
        #os.remove(os.path.join(dirname,item))


