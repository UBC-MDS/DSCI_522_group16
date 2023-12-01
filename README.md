# Portugal White Wine Quality Predictor


## Authors
- Kittipong Wongwipasamitkun
- Nicole Tu
- Sho Inagaki


## Summary of the Project
The Data analysis project for DSCI 522 (Data Science workflows); a course in the Master of Data Science program (2023-2024) at the University of British Columbia.


## About
We tried to make the classification model using the Polynomial Regression with Ridge Regularization algorithm with Randomized Search Hyperparameters which can predict Portugal white wine quality rating (on scale 0-10) through the physicochemical properties of the test wine. The model has trained on the Portugal white wine data set with 4898 observations. In the conclusion, the model performance is not quite good enough both on training data and on an unseen test data set with the test score at around 0.32 with the average train $R^2$ at 0.35 and the average test $R^2$ at 0.27 also with high root MSE and MSE (Mean Squared Error).

This data set used in this project is related to white vinho verde wine samples from the north of Portugal created By P. Cortez, A. Cerdeira, Fernando Almeida, Telmo Matos, J. Reis. 2009. The dataset was sourced from  website for downloading these datasets is the UC Irvine Machine Learning Repository (https://archive.ics.uci.edu/dataset/186/wine+quality). In addition, these datasets stored the physicochemical properties data on wines and the quality rating to compare and make the quality prediction model.


## Report
The final report can be found [here] (https://htmlpreview.github.io/?https://github.com/UBC-MDS/portugal_white_wine_quality_predictor_py/blob/main/src/portugal_white_wine_quality_predictor.html).


## Dependencies
We use [Docker] (https://docker.com) to build the container to manage the software dependencies for this project. This project's Docker image is based on the `quay.io/jupyter/minimal-notebook` image along with the specified additional dependencies in the [`Dockerfile`](Dockerfile), which called dependencies list from [`environment.yml`](environment.yml). 


## Usage

#### SET UP

To run the project first time, you should be  

1. [Install](https://www.docker.com/get-started/) and launch Docker on your computer.

2. Then you should clone this GitHub repository.


#### HOW TO RUN THE ANALYSIS

1. By using command line terminal, please go to the clone repository directory on your local machine and enter the following command:

``` 
docker compose up jupyter-lab
```

2. After executed the above command, in your terminal, please copy the URL that start with `http://127.0.0.1:8888/lab?token=` (as shown in the highlighted text in the example below) and paste it into your browser

<img src="img/jupyter-container-web-app-launch-url.png" width=400>

3. Run the analysis,
In the command terminal at the repository directory in your local machine, enter the following command:

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

running process need to add later

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#### Clean up (Shut down the container and clean up the resources) 

In the terminal where you used the container, type `Cntrl` + `C`, follow by type `docker compose rm`

> #### Note
> There is an alternative way via VS Code to run a one-time command within a service defined in a Docker Compose configuration file. 
> In VS Code, go to the repository folder and launch the container there by using the command:
>
> ```
> docker compose run --rm terminal bash
>```
>
> After finished, in the terminal, exit the container by type `exit`.


## Developer notes

#### Adding a new dependency

1. Add the new dependency to the `environment.yml` file, on which `DockerFile` file has linked to, on a new branch.

2. In your local machine, re-build the Docker image to ensure it builds and smoothly runs without any problem.

3. Push the changes to the remote repository (GitHub). 
   The new Docker image will be constructed and pushed to Docker Hub automatically.
   There will be tagged with SHA on this commit.

4. Update the new container image on your branch in the `docker-compose.yml` file (Ensure to update the tag specifically).

5. Merge the changes into the `main` branch by sending the pull request. 

#### Running the tests

At the repository directory, in the terminal, all tests are run by the `pytest` command. 
See more details on [`tests`](tests) directory.


## License
The code on portugal_wine_quality_predictor files are licensed under a MIT License. See the [the license file](LICENSE.md) for more information.

The Report and the Portugal White Wine Quality Predictor materials here are licensed under a [Creative Commons Attribution 4.0 International (CC BY 4.0)] (https://creativecommons.org/licenses/by-nc-sa/4.0/) license. See the [the license file](LICENSE.md).

If re-using/re-mixing please provide attribution and link to this webpage.


## References
Cortez, P., Cerdeira, A., Almeida, F., Matos, T., & Reis, J. (2009). Modeling wine preferences by data mining from physicochemical properties. Decision Support Systems. DOI: https://doi.org/10.24432/C56S3T

Dua, Dheeru, and Casey Graff. 2019. “UCI Machine Learning Repository.” University of California, Irvine, School of Information; Computer Sciences. https://archive.ics.uci.edu/dataset/186/wine+quality.

WSET Global. (n.d.). WSET systematic approach to tasting (SAT). Retrieved from https://www.wsetglobal.com/knowledge-centre/wset-systematic-approach-to-tasting-sat/ed: Mystery Tasting. (n.d.). WSET SAT explained. Retrieved from https://www.mysterytasting.com/wset-sat-explainace.

MDS-2023-24. (2023). MDS Lecture Notes on GitHub repository. Retrieved from https://github.ubc.ca/MDS-2023-24.

Fan, J. (1996). Local Polynomial Modelling and Its Applications: From linear regression to nonlinear regression. Monographs on Statistics and Applied Probability. Chapman & Hall/CRC. ISBN 978-0-412-98321-4.
