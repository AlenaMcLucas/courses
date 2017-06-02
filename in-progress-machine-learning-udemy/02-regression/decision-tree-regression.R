### Decision Tree Regression ###

# libraries
library(rpart)

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
regressor = rpart(formula = Salary ~ ., data = dataset, control = rpart.control(minsplit = 1))
summary(regressor)

## Visualizing ##
library(ggplot2)

# need high resolution because non-continuous
X_grid = seq(min(dataset$Level), max(dataset$Level), 0.01)
ggplot() + geom_point(aes(x = dataset$Level, y = dataset$Salary), color = 'red') + 
  geom_line(aes(x = X_grid, y = predict(regressor, newdata = data.frame(Level = X_grid))), color = 'blue') + 
  ggtitle('Decision Tree Regression') + 
  xlab('Level') + 
  ylab('Salary')

## Predictions ##

y_pred = predict(regressor, data.frame(Level = 6.5))
y_pred
