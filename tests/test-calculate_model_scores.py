import requests
import zipfile
from pathlib import Path
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import cross_validate
import pandas as pd
import altair as alt
import pytest
import sys
import os
from sklearn.linear_model import Ridge


# Import the count_classes function from the src folder
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.functions import calculate_model_scores

# Test data
ten_obs = pd.DataFrame({'a': [1,2,3,4,5,6,7,8,9,10],
                          'b': [2,3,4,5,6,7,8,9,10,11],
                          'c':[3,4,5,6,7,8,9,10,11,12]})


input_as_list = [1,2,3,4,5,6,7,8,9,10]

# Testing if the calculate_model_scores returns a data frame
def test_calculate_model_scores_returns_dataframe():
    X_train = ten_obs.drop(columns=["c"])
    y_train = ten_obs["c"]
    r = Ridge()
    rslt = calculate_model_scores(r, X_train, y_train, scoring_metrics=None)
    assert isinstance(rslt, pd.DataFrame), "calculate_model_scores should return a panda's data frame"


# Testing if the calculate_model_score function returns the correct number of rows and columns. 
# Rows = 10 (fit time + score time + 4 default metrics for both test and train), Cols = 5 (for 5 CV folds)
def test_calculate_model_scores_returns_dataframe():
    X_train = ten_obs.drop(columns=["c"])
    y_train = ten_obs["c"]
    r = Ridge()
    rslt = calculate_model_scores(r, X_train, y_train, scoring_metrics=None)
    assert rslt.shape[0] == 10, "The output dataframe has to contain 10 rows"
    assert rslt.shape[1] == 5, "The output dataframe has to contain 5 cols"

# Test for correct error handling for incorrect data object
# Not a panda's data frame
def test_calculate_model_scores_value_error():
    with pytest.raises(ValueError):
        y_train = ten_obs["c"]
        r = Ridge()
        calculate_model_scores(r, input_as_list, y_train, scoring_metrics=None)