
class Orderitems:
    @classmethod
    def orderitems(cls,price,index):
        # if index == 0:
            quantity = int(input("Enter Quantity\n"))
            total_price = quantity * price
            print("price:", total_price)
            return total_price