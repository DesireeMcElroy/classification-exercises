
import pandas as pd
import numpy as np
import os


# acquire
from env import host, user, password
from pydataset import data




# **************** TITANIC DATA *****************
def get_titanic_date():
    '''
    This function reads in the titanic data from the Codeup db
    and returns a pandas DataFrame with all columns.
    '''
    sql_query = 'SELECT * FROM passengers'
    return pd.read_sql(sql_query, get_connection('titanic_db'))



# ******************* IRIS DATA *********************
def get_iris_data():
    '''
    This function reads in the iris data from the Codeup db
    and returns a pandas DataFrame with all columns.
    '''
    sql_query = '''
    SELECT *
    FROM measurements
    JOIN species USING (species_id)
    '''
    return pd.read_sql(sql_query, get_connection('iris_db'))




def get_titanic_data(cached=False):
    '''
    This function reads in titanic data from Codeup database and writes data to
    a csv file if cached == False or if cached == True reads in titanic df from
    a csv file, returns df.
    '''
   #If the cached parameter is false, or the csv file is not on disk, read from the database into a dataframe
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



def get_iris_data(cached=False):
    '''
    This function reads in titanic data from Codeup database and writes data to
    a csv file if cached == False or if cached == True reads in titanic df from
    a csv file, returns df.
    '''
    # read the db from codeup db into a df if the cached parameter is false or the file is not on disk
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
