MLOPs Pipeline
==============================

CI Steps for ML

Project Organization
------------
    ├── Makefile           <- Makefile for installation of all the dependencies using `make install` 
    ├── README.md          <- The top-level README for developers using this project.
    ├── data               <- tracked using dvc, only .dvc available on github, actual data linked with google drive using dvc
    ├── models             <- Trained and pickled models
    ├── reports            <- Generated train and test metrics and tracked using dvc
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment
    ├── src                <- Source code for use in this project.
    │   ├── train.py       <- for training the model and storing the model file, logging the training metrics
    │   └── test.py        <- for testing the model and tracking the model metrics using dvc
    ├── .github/workflows  <- train.yaml file for triggering installations, model error calculations and logging using dvc
    ├── .dvc               <- contains dvc remote storage configuration (google drive)
    ├── dvc.yaml           <- dvc repro stages - model training, model testing, metrics loggging 
    └── dvc.lock           <- dvc repro stages meta data info

--------

Features 
1. Github integration of all the development files : Continuos Integration
2. CookieCutter format for organizing the repository
3. Github workflows for triggering commands on every push 
4. DVC integration 
5. Tracking of train.csv and test.csv using DVC, added google drive as remote storage 
6. Stages defined with train, test and metrics. Metrics tracked by DVC
7. dvc repro in github workflow for tracking metrics from different ML experiments facilitating continuous machine learning
