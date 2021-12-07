'''
Name: Andrew Alagna
Email: andrew.alagna98@myhunter.cuny.edu
Resources: I spoke with St. John during the planning phase to help decide how to cut down my data to a more reasonable size. I used data from - https://data.cityofnewyork.us/Public-Safety/NYPD-Arrests-Data-Historic-/8h9b-rp9u/data, https://data.cityofnewyork.us/Public-Safety/Police-Precincts/78dh-3ptz, https://data.cityofnewyork.us/Public-Safety/Police-Precincts/78dh-3ptz 
Title: Crime in Queens: The Trend of Crime Historically and After the Covid-19 Outbreak
Theme: Social-justice
Abstract:Your sense of safety largely depends on the crime rate of where you live. Some areas of the city have suffered an increase in crime since the COVID-19 outbreak , while some areas of the city have suffered a high crime rate historically. I use python Pandas and dataframes to clean the data, seaborn line-plots, count-plots and matplotlib.pyplot to display the data and visualize trends, and folium to display the area of each precinct. I then categorized which neighborhoods have had an increase in crime since covid. I am trying to visualize and identify the trend of crime in Queens.
Relevance to NYC: The trend in crime in NYC affects everyone, because we all want to see that crime is decreasing in order to feel safe where we live.
URL: https://elchic00.github.io/CrimeInQueens/.
GitHub: https://github.com/elchic00 
LinkedIn: https://www.linkedin.com/in/andrew-a-10b88215b/ 
'''
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import json
import folium
import os
import webbrowser

##CLEANING DATA AND SEPERATING INTO DATAFRAMES.##
hist = pd.read_csv('NYPD_Arrests_Data__Historic_.csv')
recent = pd.read_csv('NYPD_Arrest_Data__Year_to_Date_.csv')
# Filter DF to only include precincts in queens (100-115)
hist = hist[hist['ARREST_PRECINCT'] >= 100]
recent = recent[recent['ARREST_PRECINCT'] >= 100]

# # Get stratified sampling of my data by proportion.
# stratSampHis = hist.groupby('ARREST_BORO', group_keys=False).apply(
#     lambda x: x.sample(int(np.rint(100000 * len(x) / len(hist))))).reset_index(drop=True)

# Change arrest date to datetime
hist['ARREST_DATE'] = pd.to_datetime(hist['ARREST_DATE'])
recent['ARREST_DATE'] = pd.to_datetime(recent['ARREST_DATE'])

# Find the average crime count after the shutdown in march.
crimeCountrec = recent.groupby(['ARREST_PRECINCT'])['OFNS_DESC'].value_counts().reset_index(name='Crime Count')
# Get all dates after the shutdown in march of 2020.
hisAfPand = hist[hist.ARREST_DATE > '2020-03-11']
#Count the average crime by offense type and find the average per year after march 2020.
hisAfPand = hisAfPand.groupby(['ARREST_PRECINCT'])['OFNS_DESC'].value_counts().reset_index(name='Crime Count')
hisAfPand['Crime Count'] = round((hisAfPand['Crime Count'] + crimeCountrec['Crime Count'])/1.67)

# Average crime rate over the last 5 years
hisToPand = hist[hist.ARREST_DATE <= '2020-03-11']
histAvg = hisToPand.groupby(['ARREST_PRECINCT'])['OFNS_DESC'].value_counts().reset_index(name='Crime Count')
histAvg['Crime Count'] = round(histAvg['Crime Count']/5.225)
histAvg.rename(columns = {'Crime Count':'Crime Count Historic Avg'},inplace = True)

# Merge histAvg and recentAvg and add new column to df to check if there was an increase in crime since covid.
merged = pd.merge(histAvg, hisAfPand)
# Make a new column to say if average crime rate of the last five years has increased since the shutdown.
merged['Increase in Crime'] = merged['Crime Count Historic Avg'] < merged['Crime Count']
print(merged)
# print(merged[['ARREST_PRECINCT','OFNS_DESC','Increase in Crime']])
merged.to_csv('merged.csv')




# Find the average crime count after the shutdown in march.
crimeCountrec = recent.groupby(['ARREST_DATE'])['OFNS_DESC'].value_counts().reset_index(name='Crime Count')
# Get all dates after the shutdown in march of 2020 and the prior 5 years.
hisAfPand = hist[hist.ARREST_DATE > '2020-03-11']
hisToPand = hist[hist.ARREST_DATE <= '2020-03-11']
#Count the average crime by offense type and find the average per year after march 2020.
hisAfPand = hisAfPand.groupby(['ARREST_PRECINCT'])['OFNS_DESC'].value_counts().reset_index(name='Crime Count')
hisAfPand['Crime Count'] = round((hisAfPand['Crime Count'] + crimeCountrec['Crime Count'])/1.67)

# Make arrest date only have the year to filter by year
hist['ARREST_DATE'] = hist.ARREST_DATE.dt.year

# Average crime rate over the last 5 years
histAvg = hisToPand.groupby(['ARREST_PRECINCT'])['OFNS_DESC'].value_counts().reset_index(name='Crime Count')
histAvg['Crime Count'] = round(histAvg['Crime Count']/5.225)
histAvg.rename(columns = {'Crime Count':'Crime Count Historic Avg'},inplace = True)


# Clean crimes to combine similar types of crime as one to count.
recent.OFNS_DESC = recent['OFNS_DESC'].apply(lambda x: 'FRAUD' if 'FRAUD' in x else x)
recent.OFNS_DESC = recent['OFNS_DESC'].apply(lambda x: 'STOLEN PROPERTY' if 'STOLEN PROPERTY' in x else x)
recent.OFNS_DESC = recent['OFNS_DESC'].apply(lambda x: 'ASSAULT' if 'ASSAULT 3' in x else x)
recent.OFNS_DESC = recent['OFNS_DESC'].apply(lambda x: 'CAR THEFT' if 'GRAND LARCENY OF MOTOR VEHICLE' in x else x)
hist.OFNS_DESC = hist['OFNS_DESC'].apply(lambda x: 'FRAUD' if 'FRAUD' in x else x)
hist.OFNS_DESC = hist['OFNS_DESC'].apply(lambda x: 'CAR THEFT' if 'GRAND LARCENY OF MOTOR VEHICLE' in x else x)
hist.OFNS_DESC = hist['OFNS_DESC'].apply(lambda x: 'ASSAULT ' if 'ASSAULT 3' in x else x)
recent.OFNS_DESC = recent['OFNS_DESC'].apply(lambda x: 'STOLEN PROPERTY' if 'STOLEN PROPERTY' in x else x)
hist.OFNS_DESC = hist['OFNS_DESC'].apply(lambda x: 'THEFT RELATED' if 'OTHER OFFENSES RELATED TO THEFT' in  x else x)
hist.OFNS_DESC = hist['OFNS_DESC'].apply(lambda x: 'THEFT RELATED' if 'THEFT OF SERVICES' in  x else x)
hist.OFNS_DESC = hist['OFNS_DESC'].apply(lambda x: 'THEFT RELATED' if "BURGLAR’S TOOLS" in x else x)

# Group crime data by the date, and count the number of crimes for each crime type.
crimeCountHis = hist.groupby(['ARREST_DATE'])['OFNS_DESC'].value_counts().reset_index(name='Crime Count')
# Group crime data by the date and precinct, then count the number of crimes for each crime type.
crimeCountHisPre = hist.groupby(['ARREST_DATE', 'ARREST_PRECINCT'])['OFNS_DESC'].value_counts().reset_index(name='Crime Count')


# Folium Map configuration
m = folium.Map(location = [40.742054, -73.769417], zoom_start = 11)
with open('PolicePrecincts.geojson') as access_json:
            read_content = json.load(access_json)
features = read_content['features']
nodeData = os.path.join('PolicePrecincts.geojson')
# Add precinct popup to map
geo_json = folium.GeoJson(nodeData, popup=folium.GeoJsonPopup(fields=['precinct']))
geo_json.add_to(m)
m.save(outfile="map.html")
webbrowser.open('map.html', new=2)


# # VISUALIZATION # #
# Make a lineplot to show the trend of crime over the last 5 years.
sns.lineplot(data=crimeCountHis, x='ARREST_DATE', y='Crime Count', hue='OFNS_DESC', style = 'OFNS_DESC', ci=25, markers = True, dashes = False).set_title("Crime in Queens (2015-2020)", fontdict={'fontsize': 20})
plt.legend(bbox_to_anchor=(1, 1), loc="best", borderaxespad=-2.4)
plt.get_current_fig_manager().full_screen_toggle()
plt.savefig('LineHis')
plt.xlabel('Arrest Year')
plt.show()

# Count by crime type for each precinct 
sns.countplot(data=recent, y='OFNS_DESC', hue = 'ARREST_PRECINCT', palette = 'bright', order = recent['OFNS_DESC'].value_counts().index).set_title("Crime in Queens by Preinct (YTD)", fontdict={'fontsize': 20})
sns.set_style('ticks')
plt.get_current_fig_manager().full_screen_toggle()
plt.xlabel('Crime Count')
plt.ylabel('Type of Crime')
plt.show()

# Make chart to count number of crimes over the last year in queens
c = sns.countplot(data=recent, y='OFNS_DESC', order =recent['OFNS_DESC'].value_counts().index ).set_title("Crime in Queens Year-to-date", fontdict={'fontsize': 20})
plt.xlabel('Crime Count')
plt.ylabel('Type of Crime')
plt.show()