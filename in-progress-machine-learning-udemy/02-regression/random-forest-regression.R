### Random Forest Regression ###

# libraries
library(randomForest)

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

# random forest
set.seed(1234)
regressor = randomForest(x = dataset[1], y = dataset$Salary, ntree = 500)
# dataset[1] returns a dataset, dataset$Salary returns a vector
# increasing trees tends to improve accuracy
summary(regressor)

## Visualizing ##
library(ggplot2)

# need high resolution because non-continuous
X_grid = seq(min(dataset$Level), max(dataset$Level), 0.01)
ggplot() + geom_point(aes(x = dataset$Level, y = dataset$Salary), color = 'red') + 
  geom_line(aes(x = X_grid, y = predict(regressor, newdata = data.frame(Level = X_grid))), color = 'blue') + 
  ggtitle('Random Forest Regression') + 
  xlab('Level') + 
  ylab('Salary')

## Predictions ##

y_pred = predict(regressor, data.frame(Level = 6.5))
y_pred
