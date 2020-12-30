import csv
import japanize_matplotlib

import pandas as pd
import matplotlib.pyplot as plt

import moving_average as ma

#Analitics Weather data
#Tokyo
titile = 'TOKYO'

data1990 = pd.read_csv('data/Tokyo_1990 - Tokyo1990.csv')
temp_rolling1 = ma.MovingAverage(data1990['temp'])
vap_pressure_rolling1 = ma.MovingAverage(data1990['vap_pressure'])
humidity_rolling1 = ma.MovingAverage(data1990['humidity'])

data1995 = pd.read_csv('data/Tokyo1995.csv')
temp_rolling1 = ma.MovingAverage(data1995['temp'])
vap_pressure_rolling1 = ma.MovingAverage(data1995['vap_pressure'])
humidity_rolling1 = ma.MovingAverage(data1995['humidity'])

data2000 = pd.read_csv('data/Tokyo_2000 - Tokyo2000.csv')
temp_rolling2 = ma.MovingAverage(data2000['temp'])
vap_pressure_rolling2 = ma.MovingAverage(data2000['vap_pressure'])
humidity_rolling2 = ma.MovingAverage(data2000['humidity'])

data2005 = pd.read_csv('data/Tokyo_2005.csv')
temp_rolling2 = ma.MovingAverage(data2005['temp'])
vap_pressure_rolling2 = ma.MovingAverage(data2005['vap_pressure'])
humidity_rolling2 = ma.MovingAverage(data2005['humidity'])

data2010 = pd.read_csv('data/Tokyo_2010 - Tokyo2010.csv')
temp_rolling3 = ma.MovingAverage(data2010['temp'])
vap_pressure_rolling3 = ma.MovingAverage(data2010['vap_pressure'])
humidity_rolling3 = ma.MovingAverage(data2010['humidity'])

y1 = data1900['Date']
y2 = data2000['Date']
y3 = data2010['Date']
y_ = [y1, y2, y3]
y_a = [range(0,len(y1)), range(0,len(y2)), range(0,len(y3))]
x1 = [temp_rolling1, temp_rolling2, temp_rolling3]
x2 = [vap_pressure_rolling1, vap_pressure_rolling2, vap_pressure_rolling3]
x3 = [humidity_rolling1, humidity_rolling2, humidity_rolling3]

label_temp = ["1900 気温", "2000 気温", "2010 気温"]
label_pressure = ["1900 気圧", "2000 気圧", "2010 気圧"]
label_humidity = ["1900　湿度","2000 湿度","2010 湿度"]

with open ('data/ans/average_moving_'+titile+'w.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(x1)
    writer.writerows(x2)
    writer.writerows(x3)
#temp
i = 0
for y,x in zip(y_a, x1):
    plt.plot(y, x, label=label_temp[i])
    i += 1
plt.legend(title='凡例', borderaxespad=0, loc='upper left', bbox_to_anchor=(1,1), fontsize=9, ncol=2)
plt.tight_layout()
plt.show()

#presseur
# i = 0
# for y,x in zip(y_a, x2):
#     plt.plot(y, x, label=label_pressure[i])
#     i += 1
# plt.legend(title='凡例', borderaxespad=0, loc='upper left', bbox_to_anchor=(1,1), fontsize=9, ncol=2)
# plt.tight_layout()
# plt.show()

#humidity
# i = 0
# for y,x in zip(y_a, x3):
#     plt.plot(y, x, label=label_humidity[i])
#     i += 1
# plt.legend(title='凡例', borderaxespad=0, loc='upper left', bbox_to_anchor=(1,1), fontsize=9, ncol=2)
# plt.tight_layout()
# plt.show()