class Fund1:
    Fundname1="HDFC MUTLUCAP"
    NAV1=108
    AUM1=20000
    XIRR1=18

class Fund2:
    Fundname2="AXIS MULTICAP"
    NAV2=103
    AUM2=25000
    XIRR2=17


class Investor(Fund1, Fund2):
    def __init__(self):
        self.amount = int(input("Enter your investment amount: "))
        print(f"Your investment amount is {self.amount}")

    def calculator(self):
        Unit1_fund1 = self.amount / self.NAV1
        Unit1_fund2 = self.amount / self.NAV2
        ROI_1 = self.amount * self.XIRR1 * 1 / 100
        ROI_2 = self.amount * self.XIRR2 * 1 / 100

        if (Unit1_fund1 > Unit1_fund2 and ROI_1 > ROI_2):
            print(f"you will get maximum no of unit from this {self.Fundname1} is {Unit1_fund1} and the ROI is {ROI_1}")
        elif (Unit1_fund2 > Unit1_fund1 and ROI_2 > ROI_1):
            print(f"you will get maximum no of unit from this {self.Fundname2} is {Unit1_fund2} and the ROI is {ROI_2}")
        else:
            print(f"The units you will get from {self.Fundname1} is {Unit1_fund1}")
            print(f"The units you will get from {self.Fundname2} is {Unit1_fund2}")
            print(f"The Return  you will get from {self.Fundname1} is {ROI_1}")
            print(f"The Return  you will get from {self.Fundname2} is {ROI_2}")
 
    
Obj=Investor()       
Obj.calculator() 