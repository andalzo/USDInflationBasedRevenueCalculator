
class Backend:

    def __init__(self,
                prev_dolar_value : float,
                new_dolar_value : float,
                prev_stock_price : float,
                new_stock_price : float,
                prev_item_value : float,
                new_item_value : float,
                ):

        self.prev_dollar_value = prev_dolar_value
        self.new_dollar_value = new_dolar_value
        self.prev_stock_price = prev_stock_price
        self.new_stock_price = new_stock_price
        self.prev_item_value = prev_item_value
        self.new_item_value = new_item_value
        self.inflation_rate_regardings_to_dollar = float()
        self.profit_regardings_to_dollar = float()
        self.reel_profit = float()


    def calculate_inflation_rate_regardings_to_dollar(self):
        prev_item_value_dollar = self.prev_item_value/self.prev_dollar_value
        new_item_value_dollar = self.new_item_value/self.new_dollar_value
        self.inflation_rate_regardings_to_dollar = new_item_value_dollar/prev_item_value_dollar

    def calculate_profit_regardings_to_dollar(self):
        prev_stock_price_dollar = self.prev_stock_price/self.prev_dollar_value
        new_stock_price_dollar = self.new_stock_price/self.new_dollar_value
        self.profit_regardings_to_dollar = new_stock_price_dollar/prev_stock_price_dollar

    def calculate_reel_profit(self):
        self.reel_profit = self.profit_regardings_to_dollar*(1.0 - (self.inflation_rate_regardings_to_dollar - 1.0))