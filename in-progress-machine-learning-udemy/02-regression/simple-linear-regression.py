### Simple Linear Regression ###

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
dataset = pd.read_csv('Salary_Data.csv')

# dependent variable - years experience
# independent variable - salary

X = dataset.iloc[:,0].values
y = dataset.iloc[:,1].values

# train test split
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size = float(1)/3,
                                                    random_state = 0)

# if one feature, need to do this
X_train = X_train.reshape(-1, 1)
X_test = X_test.reshape(-1, 1)

## Simple Linear Regression Model ##

# import libraries
from sklearn.linear_model import LinearRegression

# create LinearRegression object + fit
regressor = LinearRegression()
regressor.fit(X_train, y_train)

## Predicting the Test Set ##

y_pred = regressor.predict(X_test)

## Visualizing the Results ##

# training set results
plt.scatter(X_train, y_train, color = 'red')
# line is based on X_train and the model's predicted y values for X_train
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Training Set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()   # ready to plot graph

# test set results
plt.scatter(X_test, y_test, color = 'red')
# same line
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Test Set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()   # ready to plot graph
