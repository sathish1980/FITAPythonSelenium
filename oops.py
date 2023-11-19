class oopsconcept:
    name = "sathish"
    print (name)
    age=0

    def __init__(self,age):
        print("fita")
        self.age = age

    def __init__(self,age,amount):
        print("fita",amount)
        self.age = age

    def add(self,a,b):
        c=a+b;
        print(c)

    def div1(self, a, b):
        a/b;

    def div(self,a,b):
        try:
            c=a/b;
            print(c)
        except ArithmeticError :
            print("airthmetic exception")
        except ZeroDivisionError :
            print("zero exception")
        except Exception:
            print(Exception)
        finally:
            print("finally")

    def mul(self,a,b):
        c=a*b;
        print(c)

    def sub(self,a,b):
        c=a-b;
        print(c)


abcd = oopsconcept(7,11)
abcd.add(2,3)
abcd.sub(2,3)
#abcd.div1(2,0)
abcd.div(2,0)
abcd.mul(2,3)