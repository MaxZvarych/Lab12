import doctest

from models.Securities import Securities
from operator import itemgetter, attrgetter

from models.SortType import SortType


class SecuritiesManagerUtils:
    def __init__(self, list_of_securities=None):
        if list_of_securities is None:
            list_of_securities = [Securities(document_owner="Marko", price=400),
                                  Securities(document_owner="Evkakiy", price=300),
                                  Securities(document_owner="Olexa", price=450)]
        self.list_of_securities=list_of_securities
    def sort_by_price(self,sort_type=SortType.ascending):
        """
        >>> print(obj.sort_by_price())
        [Security [Document_owner:Evkakiy, price:300, trend_of_bidding:BiddingTrend.ascending, level_of_risk:RiskLevel.medium], Security [Document_owner:Marko, price:400, trend_of_bidding:BiddingTrend.ascending, level_of_risk:RiskLevel.medium], Security [Document_owner:Olexa, price:450, trend_of_bidding:BiddingTrend.ascending, level_of_risk:RiskLevel.medium]]
        """
        if sort_type==SortType.ascending:
            self.list_of_securities=sorted(self.list_of_securities, key=attrgetter('price'),reverse=False)

        else:
            self.list_of_securities=sorted(self.list_of_securities, key=attrgetter('price'),reverse=True)
        return self.list_of_securities
    def sort_by_document_owner(self,sort_type=SortType.ascending):
        """
        >>> print(obj.sort_by_document_owner())
        [Security [Document_owner:Evkakiy, price:300, trend_of_bidding:BiddingTrend.ascending, level_of_risk:RiskLevel.medium], Security [Document_owner:Marko, price:400, trend_of_bidding:BiddingTrend.ascending, level_of_risk:RiskLevel.medium], Security [Document_owner:Olexa, price:450, trend_of_bidding:BiddingTrend.ascending, level_of_risk:RiskLevel.medium]]
        """
        if sort_type==SortType.ascending:
            self.list_of_securities=sorted(self.list_of_securities, key=attrgetter('document_owner'),reverse=False)
        else:
            self.list_of_securities=sorted(self.list_of_securities, key=attrgetter('document_owner'),reverse=True)
        return self.list_of_securities
if __name__ == "__main__":
    doctest.testmod(verbose=True, extraglobs={'obj': SecuritiesManagerUtils()})
