import time


class User_View:
    @staticmethod
    def greetings():
        print("\t\t\t\t*.*.*.*.*.*Welcome To Sasi Pharmacy*.*.*.*.*.*\t\t\t\t")

    @classmethod
    def userchoices(cls):
        print("1.Signup / 2.Login/ 3.Logout")

    @staticmethod
    def valueError():
        print("\t\t\tYou have entered invalid choice,enter numbers\t\t\t")

    @staticmethod
    def view_signup():
        print(" " * 7 + "*." * 6, " Sign-Up to Explore " + ".*" * 6)

    @staticmethod
    def pass_word():
        print(
            "Enter Password that should :\n1.Starts with Capital Letter\n2.If you need Use Special Character(1)\n3.Note after Special Character 0 or 3 alphanumeric is accepted")

    @classmethod
    def login(cls, user):
        print(" " * 5, "*.", "Hai", user[0], "you have Logged in Successfully:)", ".*" * 6)
        time.sleep(1)
        print("\t\t\t", user[0], "Welcome to Sasi Pharmacy:)\t\t\t")
        print("")
        print("View Medicine Products")

    @staticmethod
    def logout():
        print("\t\t\t.*.*.*.*.*.*.*.*.(THANK YOU FOR VISITING US!!!).*.*.*.*.*.*.*.*.\t\t\t")

    @staticmethod
    def email_Validation():
        print("\t\t\t<<<<<<<Not Valid Email Id,Try Again>>>>>>>\t\t\t")

    @staticmethod
    def password_Validation():
        print("\t\t\t<<<<<<<Not Valid Password,Try Again>>>>>>>\t\t\t")

    @staticmethod
    def phone_Validation():
        print("\t\t\tYour Mobile Number entered is '<<<<Not Valid>>>>' Try with a Valid Number\t\t\t")

    @staticmethod
    def invalid_user():
        print("\t\t\t<<<<<<<Invalid User>>>>>>\t\t\t")
        print("\t\t\t<<<<<<<Enter a Valid User Name and Password>>>>>>>\t\t\t")

    @staticmethod
    def invalid_choice():
        print("You Have Selected a Invalid Choice...!!")

    @classmethod
    def billmessage(cls ,Total_cost):
        print("Total Cost:", Total_cost)
        print("*-----*-----*-----*-----*-----*")
        print("")
        print("1.MakePayment.\n2.Cancel Order.")

    @staticmethod
    def Cancellation():
        print("Your Order Has Been Cancelled....")
        print("*-----*-----*-----*-----*-----*")
        print("")






    # @staticmethod
    # def loginmessage():
    #     print("\n")
    #     print("-" * 100)
    #     print(" " * 10 + "*" * 20 + "Hi you are loggen in successfully" + "*" * 20 + " " * 10)
    #     print("-" * 100)
    #     print("\n")
    #
    # @staticmethod
    # def useractions():
    #     print("1 for view items")
    #     print("2 for view profile")
    #     print("Press any number key to goto login page")
    #
    # @classmethod
    # def viewuser(cls, result):
    #     print("Name       :     " + result[0])
    #     print("phone N.O. :     " + result[2])
    #     print("E-mail     :     " + result[3])
    #     print("\n")
    # @classmethod
    # def Email_validation(cls):
    #     pass
