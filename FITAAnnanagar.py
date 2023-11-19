from FITABaseBranch import FITABaseBranch

class FITAANNANAgar(FITABaseBranch):

    CourseFee = ["Python-20000","Java-15000","C#-25000","SQL-17000","REACT-20000"]

    def Get_BranchName(self):
        print(self.name," - Anananagar")

    def Get_CourseFees(self,CourseName):
        if(self.Get_Course(CourseName)==True):
            for eachCoursePrice in self.CourseFee:
                courseSplit = eachCoursePrice.split("-")
                if(courseSplit[0]==CourseName):
                    print("Your fees amount is",courseSplit[1])
                    return int(courseSplit[1]);
        else:
            print("The requested course ", CourseName," is not available")
        return 0

#obj = FITAANNANAgar()
#obj.Get_BranchName()
#obj.Get_CourseFees("JAVA")

