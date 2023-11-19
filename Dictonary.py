class dictonary():
    def dictonaryimplementation(self):
        student_Details = {
            "name":"sathish",
            "DOB" : "90",
            "Course" : "python",
            "name":"abdul"
        }
        print(student_Details)
        print(type(student_Details))
        print(len(student_Details))
        print(student_Details["name"])
        print(student_Details.get("name"))
        print(student_Details.keys())
        print(student_Details.values())
        print(student_Details.items())
        if "std" in student_Details.keys():
            print('yes')
        student_Details["SAT"] ="99"
        print(student_Details)
        student_Details.update({"DOB1":"96"})
        print(student_Details)
        student_Details.pop("DOB1")
        print(student_Details)
        student_Details.popitem()
        print(student_Details)
        

obj= dictonary()
obj.dictonaryimplementation()