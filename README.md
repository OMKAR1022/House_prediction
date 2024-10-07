# Bangalore House Price Prediction

A machine learning model that predicts house prices in Bangalore based on various features. This project integrates the trained model with a Flask API, also connected to a Flutter application for mobile-based interactions.


## Table of Contents:-

Overview

Dataset

Model

Flask API Setup

Flutter Integration

Contributing

License



# Overview

The Bangalore House Price Prediction project uses machine learning to predict house prices in the Bangalore region. The model is trained using the Kaggle Bangalore House Price Prediction Dataset and is built using a Linear Regression algorithm. It achieves an accuracy of 81%.

In addition to training and testing the model, this project features a Flask API for interacting with the model and a Flutter application that communicates with the API to provide a mobile interface for predictions.


# Dataset

The dataset used for this project was sourced from Kaggle, containing various features relevant to house pricing in Bangalore
## Link to Dataset:
https://www.kaggle.com/datasets/amitabhajoy/bengaluru-house-price-data/data


# Model

We used a Linear Regression model for this project. After training the model, we achieved an accuracy of 81%.

Key Features of the Model:
Algorithm: Linear Regression
Training Accuracy: 81%
Evaluation Metrics: Mean Squared Error (MSE), R-Squared
Libraries Used:

sklearn

pandas

numpy

matplotlib

The trained model is saved and deployed on a Flask server for real-time predictions.


# Flask API Setup

The Flask API is responsible for serving the trained model and handling prediction requests via HTTP. You can use Postman or integrate the API into the Flutter app for predictions.

Flask API Endpoints:
POST /predict: Accepts input data (house features) and returns predicted house prices.



# Flutter Integration

The Flutter application provides a mobile interface to interact with the Flask API. Users can input house features such as the number of bedrooms, location, and area to predict the house price.

How It Works:
The user enters house data on the Flutter app.
The app sends a request to the Flask API.
The API returns a prediction, which is displayed on the app.

## Flutter_App_repo link : 
https://github.com/OMKAR1022/Flutter_App_House_Prediction

# Contributing

Contributions are welcome! Feel free to fork this repository, make changes, and submit a pull request. 

# License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/OMKAR1022/House_prediction/blob/main/LICENSE)  file for details.

