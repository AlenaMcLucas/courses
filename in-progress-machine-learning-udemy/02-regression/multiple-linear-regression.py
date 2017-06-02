### Multiple Linear Regression ###

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
dataset = pd.read_csv('50_Startups.csv')

# dependent variable - profit
# independent variables - all other variables

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# see new variables
X
y

# encode categorical variable
labelencoder_state = LabelEncoder()
X[:, -1] = labelencoder_state.fit_transform(X[:, -1])
onehotencoder = OneHotEncoder(categorical_features = [-1])
X = onehotencoder.fit_transform(X).toarray()   # number -> dummy
X = X[:, 1:]   # avoid dummy variable trap, don't need for our python library

# train test split
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size = 0.2,
                                                    random_state = 0)

# no feature scaling because package does this for us

## Multivariate Regression Model ##

from sklearn.linear_model import LinearRegression

# create LinearRegression object + fit
regressor = LinearRegression()
regressor.fit(X_train, y_train)

## Predicting the Test Set ##

y_pred = regressor.predict(X_test)

## Visualizing the Results ##

# cannot plot model because there are multiple independent variables

## Backward Elimination ##

import statsmodels.formula.api as sm

# include x0 = 1, add column of 1s
X = np.append(arr = np.ones((50, 1)).astype(int), values = X,
              axis = 1)   # cast int

# fit model with all possible predictors
X_opt = X[:, [0, 1, 2, 3, 4, 5]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
# check p values
regressor_OLS.summary()

# remove index 2 because p-value = 0.990
X_opt = X[:, [0, 1, 3, 4, 5]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()

# remove index 1 because p-value = 0.940
X_opt = X[:, [0, 3, 4, 5]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()

# remove index 3 because p-value = 0.604
X_opt = X[:, [0, 3, 5]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()

# remove index 5 because p-value = 0.060
X_opt = X[:, [0, 3]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()
