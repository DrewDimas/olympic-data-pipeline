from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.google_cloud_storage import GoogleCloudStorage
from pandas import DataFrame
from os import path

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

@data_exporter
def export_data_to_google_cloud_storage(df: DataFrame, **kwargs) -> None:
    """
    Exports data to a Google Cloud Storage bucket specified in the 'io_config.yaml' or directly in this function.

    Docs: https://docs.mage.ai/design/data-loading#googlecloudstorage
    """
    # Here we're using the values directly, but consider using environment variables or a secure config for production
    bucket_name = 'olympic-raw-data-bucket'  # Name of the GCS bucket
    object_key = 'test/data.csv'  # Define your object key (path in the bucket where file will be stored)

    # Optional: Load additional configurations dynamically if needed
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'

    # Assuming the configuration file or environment variables include credentials
    GoogleCloudStorage.with_config(ConfigFileLoader(config_path, config_profile)).export(
        df,
        bucket_name,
        object_key,
    )
