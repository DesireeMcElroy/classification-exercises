import pandas as pd
import numpy as np
import acquire
from sklearn.model_selection import train_test_split


def prep_iris(iris_df):
    iris_df = iris_df.drop(columns=['species_id', 'measurement_id'])
    iris_df = iris_df.rename(columns={'species_name': 'species'})
    dummy_df = pd.get_dummies(iris_df[['species']])
    iris_df = pd.concat([iris_df, dummy_df], axis=1)
    return iris_df



def train_validate_test_split(df, seed=123):
    train_and_validate, test = train_test_split(
        df, test_size=0.2, random_state=seed, stratify=df.survived
    )
    train, validate = train_test_split(
        train_and_validate,
        test_size=0.3,
        random_state=seed,
        stratify=train_and_validate.survived,
    )
    return train, validate, test