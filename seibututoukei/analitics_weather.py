#python default library
import csv
#python threed party library
import japanize_matplotlib
import pandas as pd
import matplotlib.pyplot as plt
#module made by me(shiho aoki)
import moving_average as ma

class PltMovingAveFigure:
    """plot data function
        datainfo must be following shape.

        datainfo = {"title":title, "x_name":x_name,"y_name":y_name, "label":lables}
    """
    def __init__(self, path:list, datainfo:dict, point:str):
        self.path = path
        self.datainfo = datainfo
        if point == 'temp':
            self.data_point = 'temp'
        elif point == 'vap':
            self.data_point = 'vap_pressure'
        elif point == 'hum':
            self.data_point = 'humidity'
        elif point == 'atm':
            self.data_point = 'atm_pressure'
        elif point == 'tp_max':
            self.data_point = 'temp_max'
        elif point == 'tp_min':
            self.data_point = 'temp_min'
        elif point == 'weather':
            self.data_point = 'weather_num'
        else:
            raise AttributeError

    def __make_moving_ave(self):
        x_data = []
        y_data = []
        for data_path in self.path:
            data = pd.read_csv(data_path)
            rolling = ma.MovingAverage(data[self.data_point])
            y = data['Date']
            x_data.append(rolling)
            y_data.append(y)
        return y_data, x_data

    def plt_moving_ave(self):
        y, x_axis = self.__make_moving_ave()
        saving_path = "./analitics/MovingAve_Img"+str(self.datainfo['title'])+".png"
        print(saving_path)
        i = 0
        title = self.datainfo['title']
        y_axis = []
        for y_ in y:
            y_memb = range(0, len(y_))
            y_axis.append(y_memb)
        
        plt.title(self.datainfo['title'])
        plt.xlabel(self.datainfo['x_name'])
        plt.ylabel(self.datainfo['y_name'])

        for y, x in zip(y_axis, x_axis):
            plt.plot(y, x, label=self.datainfo['label'][i])
            i += 1
        plt.legend(title='凡例', borderaxespad=0, loc='upper left', bbox_to_anchor=(1,1), fontsize=9, ncol=2)
        plt.tight_layout()
        plt.savefig(saving_path)
        #plt.show()

##for analisis
def make_y_name(point_num):
    if point_num == 'temp':
        point_y = "気温 (℃)"
        return point_y
    elif point_num == 'vap':
        point_y = "水蒸気圧 (hPa)"
        return point_y
    elif point_num == 'hum':
        point_y = "湿度 (%)"
        return point_y
    elif point_num == 'atm':
        point_y = "大気圧 (hPa)"
        return point_y
    elif point_num == 'tp_max':
        point_y = "最高気温　(℃)"
        return point_y
    elif point_num == 'tp_min':
        point_y = "最低気温　(℃)"
        return point_y
    elif point_num == 'weather':
        point_y = "天気概要"
        return point_y

def make_csv_path(base_path):
    paths = []
    years = ['1990','1995','2000','2005','2010']
    for year in years:
        path = base_path + year + '.csv'
        paths.append(path)
    return paths

point = ['temp','vap','hum','atm','tp_max','tp_min','weather']
#===TOKYO===========
base_path = r'data\weather\Tokyo'
paths = make_csv_path(base_path)
##temp
point = 'temp'
point_y = make_y_name(point)
datainfo_TOKYO = {
    "title": "東京都" + str(point_y) + "移動平均足", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

MA_Tokyo_t = PltMovingAveFigure(paths, datainfo_TOKYO, point)
MA_Tokyo_t.plt_moving_ave()

##vap
point = 'vap'
point_y = make_y_name(point)
datainfo_TOKYO = {
    "title": "東京都" + str(point_y) + "移動平均足", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

MA_Tokyo_v = PltMovingAveFigure(paths, datainfo_TOKYO, point)
MA_Tokyo_v.plt_moving_ave()

##hum
point = 'hum'
point_y = make_y_name(point)
datainfo_TOKYO = {
    "title": "東京都" + str(point_y) + "移動平均足", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

MA_Tokyo_h = PltMovingAveFigure(paths, datainfo_TOKYO, point)
MA_Tokyo_h.plt_moving_ave()

##atm
point = 'atm'
point_y = make_y_name(point)
datainfo_TOKYO = {
    "title": "東京都" + str(point_y) + "移動平均足", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

MA_Tokyo_a = PltMovingAveFigure(paths, datainfo_TOKYO, point)
MA_Tokyo_a.plt_moving_ave()

##tp_max
point = 'tp_max'
point_y = make_y_name(point)
datainfo_TOKYO = {
    "title": "東京都" + str(point_y) + "移動平均足", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

MA_Tokyo_tma = PltMovingAveFigure(paths, datainfo_TOKYO, point)
MA_Tokyo_tma.plt_moving_ave()

##tp_min
point = 'tp_min'
point_y = make_y_name(point)
datainfo_TOKYO = {
    "title": "東京都" + str(point_y) + "移動平均足", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

MA_Tokyo_tmi = PltMovingAveFigure(paths, datainfo_TOKYO, point)
MA_Tokyo_tmi.plt_moving_ave()

##weather
point = 'weather'
point_y = make_y_name(point)
datainfo_TOKYO = {
    "title": "東京都" + str(point_y) + "移動平均足", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

MA_Tokyo_w = PltMovingAveFigure(paths, datainfo_TOKYO, point)
MA_Tokyo_w.plt_moving_ave()


#===Sapporo=========
base_path = r'data\weather\Sapporo'
paths = make_csv_path(base_path)
##temp
point = 'temp'
point_y = make_y_name(point)
datainfo = {
    "title": "札幌市" + str(point_y) + "移動平均足", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

MA_Sapporo_t = PltMovingAveFigure(paths, datainfo, point)
MA_Sapporo_t.plt_moving_ave()

##vap
point = 'vap'
point_y = make_y_name(point)
datainfo = {
    "title": "札幌市" + str(point_y) + "移動平均足", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

MA_Sapporo_v = PltMovingAveFigure(paths, datainfo, point)
MA_Sapporo_v.plt_moving_ave()

##hum
point = 'hum'
point_y = make_y_name(point)
datainfo = {
    "title": "札幌市" + str(point_y) + "移動平均足", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

MA_Sapporo_h = PltMovingAveFigure(paths, datainfo, point)
MA_Sapporo_h.plt_moving_ave()

##atm
point = 'atm'
point_y = make_y_name(point)
datainfo = {
    "title": "札幌市" + str(point_y) + "移動平均足", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

MA_Sapporo_a = PltMovingAveFigure(paths, datainfo, point)
MA_Sapporo_a.plt_moving_ave()

##tp_max
point = 'tp_max'
point_y = make_y_name(point)
datainfo = {
    "title": "札幌市" + str(point_y) + "移動平均足", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

MA_Sapporo_tma = PltMovingAveFigure(paths, datainfo, point)
MA_Sapporo_tma.plt_moving_ave()

##tp_min
point = 'tp_min'
point_y = make_y_name(point)
datainfo = {
    "title": "札幌市" + str(point_y) + "移動平均足", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

MA_Sapporo_tmi = PltMovingAveFigure(paths, datainfo, point)
MA_Sapporo_tmi.plt_moving_ave()

##weather
point = 'weather'
point_y = make_y_name(point)
datainfo = {
    "title": "札幌市" + str(point_y) + "移動平均足", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

MA_Sapporo_w = PltMovingAveFigure(paths, datainfo, point)
MA_Sapporo_w.plt_moving_ave()

#===Osaka===========
base_path = r'data\weather\Osaka'
paths = make_csv_path(base_path)
##temp
point = 'temp'
point_y = make_y_name(point)
datainfo = {
    "title": "大阪市" + str(point_y) + "移動平均足", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

MA_Osaka_t = PltMovingAveFigure(paths, datainfo, point)
MA_Osaka_t.plt_moving_ave()

##vap
point = 'vap'
point_y = make_y_name(point)
datainfo = {
    "title": "大阪市" + str(point_y) + "移動平均足", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

MA_Osaka_v = PltMovingAveFigure(paths, datainfo, point)
MA_Osaka_v.plt_moving_ave()

##hum
point = 'hum'
point_y = make_y_name(point)
datainfo = {
    "title": "大阪市" + str(point_y) + "移動平均足", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

MA_Osaka_h = PltMovingAveFigure(paths, datainfo, point)
MA_Osaka_h.plt_moving_ave()

##atm
point = 'atm'
point_y = make_y_name(point)
datainfo = {
    "title": "大阪市" + str(point_y) + "移動平均足", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

MA_Osaka_a = PltMovingAveFigure(paths, datainfo, point)
MA_Osaka_a.plt_moving_ave()

##tp_max
point = 'tp_max'
point_y = make_y_name(point)
datainfo = {
    "title": "大阪市" + str(point_y) + "移動平均足", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

MA_Osaka_tma = PltMovingAveFigure(paths, datainfo, point)
MA_Osaka_tma.plt_moving_ave()

##tp_min
point = 'tp_min'
point_y = make_y_name(point)
datainfo = {
    "title": "大阪市" + str(point_y) + "移動平均足", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

MA_Osaka_tmi = PltMovingAveFigure(paths, datainfo, point)
MA_Osaka_tmi.plt_moving_ave()

##weather
point = 'weather'
point_y = make_y_name(point)
datainfo = {
    "title": "大阪市" + str(point_y) + "移動平均足", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

MA_Osaka_w = PltMovingAveFigure(paths, datainfo, point)
MA_Osaka_w.plt_moving_ave()

#===Naha============
base_path = r'data\weather\Okinawa'
paths = make_csv_path(base_path)
##temp
point = 'temp'
point_y = make_y_name(point)
datainfo = {
    "title": "那覇市" + str(point_y) + "移動平均足", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

MA_Okinawa_t = PltMovingAveFigure(paths, datainfo, point)
MA_Okinawa_t.plt_moving_ave()

##vap
point = 'vap'
point_y = make_y_name(point)
datainfo = {
    "title": "那覇市" + str(point_y) + "移動平均足", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

MA_Okinawa_v = PltMovingAveFigure(paths, datainfo, point)
MA_Okinawa_v.plt_moving_ave()

##hum
point = 'hum'
point_y = make_y_name(point)
datainfo = {
    "title": "那覇市" + str(point_y) + "移動平均足", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

MA_Okinawa_h = PltMovingAveFigure(paths, datainfo, point)
MA_Okinawa_h.plt_moving_ave()

##atm
point = 'atm'
point_y = make_y_name(point)
datainfo = {
    "title": "那覇市" + str(point_y) + "移動平均足", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

MA_Okinawa_a = PltMovingAveFigure(paths, datainfo, point)
MA_Okinawa_a.plt_moving_ave()

##tp_max
point = 'tp_max'
point_y = make_y_name(point)
datainfo = {
    "title": "那覇市" + str(point_y) + "移動平均足", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

MA_Okinawa_tma = PltMovingAveFigure(paths, datainfo, point)
MA_Okinawa_tma.plt_moving_ave()

##tp_min
point = 'tp_min'
point_y = make_y_name(point)
datainfo = {
    "title": "那覇市" + str(point_y) + "移動平均足", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

MA_Okinawa_tmi = PltMovingAveFigure(paths, datainfo, point)
MA_Okinawa_tmi.plt_moving_ave()

##weather
point = 'weather'
point_y = make_y_name(point)
datainfo = {
    "title": "那覇市" + str(point_y) + "移動平均足", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

MA_Okinawa_w = PltMovingAveFigure(paths, datainfo, point)
MA_Okinawa_w.plt_moving_ave()


#===Nagano==========
base_path = r'data\weather\agano'
paths = make_csv_path(base_path)
##temp
point = 'temp'
point_y = make_y_name(point)
datainfo = {
    "title": "長野市" + str(point_y) + "移動平均足", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

MA_Nagano_t = PltMovingAveFigure(paths, datainfo, point)
MA_Nagano_t.plt_moving_ave()

##vap
point = 'vap'
point_y = make_y_name(point)
datainfo = {
    "title": "長野市" + str(point_y) + "移動平均足", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

MA_Nagano_v = PltMovingAveFigure(paths, datainfo, point)
MA_Nagano_v.plt_moving_ave()

##hum
point = 'hum'
point_y = make_y_name(point)
datainfo = {
    "title": "長野市" + str(point_y) + "移動平均足", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

MA_Nagano_h = PltMovingAveFigure(paths, datainfo, point)
MA_Nagano_h.plt_moving_ave()

##atm
point = 'atm'
point_y = make_y_name(point)
datainfo = {
    "title": "長野市" + str(point_y) + "移動平均足", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

MA_Nagano_a = PltMovingAveFigure(paths, datainfo, point)
MA_Nagano_a.plt_moving_ave()

##tp_max
point = 'tp_max'
point_y = make_y_name(point)
datainfo = {
    "title": "長野市" + str(point_y) + "移動平均足", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

MA_Nagano_tma = PltMovingAveFigure(paths, datainfo, point)
MA_Nagano_tma.plt_moving_ave()

##tp_min
point = 'tp_min'
point_y = make_y_name(point)
datainfo = {
    "title": "長野市" + str(point_y) + "移動平均足", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

MA_Nagano_tmi = PltMovingAveFigure(paths, datainfo, point)
MA_Nagano_tmi.plt_moving_ave()

##weather
point = 'weather'
point_y = make_y_name(point)
datainfo = {
    "title": "長野市" + str(point_y) + "移動平均足", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

MA_Nagano_w = PltMovingAveFigure(paths, datainfo, point)
MA_Nagano_w.plt_moving_ave()


#===Fukuoka=========
base_path = r'data\weather\Fukuoka'
paths = make_csv_path(base_path)
##temp
point = 'temp'
point_y = make_y_name(point)
datainfo = {
    "title": "福岡市" + str(point_y) + "移動平均足", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

MA_Fukuoka_t = PltMovingAveFigure(paths, datainfo, point)
MA_Fukuoka_t.plt_moving_ave()

##vap
point = 'vap'
point_y = make_y_name(point)
datainfo = {
    "title": "福岡市" + str(point_y) + "移動平均足", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

MA_Fukuoka_v = PltMovingAveFigure(paths, datainfo, point)
MA_Fukuoka_v.plt_moving_ave()

##hum
point = 'hum'
point_y = make_y_name(point)
datainfo = {
    "title": "福岡市" + str(point_y) + "移動平均足", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

MA_Fukuoka_h = PltMovingAveFigure(paths, datainfo, point)
MA_Fukuoka_h.plt_moving_ave()
##atm
point = 'atm'
point_y = make_y_name(point)
datainfo = {
    "title": "福岡市" + str(point_y) + "移動平均足", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

MA_Fukuoka_a = PltMovingAveFigure(paths, datainfo, point)
MA_Fukuoka_a.plt_moving_ave()

##tp_max
point = 'tp_max'
point_y = make_y_name(point)
datainfo = {
    "title": "福岡市" + str(point_y) + "移動平均足", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

MA_Fukuoka_tma = PltMovingAveFigure(paths, datainfo, point)
MA_Fukuoka_tma.plt_moving_ave()

##tp_min
point = 'tp_min'
point_y = make_y_name(point)
datainfo = {
    "title": "福岡市" + str(point_y) + "移動平均足", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

MA_Fukuoka_tmi = PltMovingAveFigure(paths, datainfo, point)
MA_Fukuoka_tmi.plt_moving_ave()

##weather
point = 'weather'
point_y = make_y_name(point)
datainfo = {
    "title": "福岡市" + str(point_y) + "移動平均足", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

MA_Fukuoka_w = PltMovingAveFigure(paths, datainfo, point)
MA_Fukuoka_w.plt_moving_ave()