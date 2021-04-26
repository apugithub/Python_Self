from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("test").getOrCreate()

df = spark.read.text("E:/hadoop/sample.json")

