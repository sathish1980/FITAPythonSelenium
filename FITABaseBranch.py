class FITABaseBranch():
    name = "FITA"
    course ={"Python","Java","C#","SQL"}
    availabe = "not identified"
    def Get_Course(self,expectedCourse):
        for eachCourse in self.course:
            if(expectedCourse==eachCourse):
                print("The ",expectedCourse,"is available")
                self.availabe="identified"
                return True

        return abcd.CheckIsAvailable(self.availabe)

    def CheckIsAvailable(self, condition):
        if (condition == "not identified"):
            return False

abcd = FITABaseBranch()
abcd.Get_Course("MYSQL")

