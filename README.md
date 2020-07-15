# COVID-19 Data Handling
The aim of this project is to automatically download data from Johns Hopkins University CSSE and update my COVID dashboard. The dashboard is built using Tableau to visualise and analyse coronavirus data. The final dashboard can be found <a href="https://public.tableau.com/profile/henry.worrall#!/vizhome/COVID-19DashboardAnalysis/COVID-19Dashboard" target="_blank">here</a>. 

### Data Sources

Coronvirus Data - <a href='https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/' target="blank">Johns Hopkins University (JHU) Github Repository</a>

GDP & Population Data - <a href="https://www.worldometers.info/gdp/gdp-by-country/" target="_blank">worldometer.info</a>

Note that for stability and data cleaning purposes, the data collected from worldometers.info is not updated. The data is accurate as of 10 June 2020.

#### Potential Errors in the Data Sources

The data collected from JHU only takes into account the "confirmed" or "official" reported figures for each country. The real number of COVID-19 cases, deaths and recoveries are likely to be greater than the numbers given in this data source.

### How the code works:

In summary, the main script associated in this project - Refresh_3.py - works as follows:
	
1. Pulls the data from the various sources (JHU and saved files)
2. Manipulates the JHU data into long vertical (rather than long horizontal) table
3. Merges GDP and Population data with the corresponding countries in the JHU COVID-19 data.
4. Saves the combined table as a google spreadsheet

In this way, the Refresh_3.py script can be scheduled to run every day to update the google spreadsheet. Tableau can then access the data in the google spreadsheet, and update the data displayed on the dashboard without any manual input.
