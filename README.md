# Portugal White Wine Quality Predictor


## Authors
- Kittipong Wongwipasamitkun
- Nicole Tu
- Sho Inagaki


## Summary of the Project
The Data analysis project for DSCI 522 (Data Science workflows); a course in the Master of Data Science program (2023-2024) at the University of British Columbia.


## About
We tried to make the classification model using the Polynomial Regression with Ridge Regularization algorithm with Randomized Search Hyperparameters which can predict Portugal white wine quality rating (on scale 0-10) through the physicochemical properties of the test wine. The model is trained on the Portugal white wine data set with 4898 observations. In the conclusion, the model performance is not quite good enough both on training data and on an unseen test data set with the test score at around 0.31 with the average train $R^2$ at 0.39 and the average test $R^2$  at 0.32. We also observed high root MSE and MSE (Mean Squared Error).

This data set used in this project is related to white vinho verde wine samples from the north of Portugal created By P. Cortez, A. Cerdeira, Fernando Almeida, Telmo Matos, J. Reis. 2009. The dataset was sourced from  website for downloading [these datasets is the UC Irvine Machine Learning Repository](https://archive.ics.uci.edu/dataset/186/wine+quality). In addition, these datasets stored the physicochemical properties data on wines and the quality rating to compare and make the quality prediction model.


## Report
The final report can be found [here](https://ubc-mds.github.io/portugal_white_wine_quality_predictor_py/portugal_white_wine_quality_predictor_report.html).


## Dependencies
We use [Docker](https://docker.com) to build the container to manage the software dependencies for this project. This project's Docker image is based on the `quay.io/jupyter/minimal-notebook` image along with the specified additional dependencies in the [`Dockerfile`](Dockerfile).


## Usage

This instruction guides you to reproduce the analysis

#### SET UP

To run the project first time, you should be  

1. [Install](https://www.docker.com/get-started/) and launch Docker on your computer.

2. Then you should clone this GitHub repository.


#### RUN THE ANALYSIS

1. By using command line terminal, please go to the clone repository directory on your local machine and enter the following command to reset the project to a clean state:

``` 
docker-compose run --rm analysis-env make clean
```

2. After executed the above command, at your terminal in your project root, please run this command to run all the entirety of the project:

``` 
docker-compose run --rm analysis-env make all
```

## Developer notes

#### Working by Jupyter Lab in the container

1. In the command terminal at the repository directory in your local machine, enter the following command:

``` 
docker-compose up analysis-env
```

2. After executed the above command, in your terminal, please copy the URL that start with ```http://127.0.0.1:8888/lab?token=``` and paste it into your browser

3. In your browser, you should see the Jupyter Lab IDE, with all the project files visible in the file browser panel on the left side of the screen.

#### Clean up (Shut down the container and clean up the resources)

Press Ctrl + C in the terminal where you set up the container, and then enter the following command:

``` 
docker-compose rm
```

#### Adding a new dependency

1. Adjust the dependency in the [`DockerFile`](Dockerfile) on a new branch.

2. You can try to test first by re-build the Docker image locally to make sure it can run properly without any problem.

3. Add commit push the changes Dockerfile to the GitHub and make a pull request to merge the changes into the main branch.

4. A new Dockerfile will build a new Docker image and will push to Docker Hub automatically.

5. It will update the new container image on your branch in the [`docker-compose.yml`](docker-compose.yml) file automatically as it stated as the latest.


#### Running the tests

At the repository directory, in the terminal, all tests are run by the `pytest` command. 
See more details on [`tests`](tests) directory.


## License
The code on portugal_wine_quality_predictor files are licensed under a MIT License. See the [the license file](LICENSE.md) for more information.

The Report and the Portugal White Wine Quality Predictor materials here are licensed under a [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/) license. See the [the license file](LICENSE.md).

If re-using/re-mixing please provide attribution and link to this webpage.


## References
Cortez, P., Cerdeira, A., Almeida, F., Matos, T., & Reis, J. (2009). Modeling wine preferences by data mining from physicochemical properties. Decision Support Systems. DOI: https://doi.org/10.24432/C56S3T

Dua, Dheeru, and Casey Graff. 2019. “UCI Machine Learning Repository.” University of California, Irvine, School of Information; Computer Sciences. https://archive.ics.uci.edu/dataset/186/wine+quality.

WSET Global. (n.d.). WSET systematic approach to tasting (SAT). Retrieved from https://www.wsetglobal.com/knowledge-centre/wset-systematic-approach-to-tasting-sat/ed: Mystery Tasting. (n.d.). WSET SAT explained. Retrieved from https://www.mysterytasting.com/wset-sat-explainace.

MDS-2023-24. (2023). MDS Lecture Notes on GitHub repository. Retrieved from https://github.ubc.ca/MDS-2023-24.

Fan, J. (1996). Local Polynomial Modelling and Its Applications: From linear regression to nonlinear regression. Monographs on Statistics and Applied Probability. Chapman & Hall/CRC. ISBN 978-0-412-98321-4.
