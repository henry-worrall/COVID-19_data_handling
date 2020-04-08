# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 17:27:01 2020

@author: Henry
"""

"""
Manipulate the data downloaded from JHU Github to pivot the individual date columns into one column titled dates and another column containing the values (#cases, #deaths, #recovered)
"""

import pandas as pd

folder_location = 'C:/Users/Henry/Documents/Programming Stuff/downloading_online_files/'

cases = 'covid-19cases.csv'
deaths = 'covid-19deaths.csv'
recovered = 'covid-19recovered.csv'

#read data into script
df1 = pd.read_csv(folder_location + cases)
df2 = pd.read_csv(folder_location + deaths)
df3 = pd.read_csv(folder_location + recovered)

#pivot data frames so that columns of individual dates are arranged into a single column titled 'date' and with the number of cases/deaths/recovered placed as the pivot value
df_cases = pd.melt(df1, id_vars = ["Province/State", "Country/Region", "Lat", "Long"], var_name="date", value_name="number of cases")

df_deaths = pd.melt(df2, id_vars = ["Province/State", "Country/Region", "Lat", "Long"], var_name="date", value_name="number of deaths")

df_recovered = pd.melt(df3, id_vars = ["Province/State", "Country/Region", "Lat", "Long"], var_name="date", value_name="number of recovered")


#merge all of the data frames into one table
df_all_data = pd.merge(df_cases, pd.merge(df_deaths, df_recovered, how='outer', on=None), how='outer', on=None)


with pd.ExcelWriter('covid-19_manipulated.xlsx') as writer:
    df_all_data.to_excel(writer, sheet_name="all")
    df_cases.to_excel(writer, sheet_name="cases")
    df_deaths.to_excel(writer, sheet_name="deaths")
    df_recovered.to_excel(writer, sheet_name="recovered")