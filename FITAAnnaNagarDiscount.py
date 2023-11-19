from FITAAnnanagar import FITAANNANAgar


class FITAAnnanagarDiscount(FITAANNANAgar):

    discount =0.15

    def Get_Discount(self,CourseName):
        Course_Amount = self.Get_CourseFees(CourseName)
        if(Course_Amount>0):
            discountAmount =Course_Amount*self.discount
            Overallamount = Course_Amount-discountAmount
            print("You have to pay ",Overallamount)

obj= FITAAnnanagarDiscount()
obj.Get_Discount("SQL")