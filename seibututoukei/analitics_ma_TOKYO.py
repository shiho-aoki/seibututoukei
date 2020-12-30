import plt_moving_average as pltma

base_path = 'data\weather\Tokyo'
makepath = pltma.make_csv_path(base_path)
paths = makepath.main()

point = 'temp'
name = pltma.make_y_name(point)
point_y = name.main()
datainfo_TOKYO = {
    "title": "東京都" + str(point_y) + "移動平均足", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }
MA_Tokyo_t = pltma.PltMovingAveFigure(paths, datainfo_TOKYO, point)
MA_Tokyo_t.plt_moving_ave()

point = 'vap'
name = pltma.make_y_name(point)
point_y = name.main()
datainfo_TOKYO = {
    "title": "東京都" + str(point_y) + "移動平均足", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }
MA_Tokyo_v = pltma.PltMovingAveFigure(paths, datainfo_TOKYO, point)
MA_Tokyo_v.plt_moving_ave()

point = 'hum'
name = pltma.make_y_name(point)
point_y = name.main()
datainfo_TOKYO = {
    "title": "東京都" + str(point_y) + "移動平均足", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }
MA_Tokyo_v = pltma.PltMovingAveFigure(paths, datainfo_TOKYO, point)
MA_Tokyo_v.plt_moving_ave()

point = 'atm'
name = pltma.make_y_name(point)
point_y = name.main()
datainfo_TOKYO = {
    "title": "東京都" + str(point_y) + "移動平均足", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }
MA_Tokyo_v = pltma.PltMovingAveFigure(paths, datainfo_TOKYO, point)
MA_Tokyo_v.plt_moving_ave()

point = 'tp_max'
name = pltma.make_y_name(point)
point_y = name.main()
datainfo_TOKYO = {
    "title": "東京都" + str(point_y) + "移動平均足", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }
MA_Tokyo_v = pltma.PltMovingAveFigure(paths, datainfo_TOKYO, point)
MA_Tokyo_v.plt_moving_ave()

point = 'tp_min'
name = pltma.make_y_name(point)
point_y = name.main()
datainfo_TOKYO = {
    "title": "東京都" + str(point_y) + "移動平均足", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }
MA_Tokyo_v = pltma.PltMovingAveFigure(paths, datainfo_TOKYO, point)
MA_Tokyo_v.plt_moving_ave()

point = 'weather'
name = pltma.make_y_name(point)
point_y = name.main()
datainfo_TOKYO = {
    "title": "東京都" + str(point_y) + "移動平均足", 
    "x_name": "時間（day）",
    "y_name": str(point_y), 
    "label": ["1990年","1995年","2000年","2005年","2010年"]
    }
MA_Tokyo_v = pltma.PltMovingAveFigure(paths, datainfo_TOKYO, point)
MA_Tokyo_v.plt_moving_ave()