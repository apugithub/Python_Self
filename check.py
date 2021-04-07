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

# jason import is required to convert string dictionary to dictionary
import json

def main():

    sql = []
    status = []
    msg = []
    final = [sql, status, msg]

    with open("E:/hadoop/sample.json", "r") as file:
        dict_file = file.readlines()

    #dct1 = {'tables': ['t1', 't2', 't3'], 'linkages': ['link1', 'link2'],'filter': ['1=1', 'filter1', 'filter2']}
    #print (type(dct1))

    def fw(**kargs):
        # Error Handling in input
        if (len(kargs['linkages']) < len(kargs['tables']) - 1):
            #print('Discrepancy in number of links and tables provided')

            sql.append("None")
            status.append("Failed")
            msg.append("Discrepancy in number of links and tables provided")

        else:
            # Framing broadcast string
            if not kargs['broadcast']:  #If broadcast list is empty
                brdcst = ""
            else:
                brdcst = "/*+ broadcast(" + ','.join(i for i in kargs['broadcast']) + ")*/ "

            df = "select " + brdcst + ', '.join(i for i in kargs['sourcecolumns']) + \
                 " from " + ' join '.join(i for i in kargs['tables']) + " on " + ' on '.join(
                 i for i in kargs['linkages']) + " where " + ' and '.join(i for i in kargs['filter'])

            sql.append(df)
            status.append("Success")
            msg.append("SQL Created Successfully")


    for lines in dict_file:
        # Convert dictionary string to dictionary
        dct = json.loads(lines)
        # Accessing dictionary elements and passing to the function
        fw(tables=dct["tables"], sourcecolumns=dct["sourcecolumns"], linkages=dct["linkages"], filter=dct["filter"], broadcast=dct["broadcast"])

    print(final)

    # Creating output file first with append option
    f = open("E:/hadoop/sample_op.txt","a")
    # Writing to the same file converting the data as string
    f.write(str(final))  # List can't be saved to a file
    f.close()


# Executing main()
if __name__=="__main__":
    main()



