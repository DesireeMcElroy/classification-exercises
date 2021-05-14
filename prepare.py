import pandas as pd
import numpy as np
import acquire


def prep_iris(iris_df):
    iris_df = iris_df.drop(columns=['species_id', 'measurement_id'])
    iris_df = iris_df.rename(columns={'species_name': 'species'})
    dummy_df = pd.get_dummies(iris_df[['species']])
    iris_df = pd.concat([df, dummy_df], axis=1)
    return iris_df