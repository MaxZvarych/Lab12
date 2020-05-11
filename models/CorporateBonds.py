from models.Securities import Securities
from models.BiddingTrend import BiddingTrend
from models.RiskLevel import RiskLevel


class Corporate_bonds(Securities):
    def __init__(self, document_owner="Volodya", price=250, level_of_risk=RiskLevel.medium, \
                 trend_of_bidding=BiddingTrend.ascending,services = "Different" ):
        Securities.__init__(self,document_owner,price,level_of_risk,trend_of_bidding)
        self.services=services

    def __del__(self):
        print("Видалення екземпляра:" + self.__str__())
