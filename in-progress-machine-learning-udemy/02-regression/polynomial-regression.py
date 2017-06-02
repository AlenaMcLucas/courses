### Polynomial Regression ###

## Data Preprocessing ##

# import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import Imputer   # for missing data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder   # for categorical data
from sklearn.cross_validation import train_test_split   # for train test split
from sklearn.preprocessing import StandardScaler   # for features scaling

# import dataset
dataset = pd.read_csv('Position_Salaries.csv')

# independent variables - level
# dependent variable - salary

X = dataset.iloc[:,1:2].values   # make X a matrix, not array
y = dataset.iloc[:,2].values

# no train test split because we don't have enough data

# no feature scaling needed because regression package takes care of it

## Linear Regression ##
from sklearn.linear_model import LinearRegression

lin_reg = LinearRegression()
lin_reg.fit(X, y)

## Polynomial Regression ##
from sklearn.preprocessing import PolynomialFeatures

poly_reg = PolynomialFeatures(degree = 4)
X_poly = poly_reg.fit_transform(X)
# creates a datset with column 0 = all 1s, 1 = x's, 2 = x^s, etc

# create regression
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y)

## Visualizations ##

# linear regression
plt.scatter(X, y, color = 'red')
plt.plot(X, lin_reg.predict(X), color = 'blue')
plt.title('Linear Regression')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

# polynomial regression
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
# 2 lines above plot contiuous curve, not straight lines between Xs/levels
plt.scatter(X, y, color = 'red')
plt.plot(X, lin_reg_2.predict(poly_reg.fit_transform(X)), color = 'blue')
plt.title('Polynomial Regression')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

## Predict ##

lin_reg.predict(6.5)   # given business question to predict 6.5 level salary
lin_reg_2.predict(poly_reg.fit_transform(6.5))