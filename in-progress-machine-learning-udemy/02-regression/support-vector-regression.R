### Support Vector Regression ###

# libraries
library(e1071)

## Data Preprocessing ##

# import dataset
dataset = read.csv("Position_Salaries.csv")

# independent variable - level
# dependent variables - salary

# delete position variable
dataset = dataset[2:3]

# no train test split because dataset too small

# no feature scaling bc simple linear regression package/fit takes care of feature scaling

## Regression ##

# support vector
regressor = svm(formula = Salary ~ ., data = dataset, type = 'eps-regression')   # gaussian
summary(regressor)

## Visualizing ##
library(ggplot2)

ggplot() + geom_point(aes(x = dataset$Level, y = dataset$Salary), color = 'red') + 
  geom_line(aes(x = dataset$Level, y = predict(regressor, newdata = dataset)), color = 'blue') + 
  ggtitle('Support Vector Regression') + 
  xlab('Level') + 
  ylab('Salary')

## Predictions ##

y_pred = predict(regressor, data.frame(Level = 6.5))
y_pred
