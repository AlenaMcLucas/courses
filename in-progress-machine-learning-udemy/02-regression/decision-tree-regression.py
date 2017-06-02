### Decision Tree Regression ###

## Import libraries ##

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import Imputer   # for missing data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder   # for categorical data
from sklearn.cross_validation import train_test_split   # for train test split
from sklearn.preprocessing import StandardScaler   # for features scaling

## Import dataset(s) ##

dataset = pd.read_csv('Position_Salaries.csv')

# independent variables - level
# dependent variable - salary

X = dataset.iloc[:,1:2].values   # make X a matrix, not array
y = dataset.iloc[:,2].values

# no train test split because we don't have enough data

# no feature scaling needed because regression package takes care of it

## Decision Tree Regression ##
from sklearn.tree import DecisionTreeRegressor

regressor = DecisionTreeRegressor(random_state = 0)   # get same results
regressor.fit(X, y)

## Visualization ##

X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
# need 2 lines above for continuous model to see real results
plt.scatter(X, y, color = 'red')
plt.plot(X_grid, regressor.predict(X_grid), color = 'blue')
plt.title('Decision Tree Regression')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()
# splitting on every point, interval predictions for each level

## Prediction ##

y_pred = regressor.predict(6.5)
y_pred
