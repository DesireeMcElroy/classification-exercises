
import pandas as pd
import numpy as np
import os


# acquire
from env import host, user, password
from pydataset import data




# **************** TITANIC DATA *****************
def get_titanic_data(cached = False):
    '''
    This function reads in the titanic data from the Codeup db
    and returns a pandas DataFrame with all columns.
    '''
    if cached == False or os.path.isfile('titanic_df.csv') == False:
        query = '''
        SELECT * 
        FROM passengers;
        '''
        titanic_df = pd.read_sql(query, get_db_url('titanic_db'))
        #also cache the data we read from the db, to a file on disk
        titanic_df.to_csv('titanic_df.csv')
    else:
        #either the cached parameter was true, or a file exists on disk. Read that into a df instead of going to the database
        titanic_df = pd.read_csv('titanic_df.csv', index_col=0)

    #return our dataframe regardless of its origin
    return titanic_df

# ******************* IRIS DATA *********************
def get_iris_data(cached = False):
    '''
    This function reads in the iris data from the Codeup db
    and returns a pandas DataFrame with all columns.
    '''
    if cached == False or os.path.isfile('iris_df.csv') == False:
        query = '''
        SELECT * 
        FROM measurements
        JOIN species USING (species_id);;
        '''
        iris_df = pd.read_sql(query, get_db_url('iris_db'))
        # cache it as a csv file
        iris_df.to_csv('iris_df.csv')

    else: # if cached parameter is True or file exists on disk, read the file into a pandas df
        iris_df = pd.read_csv('iris_df', index_col=0)
     # return the iris df regardless of origin
    return iris_df




