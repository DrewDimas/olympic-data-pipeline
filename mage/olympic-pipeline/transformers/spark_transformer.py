from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, col, lit, when
from pyspark.sql import DataFrame as PySparkDataFrame
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

# Assuming transformer and test decorators are imported correctly

@transformer
def transform(data, *args, **kwargs):
    """
    Transform the Olympic dataset using Apache Spark operations.
    """
    # Ensuring a Spark session is available
    spark = SparkSession.builder.appName("OlympicDataTransformation").getOrCreate()

    # If 'data' is a pandas DataFrame, convert it to a PySpark DataFrame
    if not isinstance(data, PySparkDataFrame):
        data = spark.createDataFrame(data)
    
    # Handling the data transformation
    # Fill null values in 'Height' and 'Weight' columns with average values
    #avg_height = data.agg(avg(col("Height")).alias("avg_height")).collect()[0]["avg_height"]
    #avg_weight = data.agg(avg(col("Weight")).alias("avg_weight")).collect()[0]["avg_weight"]
    #data = data.withColumn("Height", when(col("Height").isNull(), avg_height).otherwise(col("Height")))
    #data = data.withColumn("Weight", when(col("Weight").isNull(), avg_weight).otherwise(col("Weight")))

    # Filter out entries before the year 2000 for a more recent dataset analysis
    data_recent = data.filter(col("Year") >= 2000)
    
    return data_recent

@test
def test_transform(output, *args) -> None:
    """
    Test code for verifying the output of the transformer block.
    """
 