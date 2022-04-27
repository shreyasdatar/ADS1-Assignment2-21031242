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



df, dfT = read_data("Dataset.csv")
df_co2, df_co2T = read_data("CO2 emissions (metric tons per capita).csv")
df_popg, df_popgT = read_data("Population growth (annual %).csv")
df_tpop, df_tpopT = read_data("Population Total.csv")
df_urbpop, df_urbpopT = read_data("Urban Population.csv")


# Average CO2 emissions in last 10 years for 12 countries
mean_co2 = df_co2T.mean()
plt.figure(figsize=(10,10))
ax = plt.axes(facecolor='#E6E6E6')
ax.set_axisbelow(True)
plt.grid(color='w', linestyle='solid')
plt.bar(mean_co2.index, mean_co2.values, color='gray')
plt.xticks(np.arange(12), mean_co2.index, rotation=-90)
plt.title("Average CO2 emissions for past 10 years")
plt.xlabel("Countries")
plt.ylabel("metric tons per capita")
plt.savefig("CO2.png")
plt.show()



# colourbar for population growth in countries over 10 years
plt.figure(figsize=(10,10))
plt.subplot()
ax = plt.gca()
img = ax.imshow(df_popgT, cmap='seismic', vmin=-4, vmax=4)
plt.colorbar(img, label="%")
plt.colormaps()
ax.set_yticks(np.arange(0,10))
ax.set_yticklabels(df_popgT.index)
ax.set_xticks(np.arange(0,12))
ax.set_xticklabels(df_popgT.columns, rotation=-90)
plt.title("Population growth (annual %)")
plt.xlabel("Countries")
plt.ylabel("Years")
plt.savefig("Colourbar.png")
plt.show()



# line plot showing change in total population 
# of each country every year in billions
plt.figure(figsize=(10,10))
ax = plt.axes(facecolor='#E6E6E6')
ax.set_axisbelow(True)
plt.grid(color='w', linestyle='solid')
plt.plot(df_tpopT, marker="o")
plt.xticks(np.arange(10), df_tpopT.index, rotation=-90)
plt.legend(df_tpopT.columns)
plt.title("Total population Population")
plt.xlabel("Years")
plt.ylabel("Total Population in Billions")
plt.savefig("Totpop.png")
plt.show()



# Correlation between CO2 emissions and urban population
corr = df_urbpopT.corrwith(df_co2T)
plt.figure(figsize=(10,10))
ax = plt.axes(facecolor='#E6E6E6')
ax.set_axisbelow(True)
plt.grid(color='w', linestyle='solid')
plt.bar(corr.index, corr.values)
plt.xticks(np.arange(12), corr.index, rotation=-90)
plt.title("Correlation between CO2 emissions & Urban Population")
plt.xlabel("Countries")
plt.ylabel("Correlation")
plt.savefig("Corr.png")
plt.show()



