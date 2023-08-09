import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def find_lower_outliers1plushalf(column):
    Q1 = column.quantile(0.25)
    Q3 = column.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    
    return column[column < lower_bound]


def find_upper_outliers1plushalf(column):
    Q1 = column.quantile(0.25)
    Q3 = column.quantile(0.75)
    IQR = Q3 - Q1
    upper_bound = Q3 + 1.5 * IQR
    
    return column[column > upper_bound]

def find_lower_outliers3(column):
    Q1 = column.quantile(0.25)
    Q3 = column.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 3 * IQR
    
    return column[column < lower_bound]

def find_upper_outliers3(column):
    Q1 = column.quantile(0.25)
    Q3 = column.quantile(0.75)
    IQR = Q3 - Q1
    upper_bound = Q3 + 3 * IQR
    
    return column[column > upper_bound]

def find_outliers_2sigma(column):
    mean = column.mean()
    std_dev = column.std()
    lower_bound = mean - 2 * std_dev
    upper_bound = mean + 2 * std_dev
    
    return column[(column < lower_bound) | (column > upper_bound)]

def find_outliers_3sigma(column):
    mean = column.mean()
    std_dev = column.std()
    lower_bound = mean - 3 * std_dev
    upper_bound = mean + 3 * std_dev
    
    return column[(column < lower_bound) | (column > upper_bound)]