from models.BiddingTrend import BiddingTrend
from models.RiskLevel import RiskLevel


class Securities:
    def __init__(self, document_owner="Volodya", price=250, level_of_risk=RiskLevel.medium, \
                 trend_of_bidding=BiddingTrend.ascending ):
        self.document_owner=document_owner
        self.price=price
        self.trend_of_bidding=trend_of_bidding
        self.level_of_risk=level_of_risk
    def __del__(self):
        print("Видалення екземпляра:"+ self.__str__())
        del self.document_owner
        del self.price
        del self.trend_of_bidding
        del self.level_of_risk
    def __str__(self):
        return "Security:" + "Document_owner:" + \
            self.document_owner + ", price:" + str(self.price) \
            + ", trend_of_bidding:" + str(self.trend_of_bidding) + ", level_of_risk:" + str(
            self.level_of_risk)

    def __repr__(self):
        return "Security [Document_owner:" + \
            self.document_owner + ", price:" + str(self.price) \
            + ", trend_of_bidding:" + str(self.trend_of_bidding) + ", level_of_risk:" + str(
            self.level_of_risk) + "]"
