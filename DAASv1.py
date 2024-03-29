#This code will give output in cross linkage fashion.. like as per current input the output will be 
'''
SELECT * FROM t1 INNER JOIN t2 ON link1
SELECT * FROM t2 INNER JOIN t3 ON link2


from pyspark.sql import SparkSession
from pyspark import SparkContext
from pyspark.sql.functions import *


#Initializing spark session
spark = SparkSession.builder.appName("DAAS") \
.config("hive.exec.dynamic.partition", "true") \
.config("hive.exec.dynamic.partition.mode", "nonstrict") \
.config("spark.sql.warehouse.dir", "/apps/hive/warehouse") \
.config("spark.sql.catalogImplementation","in-memory") \
.config("spark.sql.shuffle.partitions","20") \
.enableHiveSupport() \
.getOrCreate()

#setloglevel
spark.sparkContext.setLogLevel("ERROR")
'''

def fw (**kargs):

    ## For DAAS
    if (len(kargs.get('tables'))) == 1 :
        x = "SELECT * FROM {}".format(kargs['tables'][0])
        print (x)
        #spark.sql (x)


    ## For CAAS
    else:
        if len(kargs['tables']) != len(kargs['linkage']) + 1:
            print('Discrepancy in number of links and tables provided')

        else:
            #print('SELECT * FROM {} INNER JOIN {} ON {}'.format(kargs['tables'][0],kargs['tables'][1],kargs['linkage'][0]))

            for i in range(len(kargs['linkage'])):
                y = 'SELECT * FROM {} INNER JOIN {} ON {}'.format(kargs['tables'][i], kargs['tables'][i + 1], kargs['linkage'][i])
                print(y)
                #spark.sql(y)

fw(tables =['t1','t2','t3'], linkage= ['link1', 'link2'], filter= ['1=1'])
