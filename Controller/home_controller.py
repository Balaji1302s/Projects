from View.UserView import UserView
from Model.UserValidation import New_Registration,Login

class UserChoice:

    @classmethod
    def user_choice(cls):
        UserView.greetings()

    flag = True
    while flag:

        choice = UserView.user_choice()

        if choice == 1:
            UserView.signup()
            New_Registration.new_user()

        elif choice == 2:
            Login.login()

        else:
            print("There is no Such Kind of action")

