<header id = "top">
<h2><u> The Trend of Crime in Queens NYC</u></h2>
Your sense of safety largely depends on the crime rate of where you live. 
I used python dataframes from Pandas to clean data from nycOpenData provided by NYPD.
Then I used seaborn line-plots, count-plots and matplotlib.pyplot to display the data & visualize trends, and a folium map to display the area of each precinct. I then categorized which neighborhoods have had an increase in crime since the Covid-19 shutdown. I am trying to visualize and identify the trend of crime in Queens NYC.
</header>
<br/>

<header id = "data"> 
<h2><u>The Data</u></h2>
   <p> <a href="https://data.cityofnewyork.us/Public-Safety/NYPD-Arrests-Data-Historic-/8h9b-rp9u/" target="_blank" > Historic crime data</a> </p>
  <p><a href="https://data.cityofnewyork.us/Public-Safety/NYPD-Arrest-Data-Year-to-Date-/uip8-fykc " target="_blank" >Recent crime data   </a></p>
   <p> <a href="https://data.cityofnewyork.us/Public-Safety/Police-Precincts/78dh-3ptz" target="_blank" > Police precincts GeoJson</a></p> 
</header>
 
<header id = "code">
<h2><u>The Code</u></h2>
<a href="https://github.com/elchic00/CrimeInQueens/blob/main/CrimeData.py" target="_blank" > Repository to the Python code</a>
</header>

<header id = "vis"> </header>
<h2><u>Visualizations</u></h2>

<h4 style="text-align:center"> This shows the total number of arrests in Queens NYC over the last five years (2015-2020) </h4>
![Total historical crime](historicCrime.png)

<h4 style="text-align:center"> This chart shows the total number of arrests in Queens NYC (YTD 2021) </h4>
![Total crime in queens this year](yearToDateQueens.png)

<h4 style="text-align:center"> This chart shows the crime in Queens by precinct (YTD 2021) </h4>
![Crimes by precinct in queens](crimesByPrec.png)
    

<h4 style="text-align:center"> You can use the map while viewing the histogram and table to see where each precinct is located and find the precinct covering your neighborhood </h4>
<iframe style="text-align:center" src="map.html" height="500" width="500"></iframe>

<h4 style="text-align:center"> You can use the table below to see which precincts and types of crime have increased since March of 2020 (Post Covid-19 shut-down) </h4>

<a href="#top" class="back-to-top">
  Back to Top &uarr;
</a>

|Arrest Precinct|Offense Description|Crime Count Historic Avg|Crime Count|Increase in Crime|# Change|
|---------------|-------------------|------------------------|-----------|-----------------|--------|
|100            |ASSAULT            |247.0                   |166.0      |False            |-81     |
|100            |PETIT LARCENY      |131.0                   |38.0       |False            |-93     |
|100            |FELONY ASSAULT     |112.0                   |112.0      |False            |0       |
|100            |GRAND LARCENY      |48.0                    |18.0       |False            |-30     |
|100            |ROBBERY            |41.0                    |36.0       |False            |-5      |
|100            |BURGLARY           |32.0                    |26.0       |False            |-6      |
|100            |SEX CRIMES         |27.0                    |16.0       |False            |-11     |
|100            |FRAUD              |10.0                    |8.0        |False            |-2      |
|100            |CAR THEFT          |7.0                     |6.0        |False            |-1      |
|101            |ASSAULT            |413.0                   |146.0      |False            |-267    |
|101            |FELONY ASSAULT     |257.0                   |245.0      |False            |-12     |
|101            |ROBBERY            |108.0                   |139.0      |True             |31      |
|101            |PETIT LARCENY      |71.0                    |62.0       |False            |-9      |
|101            |BURGLARY           |52.0                    |47.0       |False            |-5      |
|101            |SEX CRIMES         |51.0                    |43.0       |False            |-8      |
|101            |GRAND LARCENY      |46.0                    |27.0       |False            |-19     |
|101            |FRAUD              |27.0                    |8.0        |False            |-19     |
|101            |CAR THEFT          |15.0                    |23.0       |True             |8       |
|101            |RAPE               |8.0                     |8.0        |False            |0       |
|102            |ASSAULT            |520.0                   |187.0      |False            |-333    |
|102            |FELONY ASSAULT     |206.0                   |120.0      |False            |-86     |
|102            |GRAND LARCENY      |188.0                   |73.0       |False            |-115    |
|102            |PETIT LARCENY      |138.0                   |270.0      |True             |132     |
|102            |ROBBERY            |91.0                    |142.0      |True             |51      |
|102            |FRAUD              |62.0                    |41.0       |False            |-21     |
|102            |BURGLARY           |60.0                    |63.0       |True             |3       |
|102            |SEX CRIMES         |53.0                    |56.0       |True             |3       |
|102            |CAR THEFT          |32.0                    |32.0       |False            |0       |
|102            |THEFT RELATED      |25.0                    |11.0       |False            |-14     |
|102            |RAPE               |9.0                     |20.0       |True             |11      |
|102            |BURGLAR'S TOOLS    |5.0                     |15.0       |True             |10      |
|103            |ASSAULT            |607.0                   |226.0      |False            |-381    |
|103            |THEFT RELATED      |457.0                   |25.0       |False            |-432    |
|103            |FELONY ASSAULT     |291.0                   |382.0      |True             |91      |
|103            |PETIT LARCENY      |258.0                   |169.0      |False            |-89     |
|103            |ROBBERY            |237.0                   |283.0      |True             |46      |
|103            |GRAND LARCENY      |95.0                    |137.0      |True             |42      |
|103            |FRAUD              |80.0                    |32.0       |False            |-48     |
|103            |BURGLARY           |60.0                    |97.0       |True             |37      |
|103            |SEX CRIMES         |45.0                    |51.0       |True             |6       |
|103            |CAR THEFT          |33.0                    |71.0       |True             |38      |
|103            |RAPE               |8.0                     |5.0        |False            |-3      |
|103            |BURGLAR'S TOOLS    |7.0                     |14.0       |True             |7       |
|104            |ASSAULT            |440.0                   |411.0      |False            |-29     |
|104            |PETIT LARCENY      |246.0                   |221.0      |False            |-25     |
|104            |FELONY ASSAULT     |148.0                   |180.0      |True             |32      |
|104            |GRAND LARCENY      |112.0                   |54.0       |False            |-58     |
|104            |ROBBERY            |102.0                   |80.0       |False            |-22     |
|104            |BURGLARY           |62.0                    |62.0       |False            |0       |
|104            |SEX CRIMES         |41.0                    |44.0       |True             |3       |
|104            |FRAUD              |18.0                    |11.0       |False            |-7      |
|104            |BURGLAR'S TOOLS    |15.0                    |25.0       |True             |10      |
|104            |CAR THEFT          |13.0                    |8.0        |False            |-5      |
|104            |RAPE               |5.0                     |3.0        |False            |-2      |
|105            |ASSAULT            |609.0                   |426.0      |False            |-183    |
|105            |FELONY ASSAULT     |281.0                   |285.0      |True             |4       |
|105            |ROBBERY            |116.0                   |108.0      |False            |-8      |
|105            |GRAND LARCENY      |106.0                   |62.0       |False            |-44     |
|105            |PETIT LARCENY      |92.0                    |90.0       |False            |-2      |
|105            |BURGLARY           |69.0                    |43.0       |False            |-26     |
|105            |SEX CRIMES         |47.0                    |55.0       |True             |8       |
|105            |CAR THEFT          |45.0                    |35.0       |False            |-10     |
|105            |FRAUD              |29.0                    |32.0       |True             |3       |
|105            |RAPE               |6.0                     |8.0        |True             |2       |
|105            |BURGLAR'S TOOLS    |3.0                     |14.0       |True             |11      |
|106            |ASSAULT            |410.0                   |392.0      |False            |-18     |
|106            |FELONY ASSAULT     |192.0                   |231.0      |True             |39      |
|106            |PETIT LARCENY      |161.0                   |93.0       |False            |-68     |
|106            |GRAND LARCENY      |127.0                   |104.0      |False            |-23     |
|106            |ROBBERY            |122.0                   |80.0       |False            |-42     |
|106            |BURGLARY           |63.0                    |26.0       |False            |-37     |
|106            |SEX CRIMES         |39.0                    |42.0       |True             |3       |
|106            |CAR THEFT          |31.0                    |52.0       |True             |21      |
|106            |FRAUD              |17.0                    |15.0       |False            |-2      |
|106            |RAPE               |5.0                     |8.0        |True             |3       |
|107            |ASSAULT            |328.0                   |279.0      |False            |-49     |
|107            |PETIT LARCENY      |139.0                   |67.0       |False            |-72     |
|107            |ROBBERY            |126.0                   |82.0       |False            |-44     |
|107            |FELONY ASSAULT     |123.0                   |129.0      |True             |6       |
|107            |THEFT RELATED      |101.0                   |172.0      |True             |71      |
|107            |GRAND LARCENY      |100.0                   |85.0       |False            |-15     |
|107            |BURGLARY           |47.0                    |50.0       |True             |3       |
|107            |FRAUD              |30.0                    |34.0       |True             |4       |
|107            |SEX CRIMES         |30.0                    |18.0       |False            |-12     |
|107            |CAR THEFT          |14.0                    |33.0       |True             |19      |
|107            |RAPE               |6.0                     |3.0        |False            |-3      |
|107            |BURGLAR'S TOOLS    |5.0                     |7.0        |True             |2       |
|108            |ASSAULT            |340.0                   |191.0      |False            |-149    |
|108            |FELONY ASSAULT     |109.0                   |93.0       |False            |-16     |
|108            |GRAND LARCENY      |99.0                    |45.0       |False            |-54     |
|108            |PETIT LARCENY      |82.0                    |41.0       |False            |-41     |
|108            |ROBBERY            |57.0                    |53.0       |False            |-4      |
|108            |BURGLARY           |28.0                    |61.0       |True             |33      |
|108            |SEX CRIMES         |28.0                    |42.0       |True             |14      |
|108            |FRAUD              |21.0                    |30.0       |True             |9       |
|108            |CAR THEFT          |12.0                    |6.0        |False            |-6      |
|108            |BURGLAR'S TOOLS    |7.0                     |3.0        |False            |-4      |
|109            |PETIT LARCENY      |730.0                   |272.0      |False            |-458    |
|109            |ASSAULT            |538.0                   |394.0      |False            |-144    |
|109            |ROBBERY            |225.0                   |148.0      |False            |-77     |
|109            |FELONY ASSAULT     |206.0                   |167.0      |False            |-39     |
|109            |GRAND LARCENY      |180.0                   |122.0      |False            |-58     |
|109            |BURGLARY           |88.0                    |85.0       |False            |-3      |
|109            |SEX CRIMES         |54.0                    |51.0       |False            |-3      |
|109            |FRAUD              |31.0                    |36.0       |True             |5       |
|109            |BURGLAR'S TOOLS    |25.0                    |18.0       |False            |-7      |
|109            |CAR THEFT          |13.0                    |14.0       |True             |1       |
|109            |RAPE               |9.0                     |3.0        |False            |-6      |
|110            |PETIT LARCENY      |751.0                   |253.0      |False            |-498    |
|110            |ASSAULT            |536.0                   |473.0      |False            |-63     |
|110            |FELONY ASSAULT     |245.0                   |323.0      |True             |78      |
|110            |ROBBERY            |163.0                   |125.0      |False            |-38     |
|110            |GRAND LARCENY      |153.0                   |91.0       |False            |-62     |
|110            |BURGLARY           |55.0                    |49.0       |False            |-6      |
|110            |SEX CRIMES         |51.0                    |81.0       |True             |30      |
|110            |FRAUD              |37.0                    |21.0       |False            |-16     |
|110            |BURGLAR'S TOOLS    |24.0                    |15.0       |False            |-9      |
|110            |CAR THEFT          |16.0                    |25.0       |True             |9       |
|110            |RAPE               |10.0                    |7.0        |False            |-3      |
|111            |ASSAULT            |141.0                   |115.0      |False            |-26     |
|111            |PETIT LARCENY      |71.0                    |32.0       |False            |-39     |
|111            |GRAND LARCENY      |58.0                    |16.0       |False            |-42     |
|111            |FELONY ASSAULT     |56.0                    |60.0       |True             |4       |
|111            |BURGLARY           |37.0                    |21.0       |False            |-16     |
|111            |ROBBERY            |29.0                    |13.0       |False            |-16     |
|111            |SEX CRIMES         |13.0                    |20.0       |True             |7       |
|111            |CAR THEFT          |7.0                     |6.0        |False            |-1      |
|111            |BURGLAR'S TOOLS    |5.0                     |8.0        |True             |3       |
|112            |PETIT LARCENY      |325.0                   |164.0      |False            |-161    |
|112            |SEX CRIMES         |174.0                   |74.0       |False            |-100    |
|112            |ASSAULT            |151.0                   |134.0      |False            |-17     |
|112            |RAPE               |98.0                    |93.0       |False            |-5      |
|112            |FELONY ASSAULT     |89.0                    |71.0       |False            |-18     |
|112            |GRAND LARCENY      |82.0                    |57.0       |False            |-25     |
|112            |ROBBERY            |24.0                    |44.0       |True             |20      |
|112            |BURGLARY           |18.0                    |38.0       |True             |20      |
|112            |BURGLAR'S TOOLS    |13.0                    |15.0       |True             |2       |
|112            |FRAUD              |11.0                    |5.0        |False            |-6      |
|112            |CAR THEFT          |7.0                     |19.0       |True             |12      |
|113            |ASSAULT            |746.0                   |244.0      |False            |-502    |
|113            |FELONY ASSAULT     |302.0                   |376.0      |True             |74      |
|113            |PETIT LARCENY      |222.0                   |216.0      |False            |-6      |
|113            |GRAND LARCENY      |155.0                   |125.0      |False            |-30     |
|113            |ROBBERY            |110.0                   |85.0       |False            |-25     |
|113            |FRAUD              |94.0                    |73.0       |False            |-21     |
|113            |BURGLARY           |57.0                    |51.0       |False            |-6      |
|113            |SEX CRIMES         |57.0                    |47.0       |False            |-10     |
|113            |CAR THEFT          |42.0                    |57.0       |True             |15      |
|113            |RAPE               |10.0                    |29.0       |True             |19      |
|113            |BURGLAR'S TOOLS    |7.0                     |11.0       |True             |4       |
|114            |ASSAULT            |652.0                   |246.0      |False            |-406    |
|114            |PETIT LARCENY      |296.0                   |439.0      |True             |143     |
|114            |FELONY ASSAULT     |257.0                   |264.0      |True             |7       |
|114            |ROBBERY            |145.0                   |202.0      |True             |57      |
|114            |GRAND LARCENY      |133.0                   |136.0      |True             |3       |
|114            |BURGLARY           |55.0                    |108.0      |True             |53      |
|114            |SEX CRIMES         |46.0                    |67.0       |True             |21      |
|114            |FRAUD              |37.0                    |63.0       |True             |26      |
|114            |CAR THEFT          |15.0                    |45.0       |True             |30      |
|114            |BURGLAR'S TOOLS    |11.0                    |8.0        |False            |-3      |
|114            |RAPE               |7.0                     |9.0        |True             |2       |
|115            |ASSAULT            |753.0                   |235.0      |False            |-518    |
|115            |FELONY ASSAULT     |282.0                   |407.0      |True             |125     |
|115            |PETIT LARCENY      |220.0                   |195.0      |False            |-25     |
|115            |THEFT RELATED      |200.0                   |12.0       |False            |-188    |
|115            |ROBBERY            |165.0                   |114.0      |False            |-51     |
|115            |GRAND LARCENY      |137.0                   |117.0      |False            |-20     |
|115            |SEX CRIMES         |89.0                    |128.0      |True             |39      |
|115            |BURGLARY           |61.0                    |88.0       |True             |27      |
|115            |FRAUD              |41.0                    |28.0       |False            |-13     |
|115            |CAR THEFT          |27.0                    |36.0       |True             |9       |
|115            |BURGLAR'S TOOLS    |15.0                    |19.0       |True             |4       |
|115            |RAPE               |12.0                    |4.0        |False            |-8      |
