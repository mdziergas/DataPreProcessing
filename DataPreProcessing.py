#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 00:06:13 2021

@author: marekdziergas
"""

# Imports
import pandas as pd
import numpy as np
#from sklearn.model_selection import train_test_split



# Load CSV into DataFrame
df = pd.read_csv("WineProcessed.csv",sep = ',')


# Create a data quality report
describe_df = df.describe()
missing_values = df.isna().sum()
counts = df.nunique()

# Find correlations
correlation_matrix = df.corr()


# Change any features that seem numeric but are categorical (ex. zip code)

# split into numeric and categorical
numeric_data = df.select_dtypes(include=[np.number])
categorical_data = df.select_dtypes(exclude=[np.number])

#skewness and kurtosis
kurt = numeric_data.kurtosis()
skew = numeric_data.skew()


df = pd.get_dummies(df)

df = df.interpolate(method ='linear', limit_direction ='forward')

df = df.dropna()





#X_train, X_test, y_train, y_test = train_test_split(predictors, target, test_size=0.33, random_state=42)

