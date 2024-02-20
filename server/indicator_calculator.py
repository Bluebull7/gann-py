import ta 

class IndicatorCalculator:
    def calculate_indicators(self, df, h_period, l_period, adx_period, trailing_stop_pips):
        df['ADX'] = ta.adx(df['high'], df['low'], df['close'], adx_period)
        df['SMA_High'] = ta.sma(df['high'], h_period)
        df['SMA_Low'] = ta.sma(df['low'], l_period)
        df['TrailingStop'] = df['SMA_High'] - trailing_stop_pips * 0.000001
        return df
