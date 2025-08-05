# 🚗 Car Price Predictor

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Status](https://img.shields.io/badge/status-Active-brightgreen)

A full-stack machine learning project to predict car prices using advanced regression techniques. Includes model training, deployment with Flask and/or Streamlit, and optional data visualization dashboards.

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Demo & Features](#-demo--features)
- [Dataset & Preprocessing](#-dataset--preprocessing)
- [Modeling](#-modeling)
- [Web & Interactive UI](#-web--interactive-ui)
- [Visualization Dashboard](#-visualization-dashboard)
- [Usage](#-usage)
- [Deployment](#-deployment)
- [Project Structure](#-project-structure)
- [Contributing](#-contributing)
- [License](#-license)
- [Acknowledgments](#-acknowledgments)

---

## 🧠 Overview

**Car Price Predictor** is a machine learning web app that predicts the selling price of a used car based on parameters like year, kilometers driven, fuel type, transmission, mileage, engine power, and more.

---

## 🎯 Demo & Features

### 🚀 Features

- 🔍 Predict car price using machine learning (Random Forest, Linear Regression, etc.)
- 📈 Model performance metrics shown (MAE, R², RMSE)
- 📊 Visualizations for EDA and feature importance
- 🧪 Clean UI with real-time prediction
- 🧠 Trained ML model saved using `joblib` or `pickle`

> ✅ *Interactive prediction interface using Streamlit or Flask web form.*

---

## 📊 Dataset & Preprocessing

- 📂 Dataset: Used Cars Dataset (from CarDekho or similar source)
- 🔑 Key Features:
  - Year
  - Present Price
  - Kms Driven
  - Fuel Type
  - Transmission
  - Owner
  - Mileage
  - Engine
  - Seats

### 🛠️ Preprocessing Steps

- Handling missing values
- Label encoding categorical variables
- Removing outliers
- Feature scaling and transformation
- Train-test split (e.g., 80/20)

---

## ⚙️ Modeling

- Algorithms Tested:
  - Linear Regression
  - Lasso Regression
  - Random Forest Regressor (✅ Best Performance)
  - Gradient Boosting

### 🧪 Evaluation Metrics

- R² Score
- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)

---

## 🌐 Web & Interactive UI

| Component | Technology |
|----------|------------|
| 🔙 Backend | Flask API (`app.py`) |
| 🧑 Frontend | Streamlit App / HTML Form |
| 💾 Model | Trained and saved as `model.pkl` |
| 🧪 Testing | Manual UI testing + Postman |

### 📌 API Endpoint Example

```bash
POST /predict
Content-Type: application/json
{
  "year": 2015,
  "kms_driven": 45000,
  "fuel_type": "Petrol",
  "transmission": "Manual",
  "mileage": 18.5,
  "engine": 1200,
  "seats": 5
}
