import openpyxl


class MakeMyTripTestDataRead():
    Data={}
    def excelFileRead(self,Sheetname):
        WBK = openpyxl.load_workbook("C:\\Users\\sathishkumar\\PycharmProjects\\FITAPythonSelenium\\input\\MakeMyTrip.xlsx")
        sheetName = WBK[Sheetname]
        totalRows = sheetName.max_row
        print("totalrows: ",totalRows)
        totalColumn = sheetName.max_column
        print("totalColumn: ",totalColumn)
        for eachRow in range(1,totalRows+1):
            for eachColumn in range(1, totalColumn + 1):
                eachValue = sheetName.cell(row=eachRow,column=eachColumn).value
                if(eachColumn==1):
                    self.Data[sheetName.cell(row=1,column=eachColumn).value+str(eachRow)]=eachValue
                if (eachColumn == 2):
                    self.Data[sheetName.cell(row=1,column=eachColumn).value+str(eachRow)]=eachValue
                if (eachColumn == 3):
                    self.Data[sheetName.cell(row=1,column=eachColumn).value+str(eachRow)]=eachValue
        print(self.Data)
        WBK.close()
        return self.Data
