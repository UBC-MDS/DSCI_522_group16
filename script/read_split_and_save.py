import pandas as pd
from sklearn.model_selection import train_test_split
import click

@click.command()
@click.argument('file_path', type=click.Path(exists=True))
@click.option('--dropna', is_flag=True, help='Drop NA values')
@click.option('--info', is_flag=True, help='Display dataset information')
@click.option('--split-data', is_flag=True, help='Split data into train and test sets')
def process_white_wine(file_path, dropna, info, split_data):
    """
    Load a white wine dataset from a CSV file and perform operations based on options.

    Parameters:
        - file_path (str): Path to the CSV file.
        - dropna (bool): Drop NA values if True.
        - info (bool): Display dataset information if True.
        - split_data (bool): Split data into train and test sets if True.

    Returns:
        None
    """
    # Load white wine dataset
    white_wine = pd.read_csv(file_path, sep=';')

    # Perform operations based on options
    if dropna:
        white_wine.dropna(inplace=True)
    
    if info:
        white_wine.info()

    if split_data:
        # Split data into train and test sets
        white_train, white_test = train_test_split(white_wine, train_size=0.70, random_state=123)

        # Save train and test sets to the specified folder
        white_train.to_csv("../data/Processed/white_train.csv", index=False)
        white_test.to_csv("../data/Processed/white_test.csv", index=False)

if __name__ == '__main__':
    process_white_wine()

#python script_name.py ../data/Raw/winequality-white.csv --split-data
