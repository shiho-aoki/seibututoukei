import numpy as np
import pandas as pd

def MovingAverage(data, window=7):
    rolling = data.rolling(window).mean()
    return rolling