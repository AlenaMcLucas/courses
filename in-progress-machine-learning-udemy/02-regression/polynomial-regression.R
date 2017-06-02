### Polynomial Regression ###

## Data Preprocessing ##

# import dataset
dataset = read.csv("Position_Salaries.csv")

# independent variable - level
# dependent variables - salary

# delete position variable
dataset = dataset[2:3]

# no train test split because dataset too small

# no feature scaling bc simple linear regression package/fit takes care of feature scaling

## Regressions ##

# linear model
lin_reg = lm(formula = Salary ~ Level, data = dataset)
summary(lin_reg)

# polynomial
# create variables at whatever degrees you want
dataset$Level2 = dataset$Level^2
dataset$Level3 = dataset$Level^3
dataset$Level4 = dataset$Level^4

# model (same as linear, just different inputs)
poly_reg = lm(formula = Salary ~ ., data = dataset)
summary(poly_reg)

## Visualizing ##
library(ggplot2)

# linear regression
ggplot() + geom_point(aes(x = dataset$Level, y = dataset$Salary), color = 'red') + 
  geom_line(aes(x = dataset$Level, y = predict(lin_reg, newdata = dataset)), color = 'blue') + 
  ggtitle('Linear Regression') + 
  xlab('Level') + 
  ylab('Salary')

# polynomial regression
ggplot() + geom_point(aes(x = dataset$Level, y = dataset$Salary), color = 'red') + 
  geom_line(aes(x = dataset$Level, y = predict(poly_reg, newdata = dataset)), color = 'blue') + 
  ggtitle('Polynomial Regression') + 
  xlab('Level') + 
  ylab('Salary')

## Predictions ##

y_pred_lin = predict(lin_reg, data.frame(Level = 6.5))
y_pred_lin
y_pred_poly = predict(poly_reg, data.frame(Level = 6.5, Level2 = 6.5^2, Level3 = 6.5^3, Level4 = 6.5^4))
y_pred_poly
