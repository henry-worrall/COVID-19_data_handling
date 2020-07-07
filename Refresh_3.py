# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 10:21:41 2020

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

df4 = pd.read_csv('Regional Data.csv')

df6 = pd.read_excel('Population Data Use 2.xlsx')

df7 = pd.read_excel('GDP Data Use.xlsx')

"""
************STEP 2: MANIPULATE THE DATAFRAMES USING PANDAS************
"""

df4 = df4.drop('Global North/South', axis=1) #We  don't need the 'Global North/South' column for data analysis either.

Renames = [('Russia', 'Russian Federation'),
          ('Syria', 'Syrian Arab Republic'),
          ('US', 'United States'),
          ('Korea, South', 'Korea, Republic of'),
          ('Taiwan*', 'Taiwan'),
          ('Brunei', 'Brunei Darussalam'),
          ('Laos', "Lao People's Democratic Republic"),
          ('Burma', 'Myanmar'),
          ('Czechia', 'Czech Republic'),
          ('Tanzania', 'Tanzania, United Republic of'),
          ('Congo (Kinshasa)', 'Congo, The Democratic Republic of the'),
          ('Congo (Brazzaville)', 'Congo'),
          ("Cote d'Ivoire", "Côte D'Ivoire"),
          ('Eswatini','Swaziland'),
          ('Iran', 'Iran, Islamic Republic of'),
          ('Moldova', 'Moldova, Republic of'),
          ('North Macedonia', 'Macedonia'),
          ('Cabo Verde', 'Cape Verde'),
          ('Holy See', 'Holy See (Vatican City State)')]

# Iterate through renames setting the countries of the European Data (Renames[rename][1]) to the covid data (Renames[rename][0])
for rename in range(len(Renames)):
    df4.loc[(df4['Country']==Renames[rename][1]),'Country'] = Renames[rename][0]

df5 = pd.DataFrame([['West Bank and Gaza', 'Middle East'], ['Kosovo', 'Europe']], columns=['Country', 'Region'])
df4 = df4.append(df5, ignore_index=True)
#now the european data should be in the correct format for the tableau covid data.




#pivot data frames so that columns of individual dates are arranged into a single column titled 'date' and with the number of cases/deaths/recovered placed as the pivot value
df_cases = pd.melt(df1, id_vars = ["Province/State", "Country/Region", "Lat", "Long"], var_name="date", value_name="number of cases")

df_deaths = pd.melt(df2, id_vars = ["Province/State", "Country/Region", "Lat", "Long"], var_name="date", value_name="number of deaths")

df_recovered = pd.melt(df3, id_vars = ["Province/State", "Country/Region", "Lat", "Long"], var_name="date", value_name="number of recovered")


#merge all of the data frames into one table
df_all_data = pd.merge(df_cases, pd.merge(df_deaths, df_recovered, how='outer', on=None), how='outer', on=None)

#N.b. the covid data has the Country column saved as "Country/Region" whereas the regional data has it as "Country"
df4 = df4.rename(columns={"Country": "Country/Region"})

#merge the combined cases, deaths and recoveries DataFrame with the Regional Data. 
df_total = pd.merge(df_all_data, df4, how='left', on=None)

#Now add the Population data to the DataFrame
df_total_1 = pd.merge(df_total, df6, how='left', on='Country/Region')

#Now add the GDP data to the DataFrame
df_total_2 = pd.merge(df_total_1, df7, how='left', on='Country/Region')

#Calculate GDP per Capita and add it to DataFrame as new column
df_total_2['GDP per Capita ($)'] = df_total_2['GDP ($)'] / df_total_2['Population']


"""
************STEP 3: LINK AND SEND DATA TO GOOGLE SHEETS************
"""

# Link to the google spreadsheet using the Spread function, set as variable spread
spread = Spread('COVID data new_2')
# This will ask to authenticate if you haven't done so before

# Save 'all' DataFrame to google worksheets in the google spreadsheet titled all
spread.df_to_sheet(df_total_2, index=True, sheet='all', start='A1', replace=True)

