from Controller.Medicine_controller import Med_Products
from Model.view_cart import MedCart
# from Model.database_connection import connection,my_cursor
from View.User_View import User_View
from View.view_medicine import view_medicine

MedNameList = []
Price_List = []


class medicine():
    @classmethod
    def items(self):
        global flag
        flag = True
        while flag:
            # # print("")
            # # print("1.OTC Medicine")
            # # print("2.Skin Care")
            # view_medicine.view_medlist()
            view_medicine.view_medlist()
            choice = int(input("Enter Product Choice: "))
            print("*-----*-----*-----*-----*-----*")
            ###OTC MEDCINE###
            if (choice == 1):
                # # print("OTC MEDICINES")
                # # print("-------------")
                # # Otcmed=["aspirin","Gaviscon","Cepacol","Cetirizine","Paracetamol"]
                # # OTC_Price=[11,86.5,63.5,17.5,12]
                # Med="select * from OTC_Med"
                # my_cursor.execute(Med)
                # result = my_cursor.fetchall()
                result = Med_Products.OTC()
                for i in range(len(result)):
                    view_medicine.view_otc(i, result)
                view_medicine.select()
                otc_choice = int(input("Enter Otc-Medicine no: "))
                for i in range(len(result)):
                    if i == (otc_choice - 1):
                        view_medicine.view_otc(i, result)
                        MedNameList.append(result[i][0])
                        Price_List.append(result[i][1])
                        view_medicine.add_medicine()
                        k = int(input("Enter Your Choice: "))
                        if k == 1:
                            MedCart.view_medcart(MedNameList, Price_List)
                            flag = False
                        elif k == 2:
                            Med_Products.OTC()
                        else:
                            print("***Skipped Here***")
                            print("*-*" * 5)
                # # for i in range(len(result)):
                #     print(i+1," ",result[i][0]," : Rs.",result[i][1])
                # print("*-----*-----*-----*-----*-----*")
                # print("")
                # print("If you want to select the medicine,enter the numbers (no alphabets & no special characters)")
                # view_medicine.select()
                # flag = False

                # Eo_choice = int(input("Enter Otc-Medicine no: "))
                # for i in range (len(result)):
                #     if (i == (Eo_choice-1)):
                #         print(i+1,"  ","Medicine: ",result[i][0]," - Rs",result[i][1])
                # my_cursor.execute("insert into view__med  values(%s,%s)",(result[i][0],result[i][1]))
                # connection.commit()
                # MedNameList.append(result[i][0])
                # Price_List.append(result[i][1])
                # print("Selected Medicine is added to the Cart")
                # print("*------*-----*-----*-----*-----*------*")
                # print("")
                # print("1.View Cart \n2.Add Medicine \n3.Skip")
                # k=int(input("Enter Your Choice: "))
                # if k==1:
                #      MedCart.view_medcart(MedNameList,Price_List)
                #      flag = False
                # elif k==2:
                #      self.items()
                # else:
                #      print("***Skipped Here***")
                #      print("*-----*-----*-----*-----*-----*")
            ###SKIN_CARE####
            elif (choice == 2):
                # print("SKIN CARE MEDICINES")
                # print("--------------------")
                # Med="select * from Sc_Med"
                # my_cursor.execute(Med)
                # result = my_cursor.fetchall()
                Med_Products.Skincare()
                # Skin_Care=["Calamine Lotion","cetaphil gentle","Eucerin Cream","Differin 0.1 gel","Isotretinoin"]
                # Sc_Price=[125,184.5,167.6,263.5,778]
                # for i in range(len(result)):
                #     print(i+1," ",result[i][0],": Rs. ", result[i][1])
                # print("*-----*-----*-----*-----*-----*")
                # print("")
                # print("If you want to select the medicine,enter the numbers (no alphabets & no special characters)")
                view_medicine.select()
                flag = False
                # ES_choice = int(input("Enter Skin care - Medicine no: "))
                # for i in range (len(result)):
                #         if (i == (ES_choice-1)):
                #             print(i +1,"  ","Skin Care Product: ",result[i][0]," - Rs",result[i][1])
                #             # my_cursor.execute("insert into view__med  values(%s,%s)",(result[i][0],result[i][1]))
                #             # connection.commit()
                #             MedNameList.append(result[i][0])
                #             Price_List.append(result[i][1])
                #             print("Selected Medicine is added to the Cart")
                #             print("*------*-----*-----*-----*-----*------*")
                #             print("")
                #             print("1.View Cart \n2.Add Medicine \n3.Skip")
                #             k=int(input("Enter Your Choice: "))
                #             if(k==1):
                #                 MedCart.view_medcart(MedNameList,Price_List)
                #                 flag = False
                #             elif k==2:
                #                 self.medProducts()
                #             else:
                #                   print("***Skipped Here***")
                #                 print("*-----*-----*-----*-----*-----*")

            else:
                User_View.invalid_choice()
                # print("You Have Selected a Invalid Choice...!!")
