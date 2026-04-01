# Time Series Forecasting using LSTM

## Project Overview

This project demonstrates Time Series Forecasting using a Long Short-Term Memory (LSTM) neural network. The model predicts future airline passenger numbers using historical monthly passenger data.

LSTM networks are a type of Recurrent Neural Network (RNN) that are designed to capture long-term dependencies in sequential data, making them highly suitable for time series prediction tasks.

This project showcases how deep learning techniques can be applied to analyze trends and forecast future values in time series datasets.

---

## Objectives

- Understand time series forecasting using deep learning
- Implement an LSTM-based neural network
- Train a model on historical airline passenger data
- Visualize predictions and compare them with actual values

---

## Dataset

The project uses the Airline Passengers Dataset which contains monthly totals of international airline passengers.

Dataset Features:

Month – Time period  
Passengers – Total number of airline passengers

This dataset is widely used for demonstrating time series forecasting models.

---

## Technologies Used

Python  
NumPy  
Pandas  
Matplotlib  
Scikit-learn  
TensorFlow / Keras  
Jupyter Notebook

---

## Project Workflow

1. Data Loading  
The dataset is loaded using Pandas and converted into numerical format for modeling.

2. Data Preprocessing  
The data is normalized using MinMaxScaler to improve model performance.  
The dataset is then split into training and testing sets.

3. Creating Time Series Dataset  
A helper function is used to transform the dataset into a supervised learning format where previous time steps are used to predict future values.

4. Reshaping the Data  
The input data is reshaped into the format required by LSTM models:  
Samples, Time Steps, Features.

5. Model Architecture  

The model contains:
- LSTM Layer
- Dense Output Layer

Loss Function: Mean Squared Error  
Optimizer: Adam

6. Model Training  

The model is trained using:
- 100 epochs
- Batch size = 1

7. Predictions and Visualization  

The trained model generates predictions for both training and testing datasets.  
The results are visualized using plots comparing actual and predicted values.

---

## Results

The LSTM model successfully learns patterns from historical passenger data and produces predictions that follow the general trend of the dataset.

This demonstrates the capability of deep learning models to perform time series forecasting.

---

## How to Run the Project

1. Clone the Repository

git clone https://github.com/yourusername/time-series-lstm.git

2. Navigate to the Project Directory

cd time-series-lstm

3. Install Required Libraries

pip install numpy pandas matplotlib scikit-learn tensorflow keras

4. Run the Notebook

Open the Jupyter Notebook file:

Time_Series_with_LSTM.ipynb

Run all cells to train the model and view the results.

---

## Project Structure

time-series-lstm

airline-passengers.csv  
Time_Series_with_LSTM.ipynb  
README.md

---

## Key Concepts Demonstrated

Time Series Forecasting  
Deep Learning for Sequential Data  
LSTM Neural Networks  
Data Scaling and Preprocessing  
Model Evaluation and Visualization
