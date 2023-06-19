class BuyOrder:
    def __init__(self, amount, price, id):
        self.type = "buy"
        self.amount = amount
        self.price = price
        self.id = id

    def __repr__(self):
        return f"[{self.type},{self.amount},{self.price},{self.id}]"


class SellOrder:
    def __init__(self, amount, price, id):
        self.type = "sell"
        self.amount = amount
        self.price = price
        self.id = id

    def __repr__(self):
        return f"[{self.type},{self.amount},{self.price},{self.id}]"


class OrderClass:
    def __init__(self, orderList):
        self.orderList = orderList


orderClass = OrderClass([])
orderClass.orderList.append(BuyOrder(20, 1000, 1))
orderClass.orderList.append(SellOrder(50, 7000, 5))
orderClass.orderList.append(BuyOrder(30, 1000, 7))
print(orderClass.orderList)
