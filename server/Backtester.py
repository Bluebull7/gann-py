import pandas as pd 
import numpy as np 

class Backtester:
    
    def __init__(self, data, h_period, l_period, adx_period, trailing_stop_pips):
        
        self.data = data
        self.h_period = h_period
        self.l_period = l_period
        self.adx_period = adx_period
        self.trailing_stop_pips = trailing_stop_pips
        self.equity_curve = []


        def run_backtest(self):
            signals = self.generate_signals()
            self.calculate_equity_curve(signals)

        def generate_signals
