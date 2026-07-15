# House Price Prediction
Predicting the house market price using the machine learning regression algotithum
## Project Overview
The project is the analyze the house feature and build a model that can predict the price of a house
## Dataset Features
The dataset contain the following features:
- Bedrooms
- Bathrooms
- SquareFeet
- YearBuilt
- GarageSpaces
- CrimeRate
- SchoolRating
- ZipEncoded
 Target Variable :
- Price
## Data Preprocessing
The following preprocessing steps were performed:
- Loaded the dataset
- checked missing values
- Dropped unnecsaary column 
- Convert zip code into numerical coding
- prepared data for machine learning models
## Machine learning Models
The following regression models were trained and compared
1. Linear Regression 
2. K-Nearest Neighbors Regreesor
3. Decision Tree Regressor 
4. Random Forest Regressor
## Model Evaluation 
Model are evaluated using:
- R2 score 
- MSE (Mean Squared Error)
- MAE (Mean Absolute Error)
Example Comparison :
## 🏆 Model Evaluation

Models were evaluated using:

- **R² Score** (higher is better)
- **Mean Absolute Error (MAE)** (lower is better)
- **Mean Squared Error (MSE)** (lower is better)

| Model | R² Score | MAE | MSE |
|---|---:|---:|---:|
| Linear Regression | 1.0000 | 0.000000000168 | 0.0000000000000000000465 |
| KNeighbors Regressor | 0.8148 | 88,607.28 | 11,957,660,395.66 |
| Decision Tree Regressor | 0.9987 | 5,724.27 | 81,447,721.77 |
| Random Forest Regressor | 0.9998 | 3,109.33 | 15,558,211.06 |


## Best Model 
Random Forest Regressor was selected as the final model because it provide the best performance

**Note:**
While linear Regression shows the R2=1.0  means the prefect score this typically due to data leakage or overfitted
or another hand Random forest model is the best they are nearly to the one or mae or mse is the best to the another