class view_medicine:

    @staticmethod
    def view_medlist():
        print("")
        print("1.OTC Medicine")
        print("2.Skin Care")

    @classmethod
    def view_otc(cls, i, result):
        print(i + 1, " ", result[i][0], " : Rs.", result[i][1])

    @classmethod
    def view_skincare(cls, i, result):
        print(i + 1, " ", result[i][0], " : Rs.", result[i][1])

    @staticmethod
    def select():
        print("*-----*-----*-----*-----*-----*")
        print("")
        print("If you want to select the medicine,enter the numbers (no alphabets & no special characters)")

    # @classmethod
    # def select_medicine(cls,i,result):
    #     print(i + 1, "  ", "Medicine: ", result[i][0], " - Rs", result[i][1])
    @staticmethod
    def add_medicine():
        print("Selected Medicine is added to the Cart")
        print("*------*-----*-----*-----*-----*------*")
        print("")
        print("1.View Cart \n2.Add Medicine \n3.Skip")

    @classmethod
    def ViewCart(cls,i,Medlist,Medprice):
        print(i + 1, "For", Medlist[i], " : Rs. ", Medprice[i])

    @staticmethod
    def outofstock():
        print("Selected Medicine is Out Of Stock...")
        print("*-----*-----*"*4)

    # @classmethod
    # def billmessage(cls ,Total_cost):
    #     print("Total Cost:", Total_cost)
    #     print("*-----*-----*-----*-----*-----*")
    #     print("")
    #     print("1.MakePayment.\n2.Cancel Order.")

