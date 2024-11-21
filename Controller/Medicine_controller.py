from Model.database_connection import my_cursor
from Model.view_cart import MedCart
from View.view_medicine import view_medicine

MedNameList = []
Price_List = []

class Med_Products:
    @classmethod
    def OTC(cls):
        print(" " * 6 + "*." * 5 + "OTC MEDICINES" + ".*" * 5)
        print("-" * 18)
        Med = "select * from OTC_Med"
        my_cursor.execute(Med)
        result = my_cursor.fetchall()
        return result
        # for i in range(len(result)):
        #     view_medicine.view_otc(i, result)
        # otc_choice = int(input("Enter Otc-Medicine no: "))
        # for i in range(len(result)):
        #     if i == (otc_choice - 1):
        #         view_medicine.view_otc(i, result)
        #         MedNameList.append(result[i][0])
        #         Price_List.append(result[i][1])
        #         view_medicine.add_medicine()
        #         k = int(input("Enter Your Choice: "))
        #         if k == 1:
        #             MedCart.view_medcart(MedNameList, Price_List)
        #         elif k == 2:
        #             Med_Products.OTC()
        #         else:
        #             print("***Skipped Here***")
        #             print("*-*" * 5)

    @classmethod
    def Skincare(cls):
        print(" " * 6 + "*." * 5 + "SKIN CARE MEDICINES" + ".*" * 5)
        print("-" * 18)
        Med = "select * from Sc_Med"
        my_cursor.execute(Med)
        result = my_cursor.fetchall()
        for i in range(len(result)):
            view_medicine.view_skincare(i, result)
        Sc_choice = int(input("Enter Skincare Medicine no: "))
        for i in range(len(result)):
            if i == (Sc_choice - 1):
                view_medicine.view_skincare(i, result)
                MedNameList.append(result[i][0])
                Price_List.append(result[i][1])
                view_medicine.add_medicine()
                k = int(input("Enter Your Choice: "))
                if k == 1:
                    MedCart.view_medcart(MedNameList, Price_List)
                elif k == 2:
                    Med_Products.Skincare()
                else:
                    print("***Skipped Here***")
                    print("*-*" * 5)
