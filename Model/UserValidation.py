import re
from View.UserView import UserView
from Controller.ItemsController import Viewitems
from Model.DatabaseConnectivity import global_cursor, connection


class New_Registration:
    user_name: str = ''
    user_password: str = ''
    user_phonenumber: int = 0
    user_emailId: str = ''

    @classmethod
    def new_user(cls):

        flag = True
        while flag:
            cls.user_name = input("Enter your Name\n")
            regex = "(?=.*[a-z])(?=.*[A-Z]).+$"
            constraint = re.compile(regex)
            if re.search(constraint, cls.user_name):
                flag = False
            else:
                UserView.isnotvalid()

        flag = True
        while flag:
            cls.user_password = input("Enter your Password\n")
            regex = ("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?& ])[A-Za-z\d@$!#%*?&]{8,18}$")
            constraint = re.compile(regex)
            if re.search(constraint, cls.user_password):
                flag = False
            else:
                UserView.isnotvalid()

        flag = True
        while flag:
            try:
                cls.user_phonenumber = int(input("Enter your Mobile number\n"))
            except:
                UserView.isnotvalid()
            else:
                if 6000000000 < cls.user_phonenumber < 10000000000 and cls.user_phonenumber != 6666666666 and cls.user_phonenumber != 7777777777 and cls.user_phonenumber != 8888888888 and cls.user_phonenumber != 9999999999:
                    flag = False
        flag = True
        while flag:
            cls.user_emailId = input("Enter your Email address:")
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
            match = re.compile(regex)
            if re.search(match, cls.user_emailId):
                flag = False
            else:
                UserView.isnotvalid()
        query = "insert into user_details values(%s,%s,%s,%s);"
        global_cursor.execute(query, (cls.user_name, cls.user_password, str(cls.user_phonenumber), cls.user_emailId))
        connection.commit()
        print("\n", "-" * 25, ">Successfully registered as the User<", "-" * 25)


class Login(New_Registration):
    __user_name = ""
    __password = ""

    @classmethod
    def login(cls):
        UserView.login()
        flag1 = True
        while flag1:
            __user_name = input("Enter your Name:      ")
            __password = input("Enter your Password:  ")
            query = "Select * from user_details where user_name=%s;"
            global_cursor.execute(query, (__user_name,))
            result = global_cursor.fetchone()
            try:
                if __password == result[1]:
                    UserView.loginmessage()
                    flag = True
                    while flag:
                        try:
                            UserView.useractions()
                            choice = int(input("Enter your choice\t"))
                        except:
                            UserView.isnotvalidkey()
                        else:
                            if choice == 1:
                                Viewitems().viewitems()

                            elif choice == 2:
                                UserView.viewuser(result)
                                flag = True
                            else:
                                flag = False
                else:
                    UserView.isnotvalid()
            except:
                UserView.isnotvalidkey()
            print("\t\t\t1.for continue login\t\t\t\t\t2.for return to home screen")
            flag2 = True
            while flag2:
                try:
                    choice = int(input("Enter your choice\t"))

                except TypeError:
                    UserView.isnotvalidkey()

                else:
                    if choice == 1:
                        flag2 = False
                        flag1 = True
                    elif choice == 2:
                        flag2 = False
                        flag1 = False
