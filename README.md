# End-to-End-Machine-Leaning-Project-With-Mlow

## Wine Quality Prediction Project

 - This project focuses on predicting the quality of wines based on
   various chemical attributes. The **dataset** used in this **project**
   contains information about **red** and **white** variants of the **Portuguese**
   "*Vinho Verde*" wine. Machine learning models have been employed to
   predict the quality of the wine based on its chemical
   characteristics.

   


## Introduction

This project aims to explore and predict the quality of wine based on physicochemical tests. By utilizing machine learning algorithms, we strive to create models capable of accurately assessing wine quality using various attributes. This README provides an overview of the project structure, methodology, and steps to reproduce or contribute to this work.

## Dataset

The dataset used in this project contains information on red and white variants of the Portuguese "Vinho Verde" wine. It includes various chemical attributes such as acidity levels, residual sugar, pH, alcohol content, and more. Both red and white wine datasets are included, allowing for separate or combined analyses.

The dataset used can be found in the `data` directory within this repository. Due to confidentiality and proprietary rights, the source of the dataset cannot be disclosed.

## Features

The features available in the dataset include:

-   Fixed acidity
-   Volatile acidity
-   Citric acid
-   Residual sugar
-   Chlorides
-   Free sulfur dioxide
-   Total sulfur dioxide
-   Density
-   pH
-   Sulphates
-   Alcohol
-   Quality (target variable)

```mermaid

```


## Methodology / Work-Flow

```mermaid
graph TD;
    A[Start] --> B(Update schema.yaml)
    B --> C(Update params.yaml)
    C --> D(Update the entity)
    D --> E(Update the configuration manager in src config)
    E --> F(Update the components)
    F --> G(Update the pipeline)
    G --> H(Update the main.py)
    H --> I(Update the app.py)
    I --> J[End]

    style A fill:#85C1E9,stroke:#3498DB
    style B fill:#85C1E9,stroke:#3498DB
    style C fill:#85C1E9,stroke:#3498DB
    style D fill:#85C1E9,stroke:#3498DB
    style E fill:#85C1E9,stroke:#3498DB
    style F fill:#85C1E9,stroke:#3498DB
    style G fill:#85C1E9,stroke:#3498DB
    style H fill:#85C1E9,stroke:#3498DB
    style I fill:#85C1E9,stroke:#3498DB
    style J fill:#58D68D,stroke:#196F3D,stroke-width:2px


```

<details>
<summary>Sample Images from the project</summary>
<img src="https://github.com/Zaheer-10/End-to-End-Machine-Leaning-Project-With-Mlow/blob/main/static/assets/img/demo1.png" alt="image 1" width="300" height="200">
<img src="https://github.com/Zaheer-10/End-to-End-Machine-Leaning-Project-With-Mlow/blob/main/static/assets/img/demo3.png" alt=" image 2" width="300" height="200">
<img src="https://github.com/Zaheer-10/End-to-End-Machine-Leaning-Project-With-Mlow/blob/main/static/assets/img/demo3.png" alt=" image 3" width="300" height="200">
</details>


## Usage

To run this project locally, follow these steps:
### Step 1:  Clone the repository

```bash
https://github.com/Zaheer-10/End-to-End-Machine-Leaning-Project-With-Mlow
```

### STEP 2: Create a conda environment after opening the repository

```bash
conda create -n ML_project python=3.10 -y
```

```bash
conda activate ML_project
```

### STEP 3- Install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)
#### commands for mlflow_ui

1. Open [Dagshub](https://dagshub.com).
2. Connect with your github repo.
3. Copy these detailes
> MLFLOW_TRACKING_URI= your tracking uri
> MLFLOW_TRACKING_USERNAME= username 
> MLFLOW_TRACKING_PASSWORD=password 
> python script.py
4. Open gitbash
5. Run this to export as env variables:
```bash
export MLFLOW_TRACKING_URI=your uri
export MLFLOW_TRACKING_USERNAME=username
export MLFLOW_TRACKING_PASSWORD=password
```


## AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

 #### With specific access

 1. EC2  access: It is a virtual machine

2. ECR: Elastic Container registry to save your docker image in AWS.


 #### Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	
	-> Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
### 3. Create ECR repo to store/save docker image
    - Save the URI: 566373416292.dkr.ecr.ap-south-1.amazonaws.com/ML_project

	
###  4. Create EC2 machine (Ubuntu) 

### 5. Open EC2 and Install docker in EC2 Machine:
	
	
	-> optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	-> required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
###  6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


####  7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app




## About MLflow 
**MLflow**

 - Its Production Grade
 - Trace all of your expriements
 - Logging & tagging your model

