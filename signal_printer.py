# signal printer

class SignalPrinter:

    def print_signals(self, df):
        print(df[['close', 'SMA_High', 'SMA_Low', 'ADX', 'BuySignal', 'SellSignal']])