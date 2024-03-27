import os
from pyspark.sql import SparkSession

spark = SparkSession.builder.master(os.getenv('SPARK_MASTER_HOST', 'local')).getOrCreate()

