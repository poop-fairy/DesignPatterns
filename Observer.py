'''
Challange:
I have a stock ticker that should always be in sync with the stock prices in the database.
Use the Observer design pattern to achieve the result
'''

from abc import ABC,abstractmethod

class IObservable(ABC):
    
    @abstractmethod
    def subscribe(self, Observer):
        #Add a list of Observers that will be notified when an Observable event gets updated here
        pass

    @abstractmethod
    def unsubscribe(self, Observer):
        pass
    
    @abstractmethod
    def update(self, Observer):
        #Call Observer's update method
        pass

class IObserver(ABC):
    
    @abstractmethod
    def update(self, stock_name, stock_price):
        #method of observation
        pass

class StockMarket(IObservable):

    _observe = []
    dict_of_tracked_stocks = {'AAPL':189.24,
                              'MFST':378.61,
                              'META':334.70}

    def subscribe(self,Observer):
        if Observer in self._observe:
            return
        self._observe.append(Observer)
    
    def unsubscribe(self,Observer):
        if Observer in self._observe:
            self._observe.remove(Observer)
            return
        Exception('The Stock is not present in the subscription list')
    
    def update(self,stock,new_price):
        for obs in self._observe:
            obs.update(stock,new_price)
            
    def updateStockPrice(self,stock,new_price):
        self.dict_of_tracked_stocks[stock] = new_price
        self.update(stock,new_price)

class UserSideTicker(IObserver):

    def __init__(self,name):
        self.name = name

    def update(self,stock,price):
            print(('Update for {dashboard}- ').format(dashboard=self.name),stock,':',price,'\n')

stock_prices = StockMarket()
stock_dashboard_1 = UserSideTicker('Dashboard 1')
stock_dashboard_2 = UserSideTicker('Dashboard 2')
stock_dashboard_3 = UserSideTicker('Dashboard 3')

# stock_prices.subscribe(stock_dashboard_1)
# stock_prices.subscribe(stock_dashboard_2)
stock_prices.unsubscribe(stock_dashboard_3)

# stock_prices.updateStockPrice('AAPL',188.43)