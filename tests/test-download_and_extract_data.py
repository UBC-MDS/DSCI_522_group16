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
from src.functions import download_and_extract_data


# Test to make sure the input, url is actually a URL
def test_download_and_extract_data_is_URL():
    try:
        download_and_extract_data(23948302,392010393)
    except requests.exceptions.MissingSchema:
        print("The URL has to contain 'https://'")

# Test for URL validation. Is URL actually accessible 
def test_download_and_extract_data():
    try:
        download_and_extract_data("https://239a48302.ca",392010393)
    except requests.exceptions.ConnectionError:
        print("Make sure that URL provided is valid.")

# Test for correct input type for target_folder
# (Make sure they are of string type) 
def test_count_classes_attribute_error():
    try:
        download_and_extract_data("https://github.com/ttimbers/canlang/raw/master/inst/extdata/victoria_lang.tsv"
    , 392010393)
    except TypeError:
        print("The target_folder has to be a string")