import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import json
import folium
import os

##CLEANING DATA AND SEPERATING INTO DATAFRAMES.##
hist = pd.read_csv('/home/andrewa/Desktop/Fall 2021/Intro to data science/project/NYPD_Arrests_Data__Historic_.csv')
recent = pd.read_csv('/home/andrewa/Desktop/Fall 2021/Intro to data science/project/NYPD_Arrest_Data__Year_to_Date_.csv')
# # Get stratified sampling of my data by proportion.
# stratSampHis = hist.groupby('ARREST_BORO', group_keys=False).apply(
#     lambda x: x.sample(int(np.rint(100000 * len(x) / len(hist))))).reset_index(drop=True)

# Change arrest date to datetime
hist['ARREST_DATE'] = pd.to_datetime(hist['ARREST_DATE'])

# Make arrest date only have the year to filter by year
hist['ARREST_DATE'] = hist.ARREST_DATE.dt.year

# Clean crimes to combine similar types of crime as one to count.
recent.OFNS_DESC = recent['OFNS_DESC'].apply(lambda x: 'FRAUD' if 'FRAUD' in x else x)
recent.OFNS_DESC = recent['OFNS_DESC'].apply(lambda x: 'STOLEN PROPERTY' if 'STOLEN PROPERTY' in x else x)
recent.OFNS_DESC = recent['OFNS_DESC'].apply(lambda x: 'ASSAULT' if 'ASSAULT 3' in x else x)
recent.OFNS_DESC = recent['OFNS_DESC'].apply(lambda x: 'CAR THEFT' if 'GRAND LARCENY OF MOTOR VEHICLE' in x else x)
hist.OFNS_DESC = hist['OFNS_DESC'].apply(lambda x: 'FRAUD' if 'FRAUD' in x else x)
hist.OFNS_DESC = hist['OFNS_DESC'].apply(lambda x: 'FRAUD' if 'FRAUD' in x else x)
hist.OFNS_DESC = hist['OFNS_DESC'].apply(lambda x: 'CAR THEFT' if 'GRAND LARCENY OF MOTOR VEHICLE' in x else x)
hist.OFNS_DESC = hist['OFNS_DESC'].apply(lambda x: 'ASSAULT ' if 'ASSAULT 3' in x else x)
hist.OFNS_DESC = hist['OFNS_DESC'].apply(lambda x: 'THEFT RELATED' if 'OTHER OFFENSES RELATED TO THEFT' in  x else x)
hist.OFNS_DESC = hist['OFNS_DESC'].apply(lambda x: 'THEFT RELATED' if 'THEFT OF SERVICES' in  x else x)
hist.OFNS_DESC = hist['OFNS_DESC'].apply(lambda x: 'THEFT RELATED' if 'BURGLAR' in x else x)

# Group crime data by the boro and date, and count the number of crimes for each.
crimeCountHis = hist.groupby(['ARREST_DATE'])['OFNS_DESC'].value_counts().reset_index(name='Crime Count')
crimeCountHisPre = hist.groupby(['ARREST_DATE', 'ARREST_PRECINCT'])['OFNS_DESC'].value_counts().reset_index(name='Crime Count')
crimeCountrec = recent.groupby(['ARREST_PRECINCT'])['OFNS_DESC'].value_counts().reset_index(name='Crime Count')

# print(crimeCountrec)
#Folium Map
m = folium.Map(location = [40, -73], zoom_start = 7)
with open('/home/andrewa/Desktop/Fall 2021/Intro to data science/project/PolicePrecincts.geojson') as access_json:
            read_content = json.load(access_json)
features = read_content['features']
nodeData = os.path.join('/home/andrewa/Desktop/Fall 2021/Intro to data science/project/PolicePrecincts.geojson')
geo_json = folium.GeoJson(nodeData, popup=folium.GeoJsonPopup(fields=['precinct']))
geo_json.add_to(m)
m.save(outfile="m.html")

# Sex crimes include
assCnt = len(crimeCountHis[crimeCountHis['OFNS_DESC'].str.contains('THEFT OF SERVICES')])
print(assCnt)

# VISUALIZATION ##
sns.lineplot(data=crimeCountHis, x='ARREST_DATE', y='Crime Count', hue='OFNS_DESC', style = 'OFNS_DESC', ci=25, markers = True, dashes = False).set_title("Crime in Queens (2015-2020)", fontdict={'fontsize': 20})
plt.legend(bbox_to_anchor=(1, 1), loc="best", borderaxespad=-2)
plt.get_current_fig_manager().full_screen_toggle()
plt.savefig('LineHis')
plt.show()

# Count by precinct 
recent = recent[recent['ARREST_PRECINCT'] >= 100]
sns.countplot(data=recent, y='OFNS_DESC', hue = 'ARREST_PRECINCT', palette = 'deep', order = recent['OFNS_DESC'].value_counts().index)
sns.set_style('ticks')
plt.show()

# # Make chart to count number of crimes in the last year in queens
sns.countplot(data=recent, y='OFNS_DESC').set_title("Queens Year-to-date", fontdict={'fontsize': 20})
#Change y label sizes
plt.show()

# crimeCountHis.to_csv('queensCH.csv')
