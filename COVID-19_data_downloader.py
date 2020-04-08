# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 15:55:08 2020

@author: Henry
"""

"""
New script to automatically download a new version of the JHU Covid-19 data and save the confirmed cases, confirmed deaths, and confirmed recoveries as separate sheets in one workbook.
The script will then pivot the data in the table, from the starting date column to the final column.
The script will then created a new worksheet (at the beginning of the sheets) with the pivoted confirmed cases sheet, and append the columns giving the number of incidents of each (death/recovery) from the pivoted confirmed deaths/recoveries sheet.
"""


#import pandas as pd
#import numpy as np
#from datetime import datetime, timedelta
#import math
#import os
#import base64
#import datetime
#
#def load_data(file_name, column_name):
#    data = (
#        pd.read_csv(base_URL + file_name)
#        .melt(
#            id_vars=["Province/State", "Country/Region", "Lat", "Long"],
#            var_name="date",
#            value_name=column_name,
#        )
#        .astype({"date": "datetime64[ns]", column_name: int}, errors="ignore")
#    )
#    data["Province/State"].fillna("<all>", inplace=True)
#    data[column_name].fillna(0, inplace=True)
#    return data
#
#base_URL = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/"
#confirmed_cases = "time_series_covid19_confirmed_global.csv"
#confirmed_deaths = "time_series_covid19_deaths_global.csv"
#confirmed_recovered = "time_series_covid19_recovered_global.csv"
#
#all_data = (
#    load_data(confirmed_cases, "confirmed")
#    .merge(load_data(confirmed_deaths, "deaths"))
#    .merge(load_data(confirmed_recovered, "recovered"))
#)


import requests as rq

def download_file(file_name, download_name):
    data = rq.get(base_URL + file_name)
    data.raise_for_status()
    downloadFile = open(download_name, 'wb')
    for chunk in data.iter_content(100000):
        downloadFile.write(chunk)
    downloadFile.close()
    
base_URL = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/"
confirmed_cases = "time_series_covid19_confirmed_global.csv"
confirmed_deaths = "time_series_covid19_deaths_global.csv"
confirmed_recovered = "time_series_covid19_recovered_global.csv"

download_file(confirmed_cases, 'covid-19cases.csv')
download_file(confirmed_deaths, 'covid-19deaths.csv')
download_file(confirmed_recovered, 'covid-19recovered.csv')
