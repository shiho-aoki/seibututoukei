import os

rootname = r"C:\Users\saoki\project\02_mywork\seibutsutoukei\Analitics\seibututoukei\analitics\GS\SummaryStatistics"
files = os.listdir(rootname)
label_list = [
    'data_atm_p','data_humid','data_tpmax','data_tpmin','data_tempe','data_vap_p','data_wethe',
    'data_atm_p','data_humid','data_tpmax','data_tpmin','data_tempe','data_vap_p','data_wethe',
    'data_atm_p','data_humid','data_tpmax','data_tpmin','data_tempe','data_vap_p','data_wethe',
    'data_atm_p','data_humid','data_tpmax','data_tpmin','data_tempe','data_vap_p','data_wethe',
    'data_atm_p','data_humid','data_tpmax','data_tpmin','data_tempe','data_vap_p','data_wethe',
    'data_atm_p','data_humid','data_tpmax','data_tpmin','data_tempe','data_vap_p','data_wethe']

i=0
for filename,label in zip(files, label_list):
    if i%7 == 0:
        print("")
    path = os.path.join(rootname, filename)
    path_name = str(path)
    path_name = path_name.replace('\\' ,"//")
    path_for_r = label+ ' <- read.csv("'+path_name+'")'
    print(path_for_r)
    i+=1