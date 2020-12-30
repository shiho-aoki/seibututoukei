import csv
import gause
import japanize_matplotlib

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Tokyo
titile = 'TOKYO'

data1990 = pd.read_csv('data\Tokyo_1990 - Tokyo1990.csv')
data_pressure1 = data1990['vap_pressure'].values.tolist()
data_humidity1 = data1990['humidity'].values.tolist()

data1995 = pd.read_csv('data\Tokyo1995.csv')
data_pressure2 = data1995['vap_pressure'].values.tolist()
data_humidity2 = data1995['humidity'].values.tolist()

data2000 = pd.read_csv('data\Tokyo_2000 - Tokyo2000.csv')
data_pressure3 = data2000['vap_pressure'].values.tolist()
data_humidity3 = data2000['humidity'].values.tolist()

data2005 = pd.read_csv('data\Tokyo_2005.csv')
data_pressure4 = data2005['vap_pressure'].values.tolist()
data_humidity4 = data2005['humidity'].values.tolist()

data2010 = pd.read_csv('data\Tokyo_2010 - Tokyo2010.csv')
data_pressure5 = data2010['vap_pressure'].values.tolist()
data_humidity5 = data2010['humidity'].values.tolist()

data_pressure = [data_pressure1, data_pressure2, data_pressure3, data_pressure4, data_pressure5]
data_humidity = [data_humidity1, data_humidity2, data_humidity3, data_humidity4, data_humidity5]

data_x = []
data_y= []
xtest= []
sample_index= []
var= []
mu= []
for data in data_pressure:
    data_x_, data_y_, xtest_, sample_index_, var_, mu_ = gause.GauseP(data)
    data_x.append(data_x_)
    data_y.append(data_y_)
    xtest.append(xtest_)
    sample_index.append(sample_index_)
    var.append(var_)
    mu.append(mu_)

with open ('data/ans/gause_press'+titile+'w.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(data_x)
    writer.writerows(data_y)
    writer.writerows(xtest)
    writer.writerows(sample_index)
    writer.writerows(var)
    writer.writerows(mu)

plt.figure(figsize=(10, 5))
plt.xlabel("時間(day)")
plt.ylabel("水蒸気圧(hPa)")
plt.title('signal prediction by Gaussian process', fontsize=20)
for i in range(0,len(mu)):
    plt.plot(data_x[i], data_y[i], 'x', color='green', label='correct signal')
    plt.plot(data_x[i][sample_index[i]], data_y[i][sample_index[i]], 'o', color='red', label='sample dots')
    std = np.sqrt(var[i])
    plt.plot(xtest[i], mu[i], color='blue', label='mean by Gaussian process')
    plt.fill_between(xtest[i], mu[i] + 2*std, mu[i] - 2*std, alpha=.2, color='blue', label= 'standard deviation by Gaussian process')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0, fontsize=12)
plt.show()