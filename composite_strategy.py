class CompositeStrategy:

    def __init__(self, components):
        self.components = components


    def execute_strategy(self, exchange, symbol, timeframe, h_period, l_period, adx_period, trailing_stop_pips):
        df = None
        for component in self.components:
            df = component.execute(df, exchange, symbol, timeframe, h_period, l_period, adx_period, trailing_stop_pips)