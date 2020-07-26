## Remove a particular file type, here we are removing png files.

import os

dirname = 'C:/Users/Blue Bird/Desktop/New folder/'
png_files = os.listdir(dirname)   # This list out the files in the directory

def remove_files (ext):
    for item in png_files:
        if item.endswith(ext):
            os.remove(dirname + item)  # Prepend the directory to the file name. Which is same as below line
        #os.remove(os.path.join(dirname,item))

remove_files('png')