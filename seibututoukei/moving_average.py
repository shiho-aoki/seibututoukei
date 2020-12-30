#python threed party library
import numpy as np
import pandas as pd

#calucrate a value of moving average
class MovingAverage:
    def __init__(self, data, window=7):
        self.data = data
        self.window = window
    
    def main(self):
        rolling = self.data.rolling(self.window).mean()
        return rolling