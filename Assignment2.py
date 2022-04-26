# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 20:51:22 2022

@author: dshre
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from IPython.display import display
import warnings
warnings.filterwarnings('ignore')

def read_data(fname):
    """
    The function reads data from a csv file
    and returns a Pandas Dataframe.

    Parameters
    ----------
    fname : string
        Name of file containing data of a World Bank indicator.

    Returns
    -------
    df : Pandas Dataframe
        A Pandas Dataframe containing relevent data
        from the World Bank indicator file i.e. Countries X Years data.
    df.T : Pandas Dataframe
        Transpose of the df Dataframe where the Years are the Index.

    """
    df = pd.read_csv(fname)
    df = df.drop(["Series Name", "Series Code", "Country Code",
           "1990 [YR1990]", "2000 [YR2000]"], axis=1)
    df = df.set_index('Country Name')
    df = df.rename(columns={"2011 [YR2011]":"2011", "2012 [YR2012]":"2012",
                            "2013 [YR2013]":"2013", "2014 [YR2014]":"2014",
                            "2015 [YR2015]":"2015", "2016 [YR2016]":"2016",
                            "2017 [YR2017]":"2017", "2018 [YR2018]":"2018",
                            "2019 [YR2019]":"2019", "2020 [YR2020]":"2020"})
    cols = list(df.columns)
    for col in cols:
        df[col] = df[col].astype(float)
    
    return df, df.T


def avg_var(df):
    '''
    The function returns mean and variance of each column of a Dataframe

    Parameters
    ----------
    df : Pandas Dataframe
        A Pandas Dataframe containing data.

    Returns
    -------
    mean : Pandas Series
        A Pandas Series containing mean for each column of the Dataframe.
    var : Pandas Series
        A Pandas Series containing variance for each column of the Dataframe.

    '''
    mean = df.mean()
    var = df.var()
    return mean, var
    




