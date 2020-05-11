from models.Securities import Securities
from models.BiddingTrend import BiddingTrend
from models.RiskLevel import RiskLevel

class Bills(Securities):
    def __init__(self, document_owner="Volodya", price=250, level_of_risk=RiskLevel.medium, \
                 trend_of_bidding=BiddingTrend.ascending, deposit_amount=10000,amount_of_interest_on_deposit=7.25):
        Securities.__init__(self, document_owner, price, level_of_risk, trend_of_bidding)
        self.deposit_amount=deposit_amount
        self.amount_of_interest_on_deposit = amount_of_interest_on_deposit

    def __del__(self):
        print("Видалення екземпляра:" + self.__str__())
