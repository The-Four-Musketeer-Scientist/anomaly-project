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

def prep_log_data():
    '''
    This function acquires and preps the log data.
    '''

    if os.path.isfile('log_df.csv'):
        df = pd.read_csv('log_df.csv', index_col=0)
    else:
        df = new_log_data()
        df.to_csv('log_df.csv')

    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
    

    return df


