import plt_moving_average as pltma
import plt_gause as plg

#===TOKYO==================
base_path = 'data\weather\Tokyo'
makepath = pltma.make_csv_path(base_path)
paths = makepath.main()
##temp
point = 'temp'
name = pltma.make_y_name(point)
point_y = name.main()

datainfo_TOKYO = {
    "title": "東京都" + str(point_y) + " ガウス過程回帰分析結果", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

GA_TOKYO = plg.PLTGause(paths, point, datainfo_TOKYO)
GA_TOKYO.plt_main()

##vap
points = 'vap'
point = 'vap_pressure'
name = pltma.make_y_name(points)
point_y = name.main()

datainfo_TOKYO = {
    "title": "東京都" + str(point_y) + " ガウス過程回帰分析結果", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

GA_TOKYO = plg.PLTGause(paths, point, datainfo_TOKYO)
GA_TOKYO.plt_main()

##hum
points = 'hum'
point = 'humidity'
name = pltma.make_y_name(points)
point_y = name.main()

datainfo_TOKYO = {
    "title": "東京都" + str(point_y) + " ガウス過程回帰分析結果", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

GA_TOKYO = plg.PLTGause(paths, point, datainfo_TOKYO)
GA_TOKYO.plt_main()
##atm
points = 'atm'
point = 'atm_pressure'
name = pltma.make_y_name(points)
point_y = name.main()

datainfo_TOKYO = {
    "title": "東京都" + str(point_y) + " ガウス過程回帰分析結果", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

GA_TOKYO = plg.PLTGause(paths, point, datainfo_TOKYO)
GA_TOKYO.plt_main()
##tpmax
points = 'tp_max'
point = 'temp_max'
name = pltma.make_y_name(points)
point_y = name.main()

datainfo_TOKYO = {
    "title": "東京都" + str(point_y) + " ガウス過程回帰分析結果", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

GA_TOKYO = plg.PLTGause(paths, point, datainfo_TOKYO)
GA_TOKYO.plt_main()
##tpmin
points = 'tp_min'
point = 'temp_min'
name = pltma.make_y_name(points)
point_y = name.main()

datainfo_TOKYO = {
    "title": "東京都" + str(point_y) + " ガウス過程回帰分析結果", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

GA_TOKYO = plg.PLTGause(paths, point, datainfo_TOKYO)
GA_TOKYO.plt_main()
##weather
points = 'weather'
point = 'weather_num'
name = pltma.make_y_name(points)
point_y = name.main()

datainfo_TOKYO = {
    "title": "東京都" + str(point_y) + " ガウス過程回帰分析結果", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

GA_TOKYO = plg.PLTGause(paths, point, datainfo_TOKYO)
GA_TOKYO.plt_main()

#===Sappro===================
base_path = 'data\weather\Sapporo'
makepath = pltma.make_csv_path(base_path)
paths = makepath.main()
##temp
point = 'temp'
name = pltma.make_y_name(point)
point_y = name.main()

datainfo = {
    "title": "札幌市" + str(point_y) + " ガウス過程回帰分析結果", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

GA = plg.PLTGause(paths, point, datainfo)
GA.plt_main()
##vap
points = 'vap'
point = 'vap_pressure'
name = pltma.make_y_name(points)
point_y = name.main()

datainfo = {
    "title": "札幌市" + str(point_y) + " ガウス過程回帰分析結果", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

GA = plg.PLTGause(paths, point, datainfo)
GA.plt_main()
##hum
points = 'hum'
point = 'humidity'
name = pltma.make_y_name(points)
point_y = name.main()

datainfo = {
    "title": "札幌市" + str(point_y) + " ガウス過程回帰分析結果", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

GA = plg.PLTGause(paths, point, datainfo)
GA.plt_main()
##atm
points = 'atm'
point = 'atm_pressure'
name = pltma.make_y_name(points)
point_y = name.main()

datainfo = {
    "title": "札幌市" + str(point_y) + " ガウス過程回帰分析結果", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

GA = plg.PLTGause(paths, point, datainfo)
GA.plt_main()
##tpmax
points = 'tp_max'
point = 'temp_max'
name = pltma.make_y_name(points)
point_y = name.main()

datainfo = {
    "title": "札幌市" + str(point_y) + " ガウス過程回帰分析結果", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

GA = plg.PLTGause(paths, point, datainfo)
GA.plt_main()
##tpmin
points = 'tp_min'
point = 'temp_min'
name = pltma.make_y_name(points)
point_y = name.main()

datainfo = {
    "title": "札幌市" + str(point_y) + " ガウス過程回帰分析結果", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

GA = plg.PLTGause(paths, point, datainfo)
GA.plt_main()
##weather
points = 'weather'
point = 'weather_num'
name = pltma.make_y_name(points)
point_y = name.main()

datainfo = {
    "title": "札幌市" + str(point_y) + " ガウス過程回帰分析結果", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

GA = plg.PLTGause(paths, point, datainfo)
GA.plt_main()

#===Osaka=========================
base_path = 'data\weather\Osaka'
makepath = pltma.make_csv_path(base_path)
paths = makepath.main()

##temp
point = 'temp'
name = pltma.make_y_name(point)
point_y = name.main()

datainfo = {
    "title": "大阪市" + str(point_y) + " ガウス過程回帰分析結果", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

GA = plg.PLTGause(paths, point, datainfo)
GA.plt_main()
##vap
points = 'vap'
point = 'vap_pressure'
name = pltma.make_y_name(points)
point_y = name.main()

datainfo = {
    "title": "大阪市" + str(point_y) + " ガウス過程回帰分析結果", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

GA = plg.PLTGause(paths, point, datainfo)
GA.plt_main()
##hum
points = 'hum'
point = 'humidity'
name = pltma.make_y_name(points)
point_y = name.main()

datainfo = {
    "title": "大阪市" + str(point_y) + " ガウス過程回帰分析結果", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

GA = plg.PLTGause(paths, point, datainfo)
GA.plt_main()
##atm
points = 'atm'
point = 'atm_pressure'
name = pltma.make_y_name(points)
point_y = name.main()

datainfo = {
    "title": "大阪市" + str(point_y) + " ガウス過程回帰分析結果", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

GA = plg.PLTGause(paths, point, datainfo)
GA.plt_main()
##tpmax
points = 'tp_max'
point = 'temp_max'
name = pltma.make_y_name(points)
point_y = name.main()

datainfo = {
    "title": "大阪市" + str(point_y) + " ガウス過程回帰分析結果", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

GA = plg.PLTGause(paths, point, datainfo)
GA.plt_main()
##tpmin
points = 'tp_min'
point = 'temp_min'
name = pltma.make_y_name(points)
point_y = name.main()

datainfo = {
    "title": "大阪市" + str(point_y) + " ガウス過程回帰分析結果", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

GA = plg.PLTGause(paths, point, datainfo)
GA.plt_main()
##weather
points = 'weather'
point = 'weather_num'
name = pltma.make_y_name(points)
point_y = name.main()
datainfo = {
    "title": "大阪市" + str(point_y) + " ガウス過程回帰分析結果", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

GA = plg.PLTGause(paths, point, datainfo)
GA.plt_main()

#===Naha==========================
base_path = 'data\weather\Okinawa'
makepath = pltma.make_csv_path(base_path)
paths = makepath.main()
##temp
point = 'temp'
name = pltma.make_y_name(point)
point_y = name.main()

datainfo = {
    "title": "那覇市" + str(point_y) + " ガウス過程回帰分析結果", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

GA = plg.PLTGause(paths, point, datainfo)
GA.plt_main()
##vap
points = 'vap'
point = 'vap_pressure'
name = pltma.make_y_name(points)
point_y = name.main()

datainfo = {
    "title": "那覇市" + str(point_y) + " ガウス過程回帰分析結果", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

GA = plg.PLTGause(paths, point, datainfo)
GA.plt_main()
##hum
points = 'hum'
point = 'humidity'
name = pltma.make_y_name(points)
point_y = name.main()

datainfo = {
    "title": "那覇市" + str(point_y) + " ガウス過程回帰分析結果", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

GA = plg.PLTGause(paths, point, datainfo)
GA.plt_main()
##atm
points = 'atm'
point = 'atm_pressure'
name = pltma.make_y_name(points)
point_y = name.main()

datainfo = {
    "title": "那覇市" + str(point_y) + " ガウス過程回帰分析結果", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

GA = plg.PLTGause(paths, point, datainfo)
GA.plt_main()
##tpmax
points = 'tp_max'
point = 'temp_max'
name = pltma.make_y_name(points)
point_y = name.main()

datainfo = {
    "title": "那覇市" + str(point_y) + " ガウス過程回帰分析結果", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

GA = plg.PLTGause(paths, point, datainfo)
GA.plt_main()
##tpmin
points = 'tp_min'
point = 'temp_min'
name = pltma.make_y_name(points)
point_y = name.main()

datainfo = {
    "title": "那覇市" + str(point_y) + " ガウス過程回帰分析結果", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

GA = plg.PLTGause(paths, point, datainfo)
GA.plt_main()
##weather
points = 'weather'
point = 'weather_num'
name = pltma.make_y_name(points)
point_y = name.main()

datainfo = {
    "title": "那覇市" + str(point_y) + " ガウス過程回帰分析結果", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

GA = plg.PLTGause(paths, point, datainfo)
GA.plt_main()
#===Nagano=========================
base_path = r'data\weather\agano'
makepath = pltma.make_csv_path(base_path)
paths = makepath.main()

##temp
point = 'temp'
name = pltma.make_y_name(point)
point_y = name.main()

datainfo = {
    "title": "長野市" + str(point_y) + " ガウス過程回帰分析結果", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

GA = plg.PLTGause(paths, point, datainfo)
GA.plt_main()
##vap
points = 'vap'
point = 'vap_pressure'
name = pltma.make_y_name(points)
point_y = name.main()

datainfo = {
    "title": "長野市" + str(point_y) + " ガウス過程回帰分析結果", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

GA = plg.PLTGause(paths, point, datainfo)
GA.plt_main()
##hum
points = 'hum'
point = 'humidity'
name = pltma.make_y_name(points)
point_y = name.main()

datainfo = {
    "title": "長野市" + str(point_y) + " ガウス過程回帰分析結果", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

GA = plg.PLTGause(paths, point, datainfo)
GA.plt_main()
##atm
points = 'atm'
point = 'atm_pressure'
name = pltma.make_y_name(points)
point_y = name.main()

datainfo = {
    "title": "長野市" + str(point_y) + " ガウス過程回帰分析結果", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

GA = plg.PLTGause(paths, point, datainfo)
GA.plt_main()
##tpmax
points = 'tp_max'
point = 'temp_max'
name = pltma.make_y_name(points)
point_y = name.main()

datainfo = {
    "title": "長野市" + str(point_y) + " ガウス過程回帰分析結果", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

GA = plg.PLTGause(paths, point, datainfo)
GA.plt_main()
##tpmin
points = 'tp_min'
point = 'temp_min'
name = pltma.make_y_name(points)
point_y = name.main()

datainfo = {
    "title": "長野市" + str(point_y) + " ガウス過程回帰分析結果", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

GA = plg.PLTGause(paths, point, datainfo)
GA.plt_main()
##weather
points = 'weather'
point = 'weather_num'
name = pltma.make_y_name(points)
point_y = name.main()

datainfo = {
    "title": "長野市" + str(point_y) + " ガウス過程回帰分析結果", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

GA = plg.PLTGause(paths, point, datainfo)
GA.plt_main()

#===Fukuoka========================
base_path = 'data\weather\Fukuoka'
makepath = pltma.make_csv_path(base_path)
paths = makepath.main()
##temp
point = 'temp'
name = pltma.make_y_name(point)
point_y = name.main()

datainfo = {
    "title": "福岡市" + str(point_y) + " ガウス過程回帰分析結果", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

GA = plg.PLTGause(paths, point, datainfo)
GA.plt_main()
##vap
points = 'vap'
point = 'vap_pressure'
name = pltma.make_y_name(points)
point_y = name.main()
datainfo = {
    "title": "福岡市" + str(point_y) + " ガウス過程回帰分析結果", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

GA = plg.PLTGause(paths, point, datainfo)
GA.plt_main()
##hum
points = 'hum'
point = 'humidity'
name = pltma.make_y_name(points)
point_y = name.main()
datainfo = {
    "title": "福岡市" + str(point_y) + " ガウス過程回帰分析結果", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

GA = plg.PLTGause(paths, point, datainfo)
GA.plt_main()
##atm
points = 'atm'
point = 'atm_pressure'
name = pltma.make_y_name(points)
point_y = name.main()
datainfo = {
    "title": "福岡市" + str(point_y) + " ガウス過程回帰分析結果", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

GA = plg.PLTGause(paths, point, datainfo)
GA.plt_main()
##tpmax
points = 'tp_max'
point = 'temp_max'
name = pltma.make_y_name(points)
point_y = name.main()
datainfo = {
    "title": "福岡市" + str(point_y) + " ガウス過程回帰分析結果", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

GA = plg.PLTGause(paths, point, datainfo)
GA.plt_main()
##tpmin
points = 'tp_min'
point = 'temp_min'
name = pltma.make_y_name(points)
point_y = name.main()
datainfo = {
    "title": "福岡市" + str(point_y) + " ガウス過程回帰分析結果", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

GA = plg.PLTGause(paths, point, datainfo)
GA.plt_main()
##weather
points = 'weather'
point = 'weather_num'
name = pltma.make_y_name(points)
point_y = name.main()
datainfo = {
    "title": "福岡市" + str(point_y) + " ガウス過程回帰分析結果", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }

GA = plg.PLTGause(paths, point, datainfo)
GA.plt_main()