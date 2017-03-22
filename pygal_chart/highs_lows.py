# -*- coding:utf-8 -*-

import csv
import matplotlib.pyplot as plt
from datetime import datetime

# filename = 'sitka_weather_07-2014.csv'
# filename = 'sitka_weather_2014.csv'
filename = 'death_valley_2014.csv'
with open(filename,'r') as f:
    reader = csv.reader(f)
    header_row = next(reader)
    dates, highs, lows = [],[],[]
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[2])
        except ValueError:
            print (current_date, 'missing data')
        else:
            dates.append(current_date)
            lows.append(low)
            highs.append(high)

fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.4)
plt.title("Daily high temperature, July 2014", fontsize=24)
plt.xlabel('',fontsize=16)
plt.ylabel('Temperature (F)',fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)
plt.show()