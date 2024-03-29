from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, col, lit, when
from pyspark.sql.types import StringType
from pyspark.sql import DataFrame as PySparkDataFrame
from pyspark.ml.feature import StringIndexer

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

    # Check if 'ID' column exists before trying to drop it
    if 'ID' in data.columns:
        data = data.drop('ID')

    # Replace null values in the "Medal" column with "No Medal"
    data = data.withColumn("Medal", when(col("Medal").isNull(), lit("No Medal")).otherwise(col("Medal")))

    #Converting to numeric indices for potential ML tasks:
    indexer_sex = StringIndexer(inputCol="Sex", outputCol="Sex_Index")
    data = indexer_sex.fit(data).transform(data)

    indexer_season = StringIndexer(inputCol="Season", outputCol="Season_Index")
    data = indexer_season.fit(data).transform(data)

    # Filter out entries 
    data_male = data.filter(col("Sex") == 'M')
    
   # return {'data_recent': data_recent, 'data_female': data_female, 'data_male': data_male}
    data_male = data_male.toPandas() 
    return data_male


@test
def test_transform(output, *args) -> None:
    """
    Test code for verifying the output of the transformer block.
    """
 