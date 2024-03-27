import pandas as pd
import os
import requests

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

@data_loader
def load_data(*args, **kwargs):
    """
    Code for loading data from an online source using requests.
    
    Returns:
        A pandas DataFrame loaded from the downloaded dataset.
    """
    url = 'https://figshare.com/ndownloader/files/11693840'
    local_filename = url.split('/')[-1]
    
    # Check if file already downloaded
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
    
    # Assuming the file is a CSV, adjust if different
    data = pd.read_csv(local_filename)
    
    return data

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
    # Additional basic check for a DataFrame
    assert not output.empty, 'The output DataFrame is empty'
