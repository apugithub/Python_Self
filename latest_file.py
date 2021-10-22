import glob
import os

file_path = glob.iglob('C:/Users/Blue Bird/Desktop/test/*.txt')
latest_file = max(file_path, key=os.path.getctime)

print(latest_file)

f = open(latest_file, "r")
dict_file = f.read()
print(dict_file)
