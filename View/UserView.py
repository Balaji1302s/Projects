class UserView:

    @staticmethod
    def greetings():
        print("-" * 100)
        print(" " * 30 + "Welcome Online Grocery store")
        print("-" * 100)

    @classmethod
    def user_choice(cls):
        print("Enter 1 for New Registration")
        print("Enter 2 for Login")
        choice = int(input("Enter Your Choice:\t"))
        return choice

    @staticmethod
    def signup():
        print("_" * 100)
        print("-" * 40, "Sign-Up Module", "-" * 40)
        print("_" * 100)

    @staticmethod
    def login():
        print("\n")
        print("-" * 100)
        print("*" * 40, "Login Module", "*" * 40)
        print("-" * 100)
        print("\n")

    @staticmethod
    def isnotvalid():
        print("you have entered a Invalid user Details please try with valid one:)")

    @staticmethod
    def isnotvalidkey():
        print("Invalid key please try again:)")

    @staticmethod
    def loginmessage():
        print("\n")
        print("-" * 100)
        print(" " * 10 + "*" * 20 + "Hi you are loggen in successfully" + "*" * 20 + " " * 10)
        print("-" * 100)
        print("\n")
        # --------------------------------------------------------
        # --------------------------------------------------------

    @staticmethod
    def useractions():
        print("1 for view items")
        print("2 for view profile")
        print("Press any number key to goto login page")

    @classmethod
    def viewuser(cls, result):
        print("Name       :     " + result[0])
        print("phone N.O. :     " + result[2])
        print("E-mail     :     " + result[3])
        print("\n")
