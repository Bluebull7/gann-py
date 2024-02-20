import pandas as pd 
import numpy as np 
import composite_strategy, data_fetcher, indicator_calculator
import signal_determiner, signal_printer
class Backtester:
    def __init__(self, data_fetcher, indicator_calculator, signal_determiner, signal_printer):
        strategy = signal_determiner.determine_signals()
        data = 
        self.strategy = strategy


    def run_backtest(self, historical_data):
       
        # create a copy of the data to avoid modifying the original
        historical_data = data_fetcher()
        df = pd.DataFrame(historical_data.copy(),columns=['timestamp', 'open', 'high','low', 'close', 'volume'])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit ='ms')
        df.set_index('timestamp', inplace=True)

        # calculate indicators using the trading strategy
        df = self.indicator_calculator(df)

        # apply the trading strategy to determine signals
        df = self.strategy.signal_determiner.determine_signals(df)

        # simulate trading based on signals
        self.simulate_trading(df)


    def simulate_trading(self, df):
        equity_curve = [1.0]

        # buy = 1 , sell = -1
        for i in range(1, len(df)):
            # simulate decisions based on signals from SD
            signal = df['Signal'].iloc[i]
            if signal == 1:
                equity_curve.append(equity_curve[-1] * (1 + df['close'].pct_change().iloc[i]))
            elif signal == -1
                equity_curve.append(equity_curve[-1] * (1 - df['close'].pct_change().iloc[i]))
            else:
                equity_curve.append(equity_curve[-1])
        df['EquityCurve'] = equity_curve
        print(df[['close', 'SMA_High', 'SMA_Low', 'ADX', 'BuySignal', 'SellSignal', 'EquityCurve']])
    pass

if __name__ == "__main__":

    # <TODO> implement me, override deprecated main 
    pass