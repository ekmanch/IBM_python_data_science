#################################
# Model Development Lab         #
#################################


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/automobileEDA.csv'
df = pd.read_csv(path)
print(df.head())

# Uncomment to save the downloaded csv file
# df.to_csv('original_df.csv')

# load the modules for linear regression
from sklearn.linear_model import LinearRegression

#%%

# Linear Regression

#########################################
# Question 1a                           #
# Create a linear regression object?    #
#########################################

lm = LinearRegression()

#####################################################################
# Question 1b                                                       #
# Train the model using 'engine-size' as the independent variable   #
# and 'price' as the dependent variable?                            #
#####################################################################

X = df[['engine-size']]
Y = df['price']

yhat = lm.fit(X,Y)

#################################################
# Question 1c                                   #
# Find the slope and intercept of the model?    #
#################################################

print("Intercept of the linear regression model is: ", lm.intercept_)
print("Slope of the linear regression model is: ", lm.coef_)

#####################################################################################################
# Question 1d                                                                                       #
# What is the equation of the predicted line. You can use x and yhat or 'engine-size' or 'price'?   #
#####################################################################################################

yhat = lm.intercept_ + lm.coef_*df[['engine-size']]

#%%

# Multiple Linear Regression

#########################################################################
# Question 2a                                                           #
# Create and train a Multiple Linear Regression model "lm2"             #
# where the response variable is price,                                 #
# and the predictor variable is 'normalized-losses' and 'highway-mpg'.  #
#########################################################################

lm2 = LinearRegression()

Z = df[['normalized-losses', 'highway-mpg']]
Y = df['price']

lm2.fit(Z,Y)

#################################################
# Question 2b                                   #
# Find the coefficient of the model?            #
#################################################

print("The coefficients of the Multiple Linear Regression Model are: ", lm2.coef_)

#%%

# Model Evaluation Using Visualization

# import the visualization package: seaborn
import seaborn as sns

