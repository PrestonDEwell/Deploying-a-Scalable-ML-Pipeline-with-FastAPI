Repository link: https://github.com/PrestonDEwell/Deploying-a-Scalable-ML-Pipeline-with-FastAPI

# Project Overview
This project involves developing a classification model using publicly available Census Bureau data. The primary goal is to monitor model performance across various data slices and deploy the model using FastAPI. The project encompasses a range of tasks from setting up GitHub Actions, understanding the data, to creating a RESTful API for model inference.

# How to Use
Below are instructions for setting up and using the Census Bureau Data Classification model on a Linux system using a Conda environment.

**Setting Up the Environment:**
1.	If needed install Anaconda or Miniconda from their official websites:
    *	Anaconda: https://www.anaconda.com/
    *	Miniconda: https://docs.conda.io/projects/miniconda/en/latest/miniconda-install.html
2.	Clone then navigate to the Repository:
    *	git clone https://github.com/udacity/Deploying-a-Scalable-ML-Pipeline-with-FastAPI
    *	cd Deploying-a-Scalable-ML-Pipeline-with-FastAPI
3.	Create and activate the Conda Environment:
    *	conda create -f environment.yml
    *	conda activate fastapi
4.	Install Dependencies:
    *	pip install -r requirements.txt

**Running the Machine Learning Model**
1.	Train the Model:
    *	python train_model.py
2.	Run Unit tests:
    *	pytest

**Using the API**
1.	Start the FastAPI Server:
    *	Uvicorn main: app –reload
2.	Open second CLI:
    *	python local_api.py

