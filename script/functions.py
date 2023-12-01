import requests
import zipfile
from pathlib import Path
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import cross_validate
import pandas as pd
import altair as alt
from sklearn.model_selection import train_test_split
import click

#1:
@click.command()
@click.argument('url')
@click.argument('target_folder') 
def download_and_extract_data(url, target_folder):
    """
    Download a zip file from the given URL and extract it to the specified folder.

    Parameters:
        - url (str): The URL of the zip file.
        - target_folder (str): The folder where the content should be extracted.

    Returns:
        None
    """
    request = requests.get(url)
    target_path = Path(target_folder)
    target_path.mkdir(parents=True, exist_ok=True)

    zip_file_path = target_path / Path(url.split("/")[-1])

    with open(zip_file_path, 'wb') as f:
        f.write(request.content)

    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(target_path)

    print(f"Data downloaded and extracted to {target_path}")

#2:
@click.command()
@click.argument('data')
@click.argument('columns') 
@click.option('--width', default=100, help='Width of the chart')
@click.option('--height', default=100, help='Height of the chart')
def create_repeated_scatter_chart(data, columns, width, height):
    """
    Create a repeated scatter chart using Altair.

    Parameters:
        - data: The DataFrame containing the data.
        - columns: The columns to repeat for the x-axis and y-axis.
        - width (int, optional): Width of the chart. Default is 100.
        - height (int, optional): Height of the chart. Default is 100.

    Returns:
        alt.Chart: Altair chart object.
    """
    alt.data_transformers.enable('vegafusion')

    chart = alt.Chart(data).mark_point(opacity=0.3, size=10).encode(
        alt.X(alt.repeat('row'), type='quantitative'),
        alt.Y(alt.repeat('column'), type='quantitative')
    ).properties(
        width=width,
        height=height
    ).repeat(
        column=columns,
        row=columns
    )

    return chart
    
#3:
@click.command()
@click.argument('model')
@click.argument('X') 
@click.argument('y')
@click.option('--scoring_metrics', type=click.STRING, default=None, help='Dictionary of scoring metrics')
def calculate_model_scores(model, X, y, scoring_metrics):
    """
    Calculate model scores using cross-validation.

    Parameters:
        - model: The machine learning model to evaluate.
        - X: The feature matrix.
        - y: The target variable.
        - scoring_metrics (dict, optional): Dictionary of scoring metrics.
            Default is None, which uses corporate default metrics.

    Returns:
        pd.DataFrame: DataFrame containing the scores.
    """
    if scoring_metrics is None:
        # Set default corporate scoring metrics
        scoring_metrics = {
            "r2": "r2",
            "sklearn MAPE": "neg_mean_absolute_percentage_error",
            "neg_root_mean_square_error": "neg_root_mean_squared_error",
            "neg_mean_squared_error": "neg_mean_squared_error"}

    scores = pd.DataFrame(cross_validate(model, X, y, scoring=scoring_metrics, return_train_score=True)).T
    return scores


#4:
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
    download_and_extract_data()
    create_repeated_scatter_chart()
    calculate_model_scores()
    process_white_wine()
