all: report/_build/html/index.html
# target = final output of a script.py
# dependencies =  input files of the script.py + the script itself
# action: the terminal commend to run this script

# download and extract data. Need mannual unzip and put under data/Raw before next step.
data/Raw/wine+quality.zip : script/download_and_extract_data.py
    python script/download_and_extract_data.py https://archive.ics.uci.edu/static/public/186/wine+quality.zip data/Raw

# read_split_and_save data:
data/Processed/white_train.csv data/Processed/white_test.csv : data/Raw/winequality-white.csv script/read_split_and_save.py
    python script/read_split_and_save.py data/Raw/winequality-white.csv --dropna --info --split-data

#EDA:
results/figures/%.png: script/eda.py data/Processed/white_train.csv
	python script/eda.py data/Processed/white_train.csv

#Fit polynomial models:
data/Processed/x_train_w.csv data/Processed/x_test_w.csv data/Processed/y_train_w.csv data/Processed/y_test_w.csv results/models/best_model.pkl : \
    data/Processed/white_train.csv \
    data/Processed/white_test.csv \
    script/fit_polynomial_regression.py
    python script/fit_polynomial_regression.py data/Processed/white_train.csv data/Processed/white_test.csv

report/_build/html/index.html : report/count_report.ipynb \
report/_toc.yml \
report/_config.yml \
results/figure/isles.png \
results/figure/abyss.png 
    jupyter-book build report

clean :
# remove all .dat files in results directory
    rm -f results/*.dat   
# remove all .png fules in results.figure directory
    rm -f results/figure/*.png
    rm -rf report/_build

