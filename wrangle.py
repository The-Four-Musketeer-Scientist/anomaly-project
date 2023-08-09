import pandas as pd
import numpy as np
from env import get_db_url
import os






def new_log_data():
   
    conn = get_db_url('curriculum_logs')

    query = '''
            SELECT logs.*, cohorts.*
            FROM logs
            LEFT JOIN cohorts ON logs.cohort_id = cohorts.id;

            '''

    
    df = pd.read_sql(query, conn)
    return df
    """
    Retrieves curriculum log data either from a CSV file or by calling the new_log_data function.
    If the data exists in a CSV file, it is loaded from the file. Otherwise, it is retrieved
    from the database and saved to the CSV file for future use.
    
    Returns:
    - df: pandas DataFrame
        DataFrame containing the Telco data.
    """
def get_log_data():
    if os.path.isfile('log_df.csv'):
        df = pd.read_csv('log_df.csv', index_col = 0)
        
        return df

    else:

        df = new_log_data()

        df.to_csv('log_df.csv')
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


#-------------------------------------SPLIT---------------------------


def split_log_data(df, train_percentage=0.6, validation_percentage=0.15, random_seed=123):
    '''
    this function splits the data into train, validate and test data
    '''
    
    

    total_samples = len(df)
    train_size = int(total_samples * train_percentage)
    validation_size = int(total_samples * validation_percentage)

    train = df[:train_size]
    validation = df[train_size:train_size + validation_size]
    test = df[train_size + validation_size:]

    return train, validation, test


# -----------------------------wrangle-------------------------------- 

def wrangle_log():
    '''
    This function will do all encomposing function in one line to deliver a cleaned up train, validate and test data
    '''

    df = get_log_data()
    df = prep_log_data(df)
    train, validate, test = split_log_data(df, train_percentage=0.6, validation_percentage=0.15)
   
    return train, validate, test
