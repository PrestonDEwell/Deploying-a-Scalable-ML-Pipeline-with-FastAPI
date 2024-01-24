import pytest
import numpy as np
import pandas as pd
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Import functions from train_model.py
from ml.data import process_data
from ml.model import compute_model_metrics, inference, train_model

project_path = "/mnt/c/Users/prest/Deploying-a-Scalable-ML-Pipeline-with-FastAPI"
data_path = os.path.join(project_path, "data", "census.csv")

data = pd.read_csv(data_path)

train, test = train_test_split(data, test_size=0.2, random_state=42)

# DO NOT MODIFY
cat_features = [
    "workclass",
    "education",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "native-country",
]

# use the process_data function provided to process the data.
X_train, y_train, encoder, lb = process_data(
    train, categorical_features=cat_features, label="salary", training=True)

X_test, y_test, _, _ = process_data(
    train, categorical_features=cat_features, label="salary", training=False, encoder=encoder, lb=lb)

# Test for Expected Result Type
def test_inference_result_type():
    """
    Test if the inference function returns an array.
    """
    model = train_model(X_train, y_train)
    preds = inference(model, X_test)
    assert isinstance(preds, np.ndarray), "Inference should return a numpy array"


# Test for Using Expected Algorithm
def test_train_model_algorithm():
    """
    Test if the train_model function uses a RandomForestClassifier.
    """
    model = train_model(X_train, y_train)
    assert isinstance(model, RandomForestClassifier), "Model should be an instance of RandomForestClassifier"

# Test for Correct Metrics Values
def test_compute_model_metrics():
    """
    Test if compute_model_metrics returns the expected precision, recall, and fbeta.
    """
    model = train_model(X_train, y_train)
    preds = inference(model, X_test)
    precision, recall, fbeta = compute_model_metrics(y_test, preds)
    assert isinstance(precision, float) and isinstance(recall, float) and isinstance(fbeta, float), "Metrics should be floating-point numbers"
