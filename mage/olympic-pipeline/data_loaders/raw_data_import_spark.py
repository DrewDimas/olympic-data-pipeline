from pyspark.sql import SparkSession
import os
import requests

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

@data_loader
def load_data_spark(*args, **kwargs):
    spark = SparkSession.builder.appName("DataLoader").getOrCreate()
    url = 'https://figshare.com/ndownloader/files/11693840'
    local_filename = url.split('/')[-1]
    
    if not os.path.exists(local_filename):
        print(f"Downloading {local_filename}...")
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(local_filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192): 
                    f.write(chunk)
        print(f"Downloaded {local_filename}.")
    else:
        print(f"{local_filename} already exists.")
    
    try:
        data = spark.read.csv(local_filename, header=True, inferSchema=True)
        print(f"Loaded data with {data.count()} records.")
        return data
    except Exception as e:
        print(f"Failed to load data: {e}")
        raise

@test
def test_output_spark(output, *args) -> None:
    assert output is not None, 'The output DataFrame is undefined'
    assert output.count() > 0, 'The output DataFrame is empty'
