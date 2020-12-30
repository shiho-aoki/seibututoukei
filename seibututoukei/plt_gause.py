import pandas as pd
import csv
import gause

import japanize_matplotlib
import matplotlib.pyplot as plt
import numpy as np

class PLTGause:
    def __init__(self, paths:list, point:str, datainfo:dict, filetitle:str):
        self.paths = paths
        self.point = point
        self.datainfo = datainfo
        self.filetitle = filetitle

    def caluc_main(self):
        data_set = []
        for path in self.paths:
            all_data = pd.read_csv(path)
            data = all_data[self.point].values.tolist()
            data_set.append(data)

        data_x = []
        data_y= []
        xtest= []
        sample_index= []
        var = []
        mu = []
        for d in data_set:
            data_x_, data_y_, xtest_, sample_index_, var_, mu_ = gause.GauseP(d)
            data_x.append(data_x_)
            data_y.append(data_y_)
            xtest.append(xtest_)
            sample_index.append(sample_index_)
            var.append(var_)
            mu.append(mu_)
        
        ans_path = "./analitics/GS/"+ self.filetitle +self.point+'.csv'
        with open(ans_path, 'w') as f:
            writer = csv.writer(f)
            writer.writerows(var)
            writer.writerows(mu)
        
        return data_x, data_y, sample_index, xtest, var, mu

    def plt_main(self):
        data_x, data_y, sample_index, xtest, var, mu = self.caluc_main()
        plt.figure(figsize=(12,8))
        plt.xlabel(self.datainfo['x_name'])
        plt.ylabel(self.datainfo['y_name'])
        plt.title(self.datainfo['title'], fontsize=20)

        for i in range(0, len(mu)):
            plt.plot(data_x[i], data_y[i], 'x', color='green', label='correct signal')
            plt.plot(data_x[i][sample_index[i]], data_y[i][sample_index[i]], 'o', color='red', label='sample dots')
            std = np.sqrt(var[i])
            plt.plot(xtest[i], mu[i], color='blue', label='ガウス過程回帰による平均')
            plt.fill_between(xtest[i], mu[i] + 2*std, mu[i] - 2*std, alpha=.2, color='blue', label= 'ガウス過程回帰による標準偏差')
        
        save_path = "./analitics/GS/img/"+self.datainfo['title']+'.png'
        plt.legend(title="凡例", bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0, fontsize=12)
        plt.tight_layout()
        plt.savefig(save_path)
        plt.close()