
class ViewItems :
    @classmethod
    def itemschoice(cls):
        print("\n")
        print("1 for vegitables")
        print("2 for grocery")
        print("3 for fruits")
        print("\n")
        user_choice = int(input("Enter Your Choice\n"))
        return user_choice


    @staticmethod
    def vegitems():
        print("1 for Carrot")
        print("2 for Potato")
        print("3 for Ladies finger")

    @staticmethod
    def groitems():
        print("1 for Rice")
        print("2 for Dhal")
        print("3 for Oil")

    @staticmethod
    def fruititems():
        print("1 for Apple")
        print("2 for Orange")
        print("3 for Pomogranade")

    @staticmethod
    def vegsection():
        print("  " * 15 + "Veg Section" + "  " * 15)

    @staticmethod
    def grocerysection():
        print("  " * 15 + "Grocery Section" + "  " * 15)

    @staticmethod
    def fruitsection():
        print("  " * 15 + "Fruit Section" + "  " * 15)

    @classmethod
    def itemdetails(cls,result,index):
        print(result[index][0], '\t\t\t\t', result[index][1], "per Kg")


