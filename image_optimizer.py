import sys
from datetime import datetime
from PIL import Image
from glob import glob

#LOG_FILENAME = datetime.now().strftime('C:/Users/Blue Bird/Desktop/Logfile_%H_%M_%S_%d_%m_%Y.txt')
#sys.stdout = open(LOG_FILENAME, 'w')  #This line will print the o/p in a file in liew of console


folder_files = glob('C:/Users/Blue Bird/Desktop/New folder/*')

for i in folder_files:
    savedfilename = i.split('.')[0] #Just extracting the path till filename
    #print('Saved filenames= ' + savedfilename)
    foo = Image.open(i)  #The said image file has to open first, so this is part of the process
    print("Image Started Processing..=  " + i)
    foo.save(savedfilename+ "_Optimized.jpg", optimize=True, quality=30)
    print("Image Processed and saved at:  ", savedfilename+ "_Optimized.jpg")
    print('\n')



