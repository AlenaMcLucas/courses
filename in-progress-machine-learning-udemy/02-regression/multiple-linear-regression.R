### Multiple Linear Regression ###

## Data Preprocessing ##

# import dataset
dataset = read.csv("50_Startups.csv")

# independent variable - profit
# dependent variables - all other variables

# categorical variable
dataset$State = factor(dataset$State, levels = c('New York', 'California', 'Florida'),
                         labels = c(1, 2, 3))

# train test split
library(caTools)
set.seed(123)

split = sample.split(dataset$Profit, SplitRatio = 0.8)
train_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# feature scaling
# simple linear regression package/fit takes care of feature scaling

## Simple Linear Regression ##

# could also write formula = Profit ~ R.D.Spend + Administration + Marketing.Spend + State
regressor = lm(formula = Profit ~ ., data = train_set)
summary(regressor)

## Predicting Test Set Results ##

y_pred = predict(regressor, newdata = test_set)
y_pred   # see results

## Visualize the Results ##

# can't visualize because we have more than one independent variable

## Backwards Elimination ##

regressor = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend + State,
               data = dataset)   # change from train to dataset to get all data's input on significance
summary(regressor)

# remove State2
regressor = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend + factor(State, exclude = 2),
               data = dataset)
summary(regressor)

# remove State/State3
regressor = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend, data = dataset)
summary(regressor)

# remove Administration
regressor = lm(formula = Profit ~ R.D.Spend + Marketing.Spend, data = dataset)
summary(regressor)

# remove Marketing.Spend
regressor = lm(formula = Profit ~ R.D.Spend, data = dataset)
summary(regressor)
