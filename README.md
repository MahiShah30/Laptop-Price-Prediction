Laptop Price Predictor: A Machine Learning Application

An end-to-end machine learning project that predicts laptop prices based on their specifications. The project includes data cleaning, feature engineering, model training with XGBoost, and deployment of a user-friendly web application using Streamlit.

Live Demo:
https://laptop-price-prediction-ml.streamlit.app/

Application Screenshot:

<img width="832" height="872" alt="image" src="https://github.com/user-attachments/assets/0d92d190-779f-4ec2-a69d-fee47604a87f" />

Project Overview:
This project aims to solve the common problem of estimating laptop prices based on a variety of features. It leverages a supervised machine learning model to provide real-time price predictions through an interactive web interface. The entire workflow, from raw data to a deployed application, is covered, making it an ideal showcase of a full-stack data science project.

Key Features:
Real-Time Prediction: Instantly get a price estimate based on user-selected specifications.
Multi-Currency Support: Predicts prices in multiple currencies (INR, USD, EUR) using real-time conversion.
User-Friendly Interface: A clean and simple UI built with Streamlit for easy interaction.
Highly Accurate Model: Utilizes a tuned XGBoost Regressor model for strong predictive performance.

Tech Stack:
Backend & Model: Python, Pandas, NumPy, Scikit-learn, XGBoost, Pickle
Frontend & Deployment: Streamlit, Streamlit Community Cloud
Development Environment: Google Colab, VS Code, Git & GitHub

Model Performance:
The final tuned XGBoost model achieved the following performance on the unseen test set:

R-squared (R²) Score: **0.838** (The model explains 84% of the variance in laptop prices)
Mean Absolute Error (MAE): **~$257** (The model's predictions are, on average, off by about €257)
