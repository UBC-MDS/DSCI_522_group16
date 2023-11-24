import requests
import zipfile
from pathlib import Path
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import cross_validate
import pandas as pd
import altair as alt

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



def create_repeated_scatter_chart(data, columns, width=100, height=100):
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



def calculate_model_scores(model, X, y, scoring_metrics=None):
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


