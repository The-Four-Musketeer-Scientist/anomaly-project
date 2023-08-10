import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime
import seaborn as sns
import os


def one_user_df_prep(df, user):
    '''
    This function returns a dataframe consisting of data for one user
    '''
    df = df[df.user_id == user]
    pages_one_user = df['path'].resample('d').count()
    return pages_one_user

def compute_pct_b(pages_one_user, span, weight, user):
    '''
    This function adds the %b of a bollinger band range for the page views of a single user's log activity
    '''
    # Calculate upper and lower bollinger band
    midband = pages_one_user.ewm(span=span).mean()
    stdev = pages_one_user.ewm(span=span).std()
    ub = midband + stdev*weight
    lb = midband - stdev*weight
    
    # Add upper and lower band values to dataframe
    bb = pd.concat([ub, lb], axis=1)
    
    # Combine all data into a single dataframe
    my_df = pd.concat([pages_one_user, midband, bb], axis=1)
    my_df.columns = ['pages_one_user', 'midband', 'ub', 'lb']
    
    # Calculate percent b and relevant user id to dataframe
    my_df['pct_b'] = (my_df['pages_one_user'] - my_df['lb'])/(my_df['ub'] - my_df['lb'])
    my_df['user_id'] = user
    return my_df

def plot_bands(my_df, user):
    '''
    Plots Bollinger Bands of Single User
    '''
    fig, ax = plt.subplots(figsize=(12,8))
    ax.plot(my_df.index, my_df.pages_one_user, label='Number of Pages, User: '+str(user))
    ax.plot(my_df.index, my_df.midband, label = 'EMA/midband')
    ax.plot(my_df.index, my_df.ub, label = 'Upper Band')
    ax.plot(my_df.index, my_df.lb, label = 'Lower Band')
    ax.legend(loc='best')
    ax.set_ylabel('Number of Pages')
    plt.show()

def find_anomalies(df, user, span, weight, plot=False):
    '''
    This function returns the records where a user's daily activity exceeded the lower limit of a bollinger band range
    '''
    
    # Single user dataframe
    pages_one_user = one_user_df_prep(df, user)
    
    # Adds Bollinger Bands to DF
    my_df = compute_pct_b(pages_one_user, span, weight, user)
    
    # Plots data if Plot=True
    if plot:
        plot_bands(my_df, user)
    
    # Return only records that sit outside of bollinger band lower limit
    return my_df[my_df.pct_b<1]



def save_visuals(fig: plt.figure ,viz_name:str= "unamed_viz", folder_name:int= 0, ) -> str:
    """
    Goal: Save a single visual into the project visual folder
    parameters:
        fig: seaborn visual figure to be saved
        viz_name: name of the visual to save
        folder_name: interger (0-7)represanting the section you are on in the pipeline
            0: all other (defealt)
            1: univariate stats
            2: bivariate stats
            3: multivariate stats
            4: stats test
            5: modeling
            6: final report
            7: presantation
    return:
        message to user on save status
    """
    project_visuals = "./00_project_visuals"
    folder_selection = {
        0: "00_non_specific_viz",
        1: "01_univariate_stats_viz",
        2: "02_bivariate_stats_viz",
        3: "03_multivariate_stats_viz",
        4: "04_stats_test_viz",
        5: "05_modeling_viz",
        6: "06_final_report_viz",
        7: "07_presantation"
    }
    # return error if user input for folder selection is not found
    if folder_name not in list(folder_selection.keys()):
        return f"{folder_name} is not a valid option for a folder name."
    # when folder location is found in selections
    else:
        # Specify the path to the directory where you want to save the figure
        folder_name = folder_selection[folder_name]
        directory_path = f'{project_visuals}/{folder_name}/'
        # Create the full file path by combining the directory path and the desired file name
        file_path = os.path.join(directory_path, f'{viz_name}.png')
        if os.path.exists(project_visuals): # check if the main viz folder exists
            if not os.path.exists(directory_path): # check if the folder name already exists
                os.makedirs(directory_path)
                # Save the figure to the specified file path
                fig.canvas.print_figure(file_path)
            else:
                # Save the figure to the specified file path
                fig.canvas.print_figure(file_path)
        else:
            # create both the project vis folder and the specific section folder
            os.makedirs(project_visuals)
            os.makedirs(directory_path)
            # Save the figure to the specified file path
            fig.canvas.print_figure(file_path)
    return f"Visual successfully saved in folder: {folder_name}"