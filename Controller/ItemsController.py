from Model.DatabaseConnectivity import connection,global_cursor
from View.ItemsView import ViewItems
from Model.Items import Itemlists
from Model.OrderItems import Orderitems
from View.Payments import Payments


class Viewitems:
    @classmethod
    def viewitems(cls):
        max_amt: int = 0
        bill_list = []
        index1: int = 0
        flag = True
        while flag:
            user_choice = ViewItems.itemschoice()

            if user_choice == 1:
                ViewItems.vegsection()
                result = Itemlists.vegitems()
                ViewItems.vegitems()
                index = Itemlists.userselection()
                ViewItems.itemdetails(result,index)
                total_price = Orderitems.orderitems(result[index][1], 0)
                bill_list.append(result[index][0])
                bill_list.append(total_price)
                max_amt += total_price



            elif user_choice == 2:
                ViewItems.grocerysection()
                result = Itemlists.groceryitems()
                print(result[0])
                ViewItems.groitems()
                index = Itemlists.userselection()
                print(index)
                ViewItems.itemdetails(result,index)
                total_price = Orderitems.orderitems(result[index][1], 1)
                bill_list.append(result[index][0])
                bill_list.append(total_price)
                max_amt += total_price

            elif user_choice == 3:
                ViewItems.fruitsection()
                result = Itemlists.fruititems()
                ViewItems.fruititems()
                index = Itemlists.userselection()
                ViewItems.itemdetails(result,index)
                total_price = Orderitems.orderitems(result[index][1], 2)
                bill_list.append(result[index][0])
                bill_list.append(total_price)
                max_amt += total_price

            print("Do you want more to order?\t\t 1.Continue\t\t2.Goto Payments")
            user_option = int(input("Enter your Choice: "))
            if user_option == 1:
                flag = True
            elif user_option == 2:
                for i in bill_list:
                    print(i)
                print("Your Total Amount Is :")
                print(max_amt)
                Payments().paymentchoice()
                flag = False