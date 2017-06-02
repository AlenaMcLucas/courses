### Data Preprocessing Template ###

## Import libraries ##

## Import dataset(s) ##

# in 'Files' tabe make sure you set your working directory (find dataset, click gear/More)
# OR
# setwd("~/data-science/Udemy-notes/machine-learning/01-data-preprocessing")
dataset = read.csv("Data.csv")

## Idenify independent + dependent variables ##

# independent variables - are country, age and salary
# dependent variable - purchased or not?

## Missing data ##

# if condition is true, then do the second parameter to it, if not do third parameter
# second parameter: average of Age column, add function to calculate mean and na.rm inclusdes missing data in mean calculation
# dataset$Age = ifelse(is.na(dataset$Age),
#                      ave(dataset$Age, FUN = function(x) mean(x, na.rm = TRUE)),
#                      dataset$Age)

# a better way to calculate this would be to subset the data and average only Spanish ages and German salaries
dataset$Age = ifelse(is.na(dataset$Age),
                        ave(dataset$Age, dataset$Country, FUN = function(x) mean(x, na.rm = TRUE)),
                        dataset$Age)

dataset$Salary = ifelse(is.na(dataset$Salary),
                        ave(dataset$Salary, dataset$Country, FUN = function(x) mean(x, na.rm = TRUE)),
                        dataset$Salary)

## Categorical data ##

# factor() creates a column of vectors, which act as dummy variables
# c is a vector of three elements
# labels don't really matter
dataset$Country = factor(dataset$Country, levels = c('France', 'Spain', 'Germany'),
                         labels = c(1, 2, 3))

dataset$Purchased = factor(dataset$Purchased, levels = c('No', 'Yes'), labels = c(0, 1))

## Splitting dataset(s) into training + testing sets ##

# install.packages("caTools")
library(caTools)
set.seed(123)   # get same results as instructor

# SplitRatio is % for test set
split = sample.split(dataset$Purchased, SplitRatio = 0.8)
train_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

## Feature scaling ##

# no features scaling to factors because they aren't viewed as numeric
train_set[,2:3] = scale(train_set[,2:3])
test_set[,2:3] = scale(train_set[,2:3])
