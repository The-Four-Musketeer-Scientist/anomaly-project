import pandas as pd
import numpy as np
import os


def get_log_data():
    df = pd.read_csv('anonymized-curriculum-access.txt', sep=' ', header=None,
                     names=['Timestamp', 'Resource', 'User_ID', 'Access_Type', 'IP_Address'])
    return df
    




#---------------------------------------------PREP-----------------------------------------------------    

def prep_log_data(df):
    
    '''
    This function preps the data from get_crime_data and does the necessary step to cleaning the dataframe
    '''
    
    
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True) 
    df = df.resample('D')['path'].count()
    
    
    return df    



