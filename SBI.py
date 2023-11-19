from RBI import RBI


class SBI(RBI):

    def GetLoanType(self):
        self.LoanType()

    def SBIInteresRate(self):
        rate =self.GetInterestRate()
        print("The interest rate for HDFC Home loan is : ",rate)

obj2= SBI()
obj2.GetLoanType()
obj2.SBIInteresRate()