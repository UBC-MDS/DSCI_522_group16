import os
import pandas as pd
from sklearn.externals import joblib  # Use joblib for loading models
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
@click.argument('X_file', type=click.Path(exists=True))
@click.argument('y_file', type=click.Path(exists=True))
def evaluate_model(model_file, X_file, y_file):
    """
    Evaluate a polynomial regression model using provided data.

    Parameters:
        - model_file (str): Path to the saved model file.
        - X_file (str): Path to the feature matrix CSV file.
        - y_file (str): Path to the target variable CSV file.

    Returns:
        None
    """
    # Load the trained model
    best_model = joblib.load(model_file)

    # Load training data
    X = pd.read_csv(X_file)
    y = pd.read_csv(y_file, header=None, squeeze=True)  # Assuming y is a single-column DataFrame

    # Calculate model scores
    score_table = calculate_model_scores(best_model, X, y)
    
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Save output files in the 'results/tables' directory
    results_dir = os.path.join(script_dir, '..', 'results', 'tables')
    os.makedirs(results_dir, exist_ok=True)
    
    score_table.to_csv(os.path.join(results_dir, 'score_table.csv'), index=False)

    # Calculate mean scores
    result = score_table.mean(axis=1).to_frame()
    mean_scores = result.rename(columns={0: "mean_value"})
    mean_scores.to_csv(os.path.join(results_dir, 'mean_scores.csv'), index=False)

if __name__ == '__main__':
    evaluate_model()


# In terminal at root directory of the project:
#python script/evaluate_model.py results/models/model_output.joblib data/Processed/x_train_w.csv data/Processed/y_train_w.csv
