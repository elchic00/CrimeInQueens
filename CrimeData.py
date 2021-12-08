'''
Name: Andrew Alagna
Email: andrew.alagna98@myhunter.cuny.edu
Resources: I spoke with St. John during the planning phase to help decide how to cut down my data to a more reasonable size. I used data from - https://data.cityofnewyork.us/Public-Safety/NYPD-Arrests-Data-Historic-/8h9b-rp9u/data, https://data.cityofnewyork.us/Public-Safety/Police-Precincts/78dh-3ptz, https://data.cityofnewyork.us/Public-Safety/Police-Precincts/78dh-3ptz 
Title: Crime in Queens: The Trend of Crime Historically and After the Covid-19 Outbreak
Theme: Social-justice
Abstract: Your sense of safety largely depends on the crime rate of where you live. Since the shutdown in March of 2020, it feels as if there has been an uptick in theft related crimes. 
I'm also thinking that certain areas of the city have suffered an increase in crime since the COVID-19 outbreak , while some areas of the city have suffered a high crime rate historically. 
I use python dataframes from Pandas to clean the data, seaborn line-plots, count-plots and matplotlib.pyplot to display the data and visualize trends, and folium to display the area of each precinct. 
I then categorized which neighborhoods and types of crime have increased since the shutdown in March of 2020. I am trying to visualize and identify the trend of crime in Queens.
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

# Clean crimes to combine similar types of crime as one to count.
recent.OFNS_DESC = recent['OFNS_DESC'].apply(lambda x: 'FRAUD' if 'FRAUD' in x else x)
recent.OFNS_DESC = recent['OFNS_DESC'].apply(lambda x: 'STOLEN PROPERTY' if 'STOLEN PROPERTY' in x else x)
recent.OFNS_DESC = recent['OFNS_DESC'].apply(lambda x: 'ASSAULT' if 'ASSAULT 3' in x else x)
recent.OFNS_DESC = recent['OFNS_DESC'].apply(lambda x: 'CAR THEFT' if 'GRAND LARCENY OF MOTOR VEHICLE' in x else x)
recent.OFNS_DESC = recent['OFNS_DESC'].apply(lambda x: 'THEFT RELATED' if 'OTHER OFFENSES RELATED TO THEFT' in  x else x)
recent.OFNS_DESC = recent['OFNS_DESC'].apply(lambda x: 'THEFT RELATED' if 'THEFT OF SERVICES' in  x else x)
recent.OFNS_DESC = recent['OFNS_DESC'].apply(lambda x: 'THEFT RELATED' if "BURGLAR’S TOOLS" in x else x)
hist.OFNS_DESC = hist['OFNS_DESC'].apply(lambda x: 'STOLEN PROPERTY' if 'STOLEN PROPERTY' in x else x)
hist.OFNS_DESC = hist['OFNS_DESC'].apply(lambda x: 'FRAUD' if 'FRAUD' in x else x)
hist.OFNS_DESC = hist['OFNS_DESC'].apply(lambda x: 'CAR THEFT' if 'GRAND LARCENY OF MOTOR VEHICLE' in x else x)
hist.OFNS_DESC = hist['OFNS_DESC'].apply(lambda x: 'ASSAULT ' if 'ASSAULT 3' in x else x)
hist.OFNS_DESC = hist['OFNS_DESC'].apply(lambda x: 'THEFT RELATED' if 'OTHER OFFENSES RELATED TO THEFT' in  x else x)
hist.OFNS_DESC = hist['OFNS_DESC'].apply(lambda x: 'THEFT RELATED' if 'THEFT OF SERVICES' in  x else x)
hist.OFNS_DESC = hist['OFNS_DESC'].apply(lambda x: 'THEFT RELATED' if "BURGLAR’S TOOLS" in x else x)

# Find the average crime count after the shutdown in march.
crimeCountrec = recent.groupby(['ARREST_PRECINCT'])['OFNS_DESC'].value_counts().reset_index(name='Crime Count')
# Get all dates after the shutdown in march of 2020.
hisAfPand = hist[hist.ARREST_DATE > '2020-03-11']
#Count the average crime by offense type and find the average per year after march 2020.
hisAfPand = hisAfPand.groupby(['ARREST_PRECINCT'])['OFNS_DESC'].value_counts().reset_index(name='Crime Count')
hisAfPand['Crime Count'] = round(((hisAfPand['Crime Count'] + crimeCountrec['Crime Count'])/18.5)*12) 

# Average crime rate over the last 5 years
hisToPand = hist[hist.ARREST_DATE <= '2020-03-11']
histAvg = hisToPand.groupby(['ARREST_PRECINCT'])['OFNS_DESC'].value_counts().reset_index(name='Crime Count')
histAvg['Crime Count'] = round((histAvg['Crime Count']/62.5)*12)
histAvg.rename(columns = {'Crime Count':'Crime Count Historic Avg'},inplace = True)

# Merge histAvg and recentAvg and add new column to df to check if there was an increase in crime since covid.
merged = pd.merge(histAvg, hisAfPand)
# Make a new column to say if average crime rate of the last five years has increased since the shutdown.
merged['Increase in Crime'] = merged['Crime Count Historic Avg'] < merged['Crime Count']
merged['# Change'] = -(merged['Crime Count Historic Avg'] - merged['Crime Count']).astype(int)
merged['% Change'] = (round(merged['# Change']/merged['Crime Count Historic Avg'],4)*100)
merged.rename(columns = {'ARREST_PRECINCT':'Arrest Precinct', 'OFNS_DESC':'Offense Description'},inplace = True)
print(merged)
merged.to_csv('merged.csv', index = False)

# Group crime data by the date, and count the number of crimes for each crime type.
crimeCountHis = hist.groupby(['ARREST_DATE'])['OFNS_DESC'].value_counts().reset_index(name='Crime Count')
# Group crime data by the date and precinct, then count the number of crimes for each crime type.
crimeCountHisPre = hist.groupby(['ARREST_DATE', 'ARREST_PRECINCT'])['OFNS_DESC'].value_counts().reset_index(name='Crime Count')

# Folium Map configuration
m = folium.Map(location = [40.70554, -73.779417], zoom_start = 10)
with open('PolicePrecincts.geojson') as access_json:
            read_content = json.load(access_json)
features = read_content['features']
nodeData = os.path.join('PolicePrecincts.geojson')
# Add precinct popup to map
geo_json = folium.GeoJson(nodeData, popup=folium.GeoJsonPopup(fields=['precinct']))
geo_json.add_to(m)
# Save to file then open in web-browser
m.save(outfile="map.html")
webbrowser.open('map.html', new=2)

# # VISUALIZATION # #
# Make a lineplot to show the trend of crime over the last 5 years.
ax = sns.lineplot(data=crimeCountHis, x='ARREST_DATE', y='Crime Count', hue='OFNS_DESC', style = 'OFNS_DESC', ci=25, markers = True, dashes = False)
ax.set_title("Crime in Queens (2015-2020)", fontdict={'fontsize': 20})
plt.legend(bbox_to_anchor=(1, 1), loc="best", borderaxespad=-2.4)
plt.get_current_fig_manager().full_screen_toggle()
plt.xlabel('Arrest Year')
plt.show()

# Count by crime type for each precinct 
sns.countplot(data=recent, y='OFNS_DESC', hue = 'ARREST_PRECINCT', palette = 'bright', order = recent['OFNS_DESC'].value_counts().index).set_title("Crime in Queens by Preinct (YTD)", fontdict={'fontsize': 20})
sns.set_style('ticks')
plt.get_current_fig_manager().full_screen_toggle()
plt.xlabel('Crime Count')
plt.ylabel('Type of Crime')
plt.show()

# A function to show the value at the end of each bar in the countplot
def show_values(axs, space=.01):
    def _single(ax):
            for p in ax.patches:
                _x = p.get_x() + p.get_width() + float(space)
                _y = p.get_y() + p.get_height() - (p.get_height()*0.5)
                value = '{:}'.format(p.get_width())
                ax.text(_x, _y, value, ha="left")
    if isinstance(axs, np.ndarray):
        for idx, ax in np.ndenumerate(axs):
            _single(ax)
    else:
        _single(axs)

# Make chart to count number of crimes over the last year in queens
c = sns.countplot(data=recent, y='OFNS_DESC', order =recent['OFNS_DESC'].value_counts().index )
show_values(c)
c.set_title("Crime in Queens Year-to-date", fontdict={'fontsize': 20})
plt.xlabel('Crime Count')
plt.ylabel('Type of Crime')
plt.show()