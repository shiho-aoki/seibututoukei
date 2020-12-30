#python threed party library
import numpy as np
import pandas as pd

#calucrate a value of moving average
def MovingAverage(data, window=7):
    rolling = data.rolling(window).mean()
    return rolling