# End-to-End-Machince-Learning-and-MLOps-project-with-MLflow


## Workflows

1. Update config.ymal
2. Update schema.yaml
3. Update params.yaml
4. update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the app.py
 

# How to run?

### STEPS:

clone the respository

```bash
https://github.com/sat-kum/End-to-End-Machince-Learning-and-MLOps-project-with-MLflow
```

### STEP 01- Create a conda enviroment after opening the respository

```bash
conda create -n env_name python=3.8 -y
```

```bash
conda activate env_name
```


### STEP 02- install the requirements
```bash
pip install -r requirments.txt
```


```bash
# Finally run the following command
python app.py


Now,
```bash
open up you host and port
```

## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)


##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/satkum161997/End-to-End-Machince-Learning-and-MLOps-project-with-MLflow.mlflow \
MLFLOW_TRACKING_USERNAME=satkum \
MLFLOW_TRACKING_PASSWORD=3b54a2d6452213f49cae6ae2d020f903f50976c9 \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/satkum/End-to-End-Machince-Learning-and-MLOps-project-with-MLflow.mlflow

export MLFLOW_TRACKING_USERNAME=satkum 

export MLFLOW_TRACKING_PASSWORD=3b54a2d6452213f49cae6ae2d020f903f50976c9




