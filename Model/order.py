from View.payment import Payment
from View.User_View import User_View
from View.view_medicine import view_medicine


class OrderMed:
    def ordermed(cost, index):
        Medstock = [20, 20, 20, 20, 20]
        quantity = int(input("Enter Quantity:"))
        if quantity <= Medstock[index]:
            Total_cost = (cost * quantity)
            User_View.billmessage(Total_cost)
            # print("Total Cost:", Tcost)
            # print("*-----*-----*-----*-----*-----*")
            # print("")
            # print("1.MakePayment.\n2.Cancel Order.")
            try:
                Verify = int(input("Enter Your Choice:"))
            except:
                User_View.valueError()
            else:
                if Verify == 1:
                    Payment.payment(Total_cost)
                elif Verify == 2:
                    User_View.Cancellation()
                # print("Your Order Has Been Cancelled....")
                # print("*-----*-----*-----*-----*-----*")
                # print("")
        else:
            view_medicine.outofstock()
            # print("Selected Medicine is Out Of Stock...")
            # print("*-----*-----*-----*-----*-----*")
