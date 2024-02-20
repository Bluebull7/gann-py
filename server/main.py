import ccxt
from data_fetcher import DataFetcher
from indicator_calculator import IndicatorCalculator
from signal_determiner import SignalDeterminer
from signal_printer import SignalPrinter
from composite_strategy import CompositeStrategy


if __name__ == "__main__":
    exchange = ccxt.binance()
    symbol = 'BTC/USDT'
    timeframe = '1h'
    HPeriod = 13
    LPeriod = 21
    ADXPeriod = 14
    trailing_stop_pips = 10

    data_fetcher = DataFetcher()
    indicator_calculator = IndicatorCalculator()
    signal_determiner = SignalDeterminer()
    signal_printer = SignalPrinter()

    composite_strategy = CompositeStrategy([data_fetcher, indicator_calculator, signal_determiner, signal_printer])

    composite_strategy.execute_strategy(exchange, symbol, timeframe, HPeriod, LPeriod, ADXPeriod, trailing_stop_pips)
    
