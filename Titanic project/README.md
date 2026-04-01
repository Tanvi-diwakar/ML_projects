# Titanic Survival Prediction using Scikit-Learn Pipeline

## Overview

This project predicts whether a passenger **survived the Titanic disaster** using machine learning techniques.

The primary objective is to demonstrate how **Scikit-Learn Pipelines** can be used to build a clean, scalable, and reproducible machine learning workflow that integrates preprocessing and model training.

---

## Importance of the Project

This project highlights several important machine learning concepts used in real-world data science workflows:

- Demonstrates how to build **end-to-end machine learning pipelines** using Scikit-learn.
- Shows how to handle **missing values and categorical variables** efficiently.
- Improves **model reproducibility and maintainability** by integrating preprocessing and training steps.
- Provides practical experience working with a **historical dataset widely used in machine learning education**.
- Helps understand how passenger attributes such as **age, class, and gender influence survival probability**.

This project serves as a strong foundation for understanding **structured data classification problems and production-ready ML pipelines**.

---

## Problem Statement

Using passenger attributes, predict whether a passenger survived the Titanic disaster.

### Target Variable

| Value | Description |
|------|-------------|
| 1 | Survived |
| 0 | Did Not Survive |

---

## Dataset

The dataset includes passenger information such as:

| Feature | Description |
|-------|-------------|
| Pclass | Passenger class |
| Sex | Gender |
| Age | Passenger age |
| Fare | Ticket fare |
| Embarked | Port of embarkation |
| Survived | Target variable |

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Jupyter Notebook

### Key Libraries

- ColumnTransformer
- Pipeline
- SimpleImputer
- OneHotEncoder

---

## Machine Learning Pipeline

The pipeline includes the following steps:

1. Handling missing values using **SimpleImputer**
2. Encoding categorical variables using **OneHotEncoder**
3. Feature transformation using **ColumnTransformer**
4. Training the classification model

Using a pipeline ensures that **data preprocessing and model training are combined into a single workflow**, improving efficiency and reproducibility.

---

## Project Workflow

1. Data Loading  
2. Data Cleaning  
3. Feature Engineering  
4. Pipeline Creation  
5. Model Training  
6. Model Evaluation  
