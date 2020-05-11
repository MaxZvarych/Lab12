import doctest

from models.BiddingTrend import BiddingTrend
from models.RiskLevel import RiskLevel
from models.Securities import Securities


class SecuritiesManager:
    def __init__(self, list_of_securities=None):
        if list_of_securities is None:
            list_of_securities = [Securities(document_owner="Marko", price=400),
                                  Securities(document_owner="Evkakiy", price=300),
                                  Securities(document_owner="Olexa", price=450)]
        self.list_of_securities=list_of_securities
    def search_by_price(self, price):
        """
        >>> print(obj.search_by_price(300))
        Security:Document_owner:Evkakiy, price:300, trend_of_bidding:BiddingTrend.ascending, level_of_risk:RiskLevel.medium
        """
        result="Nothing found"
        for x in self.list_of_securities:
            if x.price==price:
                result=x
        return result

    def search_by_trend_of_bidding(self, trend_of_bidding):
        """
        >>> print(obj.search_by_trend_of_bidding(BiddingTrend.ascending))
        Security:Document_owner:Olexa, price:450, trend_of_bidding:BiddingTrend.ascending, level_of_risk:RiskLevel.medium
        """
        result="Nothing found"
        for x in self.list_of_securities:
            if x.trend_of_bidding==trend_of_bidding:
                result=x
        return result

    def search_by_level_of_risk(self, level_of_risk):
        """
        >>> print(obj.search_by_level_of_risk(RiskLevel.medium))
        Security:Document_owner:Olexa, price:450, trend_of_bidding:BiddingTrend.ascending, level_of_risk:RiskLevel.medium
        """
        result = "Nothing found"
        for x in self.list_of_securities:
            if x.level_of_risk == level_of_risk:
                result = x
        return result

if __name__ == '__main__':
    doctest.testmod(verbose=True, extraglobs={'obj': SecuritiesManager()})

