class txtFile():

    def readFile(self):
        filepath = "C:\\Users\\sathishkumar\\PycharmProjects\\FITAPythonSelenium\\input\\sample.txt"
        fileToRead = open(filepath, "r")
        #print(fileToRead.read())
        i=0
        #print(fileToRead.readline())
        #while(i<3):
           # print(fileToRead.readline())
           # i=i+1
        #print(fileToRead.readlines())
        for eachvalue in fileToRead.readlines():
            print(eachvalue)
        fileToRead.close()
    def writefile(self):
        filepath = "C:\\Users\\sathishkumar\\PycharmProjects\\FITAPythonSelenium\\input\\output.txt"
        fileToWrite = open(filepath, "a")
        fileToWrite.write("sathish kumar R latest data with append")
        fileToWrite.close()

obj=txtFile()
obj.readFile()
obj.writefile()

