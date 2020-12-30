import pandas as pd
import os

rootname = r"./analitics/GS/csv"
files = os.listdir(rootname)

col_name = [i for i in range(1, 367)]
save_base_path = r'./analitics/GS/SummaryStatistics/'
for filename in files:
    csv_path = os.path.join(rootname, filename)
    data = pd.read_csv(csv_path, names=col_name)

    ave = data.mean(axis="columns")
    var_ave = ave[:5]
    var_ave.index=['1990年', '1995年', '2000年', '2005年', '2010年']
    ave_ave = ave[5:]
    ave_ave.index=['1990年', '1995年', '2000年', '2005年', '2010年']

    var = data.var(axis="columns")
    var_var = var[:5]
    var_var.index=['1990年', '1995年', '2000年', '2005年', '2010年']
    ave_var = var[5:]
    ave_var.index=['1990年', '1995年', '2000年', '2005年', '2010年']

    discribe = pd.concat({
        'var_ave': var_ave,
        'var_var': var_var,
        'ave_ave': ave_ave,
        'ave_var': ave_var
    }, axis=1)

    discribe.to_csv(save_base_path+filename)