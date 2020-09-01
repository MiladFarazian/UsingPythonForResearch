"""
Using Python for Research Homework: Week 4, Case Study 2
In this case study, we will continue taking a look at patterns 
of flight for each of the three birds in our dataset.
"""
# DO NOT EDIT THIS CODE
import pandas as pd
import numpy as np
birddata = pd.read_csv("https://courses.edx.org/asset-v1:HarvardX+PH526x+2T2019+type@asset+block@bird_tracking.csv", index_col=0)

"""
Exercise 1
In this case study, we will continue taking a look at patterns 
of flight for each of the three birds in our dataset. We will 
group the flight patterns by bird and date, and plot the mean 
altitude for these groupings.

pandas makes it easy to perform basic operations on groups within 
a dataframe without needing to loop through each value in the 
dataframe. In this exercise, we will group the dataframe by 
birdname and then find the average speed_2d for each bird.

Instructions
Fill in the code to find the mean altitudes of each bird using 
the pre-loaded birddata dataframe.
"""
grouped_birds = birddata.groupby("bird_name")
mean_speeds = grouped_birds.speed_2d.mean()
mean_altitudes = grouped_birds.altitude.mean()
​
mean_altitudes

"""
bird_name
Eric     60.249406
Nico     67.900478
Sanne    29.159922
Name: altitude, dtype: float64

Exercise 2
In this exercise, we will group the flight times by date and 
calculate the mean altitude within that day.

Instructions
Convert birddata.date_time to the pd.datetime format, extract 
the date, and store it as birddata["date"].
Fill in the code to find the mean altitudes for each day.
What is the mean altitude of the birds on 2013-09-12? 
(Hint: You will need to convert this to a datetime object as 
well, extract the date, and then use this to index into the 
dataframe.)
"""

birddata.date_time = pd.to_datetime(birddata.date_time)
birddata["date"] = birddata.date_time.dt.date
grouped_bydates = birddata.groupby("date")
mean_altitudes_perday = grouped_bydates.altitude.mean()
​
mean_altitudes_perday

"""
date
2013-08-15    134.092000
2013-08-16    134.839506
2013-08-17    147.439024
2013-08-18    129.608163
2013-08-19    180.174797
                 ...    
2014-04-26     15.118012
2014-04-27     23.897297
2014-04-28     37.716867
2014-04-29     19.244792
2014-04-30     13.954545
Name: altitude, Length: 259, dtype: float64

Exercise 3
In this exercise, we will group the flight times by both bird 
and date, and calculate the mean altitude for each.

Instructions
birddata already contains the date column. To find the average 
speed for each bird and day, create a new grouped dataframe called 
grouped_birdday that groups the data by both bird_name and date.
"""

grouped_birdday = birddata.groupby(["bird_name", "date"])
mean_altitudes_perday = grouped_birdday.altitude.mean()
​
# look at the head of `mean_altitudes_perday`.
mean_altitudes_perday.head()
​
"""
bird_name  date      
Eric       2013-08-15     74.988095
           2013-08-16    127.773810
           2013-08-17    125.890244
           2013-08-18    121.353659
           2013-08-19    134.928571
Name: altitude, dtype: float64

Exercise 4
Great! Now find the average speed for each bird and day.

Instructions
Store these are three pandas Series objects, one for each bird.
Use the plotting code provided to plot the average speeds for 
each bird.
"""

import matplotlib.pyplot as plt
​
eric_daily_speed  = grouped_birdday.speed_2d.mean()["Eric"]
sanne_daily_speed = grouped_birdday.speed_2d.mean()["Sanne"]
nico_daily_speed  = grouped_birdday.speed_2d.mean()["Nico"]
​
eric_daily_speed.plot(label="Eric")
sanne_daily_speed.plot(label="Sanne")
nico_daily_speed.plot(label="Nico")
plt.legend(loc="upper left")
plt.show()
​
nico_daily_speed[200:]

"""
date
2014-03-03     2.732428
2014-03-04     2.878018
2014-03-05     2.404222
2014-03-06     2.847120
2014-03-07     2.690564
2014-03-08     2.908432
2014-03-09     2.757326
2014-03-10     2.969922
2014-03-11     3.093018
2014-03-12     2.707914
2014-03-13     2.853118
2014-03-14     2.333892
2014-03-15     2.849500
2014-03-16     2.520370
2014-03-17     2.739105
2014-03-18     3.468390
2014-03-19     2.730760
2014-03-20     2.718993
2014-03-21     2.512176
2014-03-22     3.277353
2014-03-23     2.400540
2014-03-24     3.338499
2014-03-25     2.348788
2014-03-26     2.421999
2014-03-27     2.944375
2014-03-28     2.833248
2014-03-29     3.550028
2014-03-30     2.176832
2014-03-31     2.824631
2014-04-01     3.163723
2014-04-02     2.861222
2014-04-03     3.212099
2014-04-04     2.832465
2014-04-05     3.283842
2014-04-06     2.824700
2014-04-07     3.455989
2014-04-08     2.995421
2014-04-09     3.780186
2014-04-10     3.703409
2014-04-11     2.829536
2014-04-12     3.341111
2014-04-13     3.878121
2014-04-14     3.882314
2014-04-15     4.437659
2014-04-16     3.366451
2014-04-17     3.713230
2014-04-18     3.798646
2014-04-19     5.061530
2014-04-20    10.196981
2014-04-21     7.861385
2014-04-22     9.445087
2014-04-23     6.384096
2014-04-24     2.674536
2014-04-25     2.705160
2014-04-26     2.192028
2014-04-27     2.582072
2014-04-28     3.055051
2014-04-29     2.793232
2014-04-30     3.297032
Name: speed_2d, dtype: float64
"""