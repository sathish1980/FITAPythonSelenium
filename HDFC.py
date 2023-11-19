from RBI import RBI


class HDFC(RBI):

    def GetLoanType(self):
        self.LoanType()
    def GetInterestRate(self):
        return 14.5

    def HDFCInteresRate(self):
        rate =self.GetInterestRate()
        print("The interest rate for HDFC Home loan is : ",rate)

obj2= HDFC()
obj2.GetLoanType()
obj2.HDFCInteresRate()