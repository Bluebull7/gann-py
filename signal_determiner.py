import numpy as np


class SignalDeterminer:
    def determine_signals(self, df):
        df['Signal'] = np.where(df['close'] > df['SMA_High'].shift(1),)
                                   