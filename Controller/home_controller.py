from Model.user_validation import Signup
from Model.user_validation import Login
from View.User_View import User_View

class Choice_preference:
    @classmethod
    def choice(self):
        # print("\t\t\t\t*.*.*.*.*.*Welcome To Sasi Pharmacy*.*.*.*.*.*\t\t\t\t")
        User_View.greetings()
        C=True
        while C:
            # print("1.Signup / 2.Login/ 3.Logout")
            User_View.userchoices()
            try:
                choices = int(input("Enter your choice: "))
            except ValueError:
                # print("\t\t\tYou have entered invalid choice,enter numbers\t\t\t")
                User_View.valueError()
            else:
                if choices == 1:
                    Signup.signup()
                elif choices == 2:
                    Login.signin()   
                elif choices == 3:
                    # print("\t\t\t.*.*.*.*.*.*.*.*.(THANK YOU FOR VISITING US!!!).*.*.*.*.*.*.*.*.\t\t\t")
                    User_View.logout()
                    C= False
                else:
                    print("\t\t\t<<<<<<<Invalid Choice>>>>>>>\t\t\t")