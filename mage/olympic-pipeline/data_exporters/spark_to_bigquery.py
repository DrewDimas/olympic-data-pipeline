import pandas as pd

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

@data_exporter
def export_to_bigquery(data_recent=None, data_female=None, data_male=None, **kwargs):
    """
    Exports specified pandas DataFrames to BigQuery tables.

    Parameters:
    - data_recent: DataFrame containing recent data to be exported.
    - data_female: DataFrame containing female data to be exported.
    - data_male: DataFrame containing male data to be exported.
    """

    project_id = 'datacamp2024-412820'
    dataset_name = 'olympic_data'

    # Define table names for each DataFrame
    tables = {
        'data_recent': f'{dataset_name}.recent_table',
        'data_female': f'{dataset_name}.female_table',
        'data_male': f'{dataset_name}.male_table',
    }

    # Prepare DataFrames to export by converting from PySpark to pandas if necessary
    dataframes = {
        'data_recent': data_recent.toPandas() if data_recent else None,
        'data_female': data_female.toPandas() if data_female else None,
        'data_male': data_male.toPandas() if data_male else None,
    }

    # Iterate through the dataframes and export each to BigQuery
    for key, df in dataframes.items():
        if df is not None:
            table_id = tables[key]
            print(f"Exporting DataFrame '{key}' to BigQuery table '{table_id}'...")
            df.to_gbq(destination_table=table_id, project_id=project_id, if_exists='replace')
            print(f"Successfully exported DataFrame '{key}' to BigQuery.")
        else:
            print(f"No DataFrame available for key '{key}' to export.")
