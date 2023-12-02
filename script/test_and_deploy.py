import pandas as pd
import pickle  # Use pickle for loading models
from sklearn.metrics import r2_score, mean_absolute_error
import click
import os

@click.command()
@click.argument('model_file', type=click.Path(exists=True))
@click.argument('x_test_file', type=click.Path(exists=True))
@click.argument('y_test_file', type=click.Path(exists=True))
def test_and_deploy(model_file, x_test_file, y_test_file):
    """
    Test the best polynomial regression model and return test scores.

    Parameters:
        - model_file (str): Path to the saved model file.
        - x_test_file (str): Path to the feature matrix CSV file for testing.
        - y_test_file (str): Path to the target variable CSV file for testing.

    Returns:
        None
    """
    # Load the trained model using pickle
    with open(model_file, 'rb') as model_file:
        best_model = pickle.load(model_file)

    # Load test data
    x_test = pd.read_csv(x_test_file)
    y_test = pd.read_csv(y_test_file)  # Assuming y_test is a single-column DataFrame

    # Make predictions on the test data
    y_pred = best_model.predict(x_test)

    # Calculate test scores
    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)

    # Create a DataFrame to store the test scores
    test_scores = pd.DataFrame({'R2': [r2], 'MAE': [mae]})

    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Save the test scores to the 'results/tables' directory
    tables_dir = os.path.join(script_dir, '..', 'results', 'tables')
    os.makedirs(tables_dir, exist_ok=True)

    test_scores.to_csv(os.path.join(tables_dir, 'test_scores.csv'), index=True)
    print("Test scores saved to 'results/tables/test_scores.csv'.")
    print(test_scores)

if __name__ == '__main__':
    test_and_deploy()

# In terminal at root directory of the project:
# python script/test_and_deploy.py results/models/best_model.pkl data/Processed/x_test_w.csv data/Processed/y_test_w.csv