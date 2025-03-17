from AlgorithmImports import *

class FibonacciEmaStrategy(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2019, 1, 1)
        self.SetEndDate(2024, 1, 1)
        self.SetCash(100000)
        
        # Add SPY data
        self.spy = self.AddEquity("SPY", Resolution.Minute).Symbol
        
        # Define EMAs
        self.fast_ema = self.EMA(self.spy, 9, Resolution.Minute)
        self.slow_ema = self.EMA(self.spy, 21, Resolution.Minute)
        
        # Track positions
        self.entry_price = 0
        self.stop_loss = 0
        self.take_profit = 0
        self.trailing_stop = 0
        
        # Fibonacci Retracement Levels
        self.high_price = 0
        self.low_price = float('inf')
        self.fib_levels = {}

    def OnData(self, data):
        # Ensure SPY data exists and EMAs are ready
        if self.spy not in data or data[self.spy] is None or not (self.fast_ema.IsReady and self.slow_ema.IsReady):
            return
        
        price = data[self.spy].Close
        
        # Update high and low prices for Fibonacci
        self.high_price = max(self.high_price, price)
        self.low_price = min(self.low_price, price)
        self.CalculateFibLevels()

        # Buy Signal: EMA Crossover + Price Near Fibonacci Support
        if self.fast_ema.Current.Value > self.slow_ema.Current.Value and price > self.fib_levels[0.382]:
            if not self.Portfolio[self.spy].Invested:
                self.SetHoldings(self.spy, 1)
                self.entry_price = price
                self.stop_loss = price * 0.85  # 15% stop loss
                self.take_profit = price * 1.2  # 20% take profit
                self.trailing_stop = price * 1.05  # 5% trailing stop

        # Exit Logic
        if self.Portfolio[self.spy].Invested:
            if price <= self.stop_loss or price >= self.take_profit:
                self.Liquidate(self.spy)
            elif price <= self.trailing_stop and price > self.entry_price * 1.05:
                self.Liquidate(self.spy)
            else:
                self.trailing_stop = max(self.trailing_stop, price * 0.95)

    def CalculateFibLevels(self):
        """ Calculate Fibonacci retracement levels """
        diff = self.high_price - self.low_price
        self.fib_levels = {
            0.0: self.low_price,
            0.236: self.high_price - 0.236 * diff,
            0.382: self.high_price - 0.382 * diff,
            0.5: self.high_price - 0.5 * diff,
            0.618: self.high_price - 0.618 * diff,
            0.786: self.high_price - 0.786 * diff,
            1.0: self.high_price
        }
