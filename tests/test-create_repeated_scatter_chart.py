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


# Import the count_classes function from the src folder
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.functions import create_repeated_scatter_chart

# Initialize test data frame
three_obs = pd.DataFrame({'a': [1,2,3],
                          'b': [2,3,4],
                          'c':[3,4,5]})


# Test for correct return type
def test_create_repeated_scatter_chart_returns_repeatplot():
    rslt = create_repeated_scatter_chart(three_obs, ["a", "b"])
    assert isinstance(rslt, alt.RepeatChart), "create_repeated_scatter_plot should return a altair repeat chart"

# Test for returning the correct plot
def test_create_repeated_scatter_chart_returns_correctplot():
    chart2 = alt.Chart(three_obs).mark_point(opacity=0.3, size=10).encode(
        alt.X(alt.repeat('row'), type='quantitative'),
        alt.Y(alt.repeat('column'), type='quantitative')
    ).properties(
        width=100,
        height=100
    ).repeat(
        column=["a", "b"],
        row=["a", "b"]
    )
    assert(chart2 == create_repeated_scatter_chart(three_obs, ["a", "b"]))