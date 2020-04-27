import sys
from datetime import datetime

LOG_FILENAME = datetime.now().strftime('C:/Users/Blue Bird/Desktop/Logfile_%H_%M_%S_%d_%m_%Y.txt')
sys.stdout = open(LOG_FILENAME, 'w')  #This line will print the o/p in a file in liew of console

print('The console of program')