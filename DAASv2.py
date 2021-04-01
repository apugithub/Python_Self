## There code will merge all the table and add all the links and filters

'''from pyspark.sql import SparkSession
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
    
    # Error Handling in input
    if (len(kargs['linkage']) < len(kargs['tables']) - 1):
        print('Discrepancy in number of links and tables provided')

    else:
        '''for i in range(len(kargs['linkage'])):
            y = 'SELECT * FROM {} INNER JOIN {} ON {}'.format(kargs['tables'][i], kargs['tables'][i + 1], kargs['linkage'][i])
            print(y)'''
            
        df = "select * from " + ', '.join(i for i in kargs['tables']) + " on " + ' and '.join(i for i in kargs['linkage']) + " where " + ' and '.join(i for i in kargs['filter'])
        print (df)
        #df1 = spark.sql(df)

dct = { 'tables' : ['t1','t2','t3'], 'linkage' : ['link1', 'link2', 'link3'], 'filter' : ['1=1','filter1', 'filter2'] }

# Accessing dictionary elements and passing to the function
fw(tables = dct['tables'], linkage= dct['linkage'], filter= dct['filter'])


