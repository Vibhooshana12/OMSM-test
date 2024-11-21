from Model.order import OrderMed
from View.view_medicine import view_medicine


# from Model.database_connection import connection,my_cursor
class MedCart:
    def view_medcart(Medlist, Medprice):
        flag = True
        global check
        global length
        check = 0
        length = len(Medprice)
        while flag:
            for i in range(len(Medprice)):
                view_medicine.ViewCart(i,Medlist,Medprice)
            #     print(i + 1, "For", Medlist[i], " : Rs. ", Medprice[i])
            # print("*-----*-----*-----*-----*-----*")
            # print(" " * 6)
            if check <= length:
                print(" ")
                k = int(input("Do you want to order the medicine??\n1.Yes/press any key to view medicines only numbers:"))
                check += 1
                # if k==1:  
                #     i = int(input("Enter your choice:"))
                #     i-=1              
                #     OrderMed.ordermed(Medprice[i],i)
                if k == 1:
                    i = int(input("Enter your choice:"))
                    if i <= len(Medprice):
                        i -= 1
                        OrderMed.ordermed(Medprice[i], i)

                    else:
                        User_View.valueError()
                        # print("Kindly give A valid Input :)")

            else:
                flag = False
