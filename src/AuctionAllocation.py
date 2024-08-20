import numpy as np

class AllocationMechanism:
    ''' Base class for allocation mechanisms '''
    def __init__(self):
        pass

    def allocate(self, bids, num_slots):
        pass


class FirstPrice(AllocationMechanism):
    ''' (Generalised) First-Price Allocation '''

    def __init__(self):
        super(FirstPrice, self).__init__()

    def allocate(self, bids, num_slots):
        winners = np.argsort(-bids)[:num_slots]
        sorted_bids = -np.sort(-bids)
        prices = sorted_bids[:num_slots]
        second_prices = sorted_bids[1:num_slots+1]
        return winners, prices, second_prices


class SecondPrice(AllocationMechanism):
    ''' (Generalised) Second-Price Allocation '''

    def __init__(self):
        super(SecondPrice, self).__init__()

    def allocate(self, bids, num_slots):
        winners = np.argsort(-bids)[:num_slots]
        prices = -np.sort(-bids)[1:num_slots+1]
        return winners, prices, prices

class FirstPriceReserve(AllocationMechanism):
    ''' (Generalised) First-Price Allocation with Reserve Price '''

    def __init__(self, reserve_price = 0):
        super(FirstPriceReserve, self).__init__()
        self.reserve_price = reserve_price

    def allocate(self, bids, num_slots):
        winners = np.argsort(-bids)[:num_slots]
        sorted_bids = -np.sort(-bids)
        prices = np.maximum(sorted_bids[:num_slots], self.reserve_price)
        second_prices = sorted_bids[1:num_slots+1]
        return winners, prices, second_prices

class SecondPriceReserve(AllocationMechanism):
    ''' (Generalised) Second-Price Allocation with Reserve Price '''

    def __init__(self, reserve_price = 0):
        super(SecondPriceReserve, self).__init__()
        self.reserve_price = reserve_price

    def allocate(self, bids, num_slots):
        winners = np.argsort(-bids)[:num_slots]
        sorted_bids = -np.sort(-bids)
        prices = np.maximum(sorted_bids[1:num_slots+1], self.reserve_price)
        return winners, prices, prices