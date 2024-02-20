import numpy as np


class SignalDeterminer:
    def determine_signals(self, df):
        df['Signal'] = np.where(df['close'] > df['SMA_High'].shift(1), 1,np.where(df['close'], df['SMA_Low'].shift(1), -1, 0))
        df['BullishCondition'] = (df['close'] > df['SMA_High'].shift(1)) & (df['ADX'] > 50)
        df['BearishCondition'] = (df['close'] < df['SMA_Low'].shift(1)) &  (df['ADX'] > 50)
        df['BuySignal'] = np.where((df['Signal'] == 1) & df['BullishCondition'], 1, 0)
        df['SellSignal'] = np.where((df)['Signal'] == -1 | (df['close'] < df['TrailingStop']) , -1, 0)

        return df
