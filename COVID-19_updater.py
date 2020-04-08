# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 17:35:51 2020

@author: Henry
"""

from __future__ import print_function
import pandas as pd
from gspread_pandas import Spread

"""
************STEP 1: Load raw data into Pandas Dataframe************
"""

# raw data location
base_URL = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/"
confirmed_cases = "time_series_covid19_confirmed_global.csv"
confirmed_deaths = "time_series_covid19_deaths_global.csv"
confirmed_recovered = "time_series_covid19_recovered_global.csv"


#read data into script
df1 = pd.read_csv(base_URL + confirmed_cases)
df2 = pd.read_csv(base_URL + confirmed_deaths)
df3 = pd.read_csv(base_URL + confirmed_recovered)


"""
************STEP 2: MANIPULATE THE DATAFRAMES USING PANDAS************
"""

#pivot data frames so that columns of individual dates are arranged into a single column titled 'date' and with the number of cases/deaths/recovered placed as the pivot value
df_cases = pd.melt(df1, id_vars = ["Province/State", "Country/Region", "Lat", "Long"], var_name="date", value_name="number of cases")

df_deaths = pd.melt(df2, id_vars = ["Province/State", "Country/Region", "Lat", "Long"], var_name="date", value_name="number of deaths")

df_recovered = pd.melt(df3, id_vars = ["Province/State", "Country/Region", "Lat", "Long"], var_name="date", value_name="number of recovered")


#merge all of the data frames into one table
df_all_data = pd.merge(df_cases, pd.merge(df_deaths, df_recovered, how='outer', on=None), how='outer', on=None)


"""
************STEP 3: LINK AND SEND DATA TO GOOGLE SHEETS************
"""

# Link to the google spreadsheet using the Spread function, set as variable spread
spread = Spread('COVID-19 Data')
# This will ask to authenticate if you haven't done so before

# Save 'all' DataFrame to google worksheets in the google spreadsheet titled all
spread.df_to_sheet(df_all_data, index=True, sheet='all', start='A1', replace=True)
