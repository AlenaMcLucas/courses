### Simple Linear Regression ###

## Data Preprocessing ##

# import dataset
dataset = read.csv("Salary_Data.csv")

# independent variable - years of experience
# dependent variable - salary

# train test split
library(caTools)
set.seed(123)

split = sample.split(dataset$Salary, SplitRatio = 2/3)
train_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# feature scaling
# simple linear regression package takes care of feature scaling

## Simple Linear Regression ##

regressor = lm(formula = Salary ~ YearsExperience, data = train_set)
summary(regressor)

## Predicting Test Set Results ##

y_pred = predict(regressor, newdata = test_set)

## Visualize the Results ##

# install.packages('ggplot2')
library(ggplot2)

# training set results
ggplot() + geom_point(aes(x = train_set$YearsExperience, y = train_set$Salary),
                      color = 'red') +
  geom_line(aes(x = train_set$YearsExperience, y = predict(regressor, newdata = train_set)),
            color = 'blue') + 
  ggtitle('Salary vs Experience (Training Set)') +
  xlab('Years of Experience') +
  ylab('Salary')

# test set results
ggplot() + geom_point(aes(x = test_set$YearsExperience, y = test_set$Salary),
                      color = 'red') +
  geom_line(aes(x = train_set$YearsExperience, y = predict(regressor, newdata = train_set)),
            color = 'blue') + 
  ggtitle('Salary vs Experience (Test Set)') +
  xlab('Years of Experience') +
  ylab('Salary')
