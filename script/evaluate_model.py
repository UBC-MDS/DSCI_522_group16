import os
import pandas as pd
import pickle  # Use pickle for loading models
from sklearn.model_selection import cross_validate
import click

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

@click.command()
@click.argument('model_file', type=click.Path(exists=True))
@click.argument('x_file', type=click.Path(exists=True))
@click.argument('y_file', type=click.Path(exists=True))
def evaluate_model(model_file, x_file, y_file):
    # Load the trained model using pickle
    with open(model_file, 'rb') as model_file:
        best_model = pickle.load(model_file)

    # Load training data
    X = pd.read_csv(x_file)
    y = pd.read_csv(y_file)  # Assuming y is a single-column DataFrame

    # Specify default scoring metrics
    default_scoring_metrics = {
        "r2": "r2",
        "sklearn MAPE": "neg_mean_absolute_percentage_error",
        "neg_root_mean_square_error": "neg_root_mean_squared_error",
        "neg_mean_squared_error": "neg_mean_squared_error"}

    # Calculate model scores with default metrics
    score_table = calculate_model_scores(best_model, X, y, default_scoring_metrics)
    print(score_table)
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Save output files in the 'results/tables' directory
    results_dir = os.path.join(script_dir, '..', 'results', 'tables')
    os.makedirs(results_dir, exist_ok=True)
    
    score_table.to_csv(os.path.join(results_dir, 'score_table.csv'), index=True)

    # Calculate mean scores
    result = score_table.mean(axis=1).to_frame()
    mean_scores = result.rename(columns={0: "mean_value"})
    print(mean_scores)
    mean_scores.to_csv(os.path.join(results_dir, 'mean_scores.csv'), index=True)

if __name__ == '__main__':
    evaluate_model()




# In terminal at root directory of the project:
#python script/evaluate_model.py results/models/best_model.pkl data/Processed/x_train_w.csv data/Processed/y_train_w.csv

