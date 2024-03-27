import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

@transformer
def transform(data, *args, **kwargs):
    """
    Transformer block for cleaning and transforming the dataset.

    Performs the following operations:
        Drops the 'ID' column.
        Converts specified columns to 'category' dtype.
        Replaces null values in the "Medal" column with "No Medal".
        Saves the transformed DataFrame to a Parquet file.
    
    Args:
        data: The output from the upstream parent block (a pandas DataFrame)
        args: The output from any additional upstream blocks (if applicable)
    
    Returns:
        A transformed pandas DataFrame.
    """
    # Dropping the 'ID' column from the DataFrame
    data = data.drop('ID', axis=1)

    # Replace null values in the "Medal" column with "No Medal"
    data['Medal'] = data['Medal'].fillna('No Medal')
    
    # List of categorical columns to be converted
    categorical_columns = [
        'Sex', 'Team', 'NOC', 'Games', 'Season', 'City', 'Sport', 'Event', 'Medal'
    ]
    
    # Converting the specified columns to 'category' dtype
    data[categorical_columns] = data[categorical_columns].astype('category')

    # Save the transformed DataFrame to a Parquet file
    data.to_parquet('olympic_data_cleaned.parquet', index=False)
    
    return data

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
    assert 'ID' not in output.columns, 'ID column should be dropped'
    for col in ['Sex', 'Team', 'NOC', 'Games', 'Season', 'City', 'Sport', 'Event', 'Medal']:
            assert str(output[col].dtype) == 'category', f"'{col}' column is not of type 'category'"