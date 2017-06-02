### Support Vector Regression ###

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

# feature scaling needed because SVR doesn't takes care of it
X = X.reshape(-1, 1)
y = y.reshape(-1, 1)

sc_X = StandardScaler()
X = sc_X.fit_transform(X)

sc_y = StandardScaler()
y = sc_y.fit_transform(y)

## Support Vector Regression ##
from sklearn.svm import SVR

regressor = SVR(kernel = 'rbf') # rbf = most popular gaussian kernel
regressor.fit(X, y)

## Visualization ##

# linear regression
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color = 'red')
plt.plot(X_grid, regressor.predict(X_grid), color = 'blue')
plt.title('Support Vector Regression')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

## Predict ##

y_pred = sc_y.inverse_transform(regressor.predict(sc_X.transform(np.array([[6.5]]))))
y_pred
