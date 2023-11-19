# Portugal White Wine Quality Predictor


## Authors
- Kittipong Wongwipasamitkun
- Nicole Tu
- Sho Inagaki


## Summary of the Project
Lab1 Data analysis project for DSCI 522 (Data Science workflows); a course in the Master of Data Science program (2023-2024) at the University of British Columbia.


## About
We tried to make the classification model using the Polynomial Regression with Ridge Regularization algorithm with Randomized Search Hyperparameters which can predict Portugal white wine quality rating (on scale 0-10) through the physicochemical properties of the test wine. The model has trained on the Portugal white wine data set with 4898 observations. In the conclusion, the model performance is not quite good enough both on training data and on an unseen test data set with the test score at around 0.32 with the average train $R^2$ at 0.35 and the average test $R^2$ at 0.27 also with high root MSE and MSE (Mean Squared Error).

This data set used in this project is related to white vinho verde wine samples from the north of Portugal created By P. Cortez, A. Cerdeira, Fernando Almeida, Telmo Matos, J. Reis. 2009. The dataset was sourced from  website for downloading these datasets is the UC Irvine Machine Learning Repository (https://archive.ics.uci.edu/dataset/186/wine+quality). In addition, these datasets stored the physicochemical properties data on wines and the quality rating to compare and make the quality prediction model.


## Report
The final report can be found here (https://github.com/UBC-MDS/DSCI_522_group16/tree/main/src/portugal_wine_quality_predictor.html).


## Example Usage
To run the project first time, you should be set up the environment by run the following from the root of this repository:

conda env create --file environment.yml

To run this Portugal Wine Quality Predictor project analysis, run the following from the root of this repository:

conda activate portugal_white_wine_quality_predictor

jupyter lab 

Open src/portugal_white_wine_quality_predictor.ipynb in Jupyter Lab and under the "Kernel" menu click "Restart Kernel and Run All Cells...".


## List of Dependencies Needed
conda (version 23.9.0 or higher)
nb_conda_kernels (version 2.3.1 or higher)
Python and packages listed in environment.yml


## License
MIT License for the code.
The Report and the Portugal White Wine Quality Predictor materials here are licensed under a Creative Commons Attribution 4.0 International (CC BY 4.0) license. If re-using/re-mixing please provide attribution and link to this webpage.


## References
Cortez, P., Cerdeira, A., Almeida, F., Matos, T., & Reis, J. (2009). Modeling wine preferences by data mining from physicochemical properties. Decision Support Systems. DOI: https://doi.org/10.24432/C56S3T

Dua, Dheeru, and Casey Graff. 2019. “UCI Machine Learning Repository.” University of California, Irvine, School of Information; Computer Sciences. https://archive.ics.uci.edu/dataset/186/wine+quality.
