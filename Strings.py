class string:
    course =["python","java","C#"]
    def stringconcpets(self ,partialname):
        name = "sathish kumar R "
        name1 = " sathish kumar R "
        print(name)
        print(len(name))
        space =name.strip();
        print(name.strip())
        print(name.lstrip())
        print(name.rstrip())
        print(space)
        print(name.replace(" ",""))
        print(name.replace("a", "AT"))
        print(name.upper())
        print(name.lower())
        print(name.islower())
        print(name.isupper())
        print(name.isalnum())
        if ("SATHISH" in name): # contains
            print ("exist")
        print(name==name1)
        if("python" in self.course):
            print("yes")
        splitString = name.split(" ")
        print(splitString)

        for eachcourse in splitString:
            print(eachcourse)
            if(eachcourse.upper()==partialname):
                print("Yes its avaiable")

        print(name+name1)
        print(name.startswith(" "))
        print(name.endswith("r"))
        print(name.index("s"))
        print(name.__contains__("kumar"))
        print(name.find("skumar"))
        print(name.swapcase())
        print(name.capitalize())
        print(list(reversed(self.course)))

obj = string()
obj.stringconcpets("KUMAR")