from models.Securities import Securities
from models.BiddingTrend import BiddingTrend
from models.RiskLevel import RiskLevel

class Bills(Securities):
    def __init__(self, document_owner="Volodya", price=250, level_of_risk=RiskLevel.medium, \
                 trend_of_bidding=BiddingTrend.ascending, term="Up to 2030 year"):
        Securities.__init__(self, document_owner, price, level_of_risk, trend_of_bidding)
        self.term = term

    def __del__(self):
        print("Видалення екземпляра:" + self.__str__())
