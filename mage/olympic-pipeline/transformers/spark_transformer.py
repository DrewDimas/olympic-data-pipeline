from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, lit
from pyspark.sql.types import IntegerType, StringType  
from pyspark.ml.feature import StringIndexer
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

     # Convert all column names to lowercase
    for col_name in data.columns:
        data = data.withColumnRenamed(col_name, col_name.lower())

    # Check if 'ID' column exists before trying to drop it
    if 'id' in data.columns:
        data = data.drop('id')

    #Converting to numeric indices for potential ML tasks:
    indexer_sex = StringIndexer(inputCol="sex", outputCol="sex_index")
    data = indexer_sex.fit(data).transform(data)

    indexer_season = StringIndexer(inputCol="season", outputCol="season_index")
    data = indexer_season.fit(data).transform(data)

    # Filter out entries 
    data_male = data.filter(col("sex") == 'M')
    
    data_male = data_male.toPandas() 
    return data_male


@test
def test_transform(output, *args) -> None:
    """
    Test code for verifying the output of the transformer block.
    """
 