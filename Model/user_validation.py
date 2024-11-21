from Model.Medicine import medicine
from Model.database_connection import connection, my_cursor
from View.User_View import User_View
import time
import re
import getpass

Email_regex = r'^[A-Za-z0-9]+[\._]?[a-z0-9]+[@]+\w+[.]\w{2,3}$'
# Pcheck=r'^[a-z to A-Z to 0-9]+[!@#$%^&*()_+]?\w{0,5}$'
Password_regex = r'^[A-Z]?[a-z0-9]+[!@#$%^&*()_+]+\w{0,3}$'


class Signup():

    @classmethod
    def signup(cls):
        global User_Name, Email, Password, PhoneNumber
        v = True
        while v:
            User_View.view_signup()
            User_Name = input("Enter UserName:  ")

            Email = input("Enter Email Id:  ")
            User_View.pass_word()
            Password = input("Enter Password:  ")
            if re.search(Email_regex, Email):
                if re.search(Password_regex, Password):
                    v = False
                else:
                    User_View.password_Validation()
            else:
                User_View.email_Validation()

        flag = True
        while flag:
            try:
                PhoneNumber = int(input("Enter your Mobile number: "))
                # if 6000000000 < PhoneNumber < 10000000000 and PhoneNumber != (
                #         6666666666, 7777777777, 8888888888, 9999999999):
                #      pass
                # else:
                #     User_View.phone_Validation()
                # #     # print("\t\t\t<<<<<<<Enter the valid one>>>>>>>\t\t\t")
                # #      User_View.Phone_Validation()
            except ValueError:
                # print("\t\t\tYour Mobile Number entered is '<<<<Not Valid>>>>' try with a valid number\t\t\t")
                User_View.phone_Validation()

            else:
                if 6000000000 < PhoneNumber < 10000000000 and PhoneNumber != 6666666666 and PhoneNumber != 7777777777 and PhoneNumber != 8888888888 and PhoneNumber != 9999999999:
                    # Uphonenumber.append(PhoneNumber)
                    # print("\t\t\t\t!*!*!*!*!...Your Registration is Successful...!*!*!*!*!\t\t\t\t")
                    flag = False
                else:
                    User_View.phone_Validation()
        credential = "insert into user_details values(%s,%s,%s,%s);"
        my_cursor.execute(credential, (User_Name, Email, Password, PhoneNumber))
        connection.commit()
        time.sleep(2)
        print("\t\t", '!*' * 10 + "...Your Registration is Successful..." + '!*' * 10, "\t\t")


class Login():
    UserPassword = ""
    UserName = ""

    def __init__(self):
        self.UserName = " "
        self.UserPassword = " "

    @classmethod
    def signin(self):
        flag = True
        while flag:
            self.UserName = input("Enter UserName:  ")
            self.UserPassword = input("Enter UserPassword:  ")
            # print("*" *len(self.UserPassword))
            my_cursor.execute("SELECT * FROM user_details WHERE User_name = %s AND Password = %s",
                              (self.UserName, self.UserPassword))
            # query = "Select * from user_details where user_name= ?,;"
            # my_cursor.execute(query,(self.UserName,))
            user = my_cursor.fetchone()
            if user is not None:
                # print("\t\t\tHai", user[0], "you have Logged in Sucessfully:)\t\t\t")
                # time.sleep(2)
                # print("\t\t\t", user[0], "Welcome to Sasi Pharmacy:)\t\t\t")
                # print("")
                # print("View Medicine Products")
                User_View.login(user)
                medicine.items()
                flag = False
                # return True
            else:
                # print("\t\t\t<<<<<<<Invalid User>>>>>>\t\t\t")
                # print("\t\t\t<<<<<<<Enter a Valid User Name and Password>>>>>>>\t\t\t")
                User_View.invalid_user()
                flag = False
            # return false

            # print("success")
            # flag=False
            # if result[0] == self.UserName:
            # if self.UserPassword ==  result[1]:
            #     print("\t\t\tHai",result[0],"you have Logged in Sucessfully:)\t\t\t")
            #     time.sleep(2)
            #     print("\t\t\t",result[0],"Welcome to Sasi Pharmacy:)\t\t\t")
            #     print("")
            #     print("View Medicine Products")
            #     MedProducts.medProducts()
            # else:
            #     print("\t\t\t<<<<<<<Invalid User>>>>>>\t\t\t")
            #     print("\t\t\t<<<<<<<Enter a Valid User Name and Password>>>>>>>\t\t\t")
