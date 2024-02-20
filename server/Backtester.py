import pandas as pd 
import numpy as np 
import composite_strategy, data_fetcher, indicator_calculator
import signal_determiner, signal_printer
class Backtester:
    def __init__(self, strategy):
        strategy = signal_determiner()
        self.strategy = strategy

    def run_backtest(self, historical_data):
       
        # create a copy of the data to avoid modifying the original
        df = pd.DataFrame(historical_data.copy(),columns=['timestamp', 'open', 'high','low', 'close', 'volume'])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit ='ms')
        df.set_index('timestamp', inplace=True)

        # calculate indicators using the trading strategy
        df = self.strategy.indicator_calculator(df)

        # apply the trading strategy to determine signals
        df = self.strategy.signal_determiner(df)

        # simulate trading based on signals
        self.simulate_trading(df)


    def simulate_trading(self, df):
        # <TODO> implement me
        pass

if __name__ == "__main__":

    # <TODO> implement me, override deprecated main 
    pass