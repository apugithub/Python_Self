from glob import glob
from zipfile import ZipFile
import zipfile as zp

folder_files = glob('C:/Users/Blue Bird/Desktop/New folder/*')
folder_path = 'C:/Users/Blue Bird/Desktop/New folder'

for i in folder_files:
    try:
        with ZipFile(i, 'r') as zip:               #This will pick the zip file name with read permission
            zip.printdir()                         # This will print all the files inside that zip file
            zip.extractall(path=folder_path)       #If Path is not mentioned it will save in default location
    except  zp.BadZipFile:                         #This is to avoid exception caused by the presence of non-zip file
        continue

#The above for loop can also be written as below
'''for i in folder_files:
    try:
        ZipFile(i).printdir()
        ZipFile(i).extractall(path=folder_path)
    except zp.BadZipFile:
        continue '''



