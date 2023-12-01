import pandas as pd
from sklearn.model_selection import train_test_split
import click
import os

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
        print(white_wine.info())

    if split_data:
        # Split data into train and test sets
        white_train, white_test = train_test_split(white_wine, train_size=0.70, random_state=123)

        # Save train and test sets to the 'data/Processed' folder
        output_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'Processed')
        os.makedirs(output_folder, exist_ok=True)
        
        train_file_path = os.path.join(output_folder, 'white_train.csv')
        test_file_path = os.path.join(output_folder, 'white_test.csv')
        
        white_train.to_csv(train_file_path, index=False)
        white_test.to_csv(test_file_path, index=False)
        
        print(f"Train and test sets saved to {train_file_path} and {test_file_path}.")

if __name__ == '__main__':
    process_white_wine()


# In terminal, set current working directory as the root of git repo:
# assume you want to drop NA values, display dataset information, and split the data into train and test sets based on the options in your script.
# python script/read_split_and_save.py data/Raw/winequality-white.csv --dropna --info --split-data

#Explanation of the options:

# --dropna: Include this option if you want to drop NA values.
# --info: Include this option if you want to display dataset information.
# --split-data: Include this option if you want to split the data into train and test sets.