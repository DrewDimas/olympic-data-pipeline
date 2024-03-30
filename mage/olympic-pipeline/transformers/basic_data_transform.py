import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

@transformer
def transform(data, *args, **kwargs):

    # Transform DataFrame to a Parquet file
    data.to_parquet('olympic_data_cleaned.parquet', index=False)
    
    return data

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
    #assert 'ID' not in output.columns, 'ID column should be dropped'
    #for col in ['Sex', 'Team', 'NOC', 'Games', 'Season', 'City', 'Sport', 'Event', 'Medal']:
    #        assert str(output[col].dtype) == 'category', f"'{col}' column is not of type 'category'"