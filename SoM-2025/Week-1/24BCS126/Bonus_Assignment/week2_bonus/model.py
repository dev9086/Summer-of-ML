import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def load_data(filepath):
    df= pd.read_csv(filepath)
    return df.dropna()



def linear_regression(x,y):
    n= np.size(x)
    x_mean = np.mean(x)
    y_mean = np.mean(y)

    # Sum of cross deviation
    sumxy = np.sum(x*y) - n * x_mean * y_mean

    # Sum of squares of deviations
    sumxx = np.sum(x*x) - n * x_mean * x_mean

    # Calculating regression coefficients
    b1 = sumxy / sumxx
    b0 = y_mean - b1 * x_mean
    return (b0,b1)
  
  
def train_models(filepath):
    df= load_data(filepath)
    
    b0cf,b1cf = linear_regression(df['cc_rating'],df['cf_rating'])
    
    b0cc,b1cc = linear_regression(df['cf_rating'],df['cc_rating'])
    
    return (b0cf,b1cf),(b0cc,b1cc)