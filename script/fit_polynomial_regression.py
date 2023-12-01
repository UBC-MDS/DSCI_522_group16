import pandas as pd
from sklearn.externals import joblib  # Use joblib for saving the model
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.pipeline import make_pipeline
from sklearn.compose import make_column_transformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.linear_model import Ridge
import click
import os

@click.command()
@click.argument('train_file', type=click.Path(exists=True))
@click.argument('test_file', type=click.Path(exists=True))
def polynomial_regression(train_file, test_file):
    """
    Perform polynomial regression with hyperparameter tuning using Random Search.

    Parameters:
        - train_file (str): Path to the training CSV file.
        - test_file (str): Path to the test CSV file.

    Returns:
        None
    """
    # Load data
    white_train = pd.read_csv(train_file, sep=';')
    white_test = pd.read_csv(test_file, sep=';')

    # Drop redundant feature
    white_train = white_train.drop(columns=["free sulfur dioxide"])
    x_train_w, y_train_w = white_train.drop(columns=["quality"]), white_train["quality"]
    x_test_w, y_test_w = white_test.drop(columns=["quality"]), white_test["quality"]

    # Save data to the data/Processed folder
    processed_data_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'Processed')
    os.makedirs(processed_data_folder, exist_ok=True)
    
    x_train_w.to_csv(os.path.join(processed_data_folder, 'x_train_w.csv'), index=False)
    y_train_w.to_csv(os.path.join(processed_data_folder, 'y_train_w.csv'), index=False)
    x_test_w.to_csv(os.path.join(processed_data_folder, 'x_test_w.csv'), index=False)
    y_test_w.to_csv(os.path.join(processed_data_folder, 'y_test_w.csv'), index=False)

    # Polynomial regression setup
    numeric_transformer = make_pipeline(SimpleImputer(strategy="median"), StandardScaler())
    numeric_feats = x_train_w.columns.tolist()

    # Create a ColumnTransformer
    ct = make_column_transformer(
        (numeric_transformer, numeric_feats),  # Apply numeric transformer to numeric_feats
        (PolynomialFeatures(), numeric_feats)  # Apply poly_transformer to numeric_feats
    )

    Pipe_poly = make_pipeline(ct, Ridge())

    # Hyperparameter Tuning by Random Search
    param_dist = {
        "columntransformer__polynomialfeatures__degree": list(range(1, 8)),
        "ridge__alpha": np.logspace(-2, 2, 15)
    }

    random_search = RandomizedSearchCV(Pipe_poly, param_distributions=param_dist, n_iter=15, n_jobs=-1,
                                       return_train_score=True)

    # Fit the random search with training data
    random_search.fit(x_train_w, y_train_w)
    
   # Save the best model to the results/models/ directory
    model_output = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'results', 'models', 'best_model.joblib')
    os.makedirs(os.path.dirname(model_output), exist_ok=True)  # Create directory if it doesn't exist
    joblib.dump(random_search.best_estimator_, model_output)

    # Display the best hyperparameters
    print("Best Hyperparameters:")
    print(random_search.best_params_)

if __name__ == '__main__':
    polynomial_regression()

# In terminal at root directory of the project:
# python script/fit_polynomial_regression.py data/Processed/white_train.csv data/Processed/white_test.csv



