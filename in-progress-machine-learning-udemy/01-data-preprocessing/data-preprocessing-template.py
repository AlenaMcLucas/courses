### Data Preprocessing Template ###

## Import libraries ##

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import Imputer   # for missing data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder   # for categorical data
from sklearn.cross_validation import train_test_split   # for train test split
from sklearn.preprocessing import StandardScaler   # for features scaling

## Import dataset(s) ##

dataset = pd.read_csv('Data.csv')

## Idenify independent + dependent variables ##

# independent variables - are country, age and salary
# dependent variable - purchased or not?

# take all rows, then all colums except last one; only values
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values
# returns arrays

## Missing data ##

# identifies missing if value is NaN, strategy is replace with column mean
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
# only fit to X's columns with missing data
imputer = imputer.fit(X[:,1:3])
X[:,1:3] = imputer.transform(X[:,1:3])

## Categorical data ##

# 3 dummy variables for Country
labelencoder_X = LabelEncoder()
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])   # category -> number
onehotencoder = OneHotEncoder(categorical_features = [0])
X = onehotencoder.fit_transform(X).toarray()   # number -> dummy

# boolean variable for Purchased Yes/No
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)

## Splitting dataset(s) into training + testing sets ##

# random state so we can get same results as instructor
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size = 0.2,
                                                    random_state = 0)

# if you only have one feature, you must run the code below:
# X_train = X_train.reshape(-1, 1)
# X_test = X_test.reshape(-1, 1)

## Feature scaling ##

sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
# fit X train first to learn scaling that should be applied, then since X test
# structure is the same you can directly apply the transform method

# we are scaling all variables including the dummies
