global name
name = "sathish kumar","heera";
fees1=fees2=fees=15000

print("sahtish");
print("hi","sathish")
print("welcome","sathish")

print(name);
print("hi",name)
print("welcome",name)

def welcome():
    student = "sathish Fita"
    print(student) #locAL variable
    print(name) #global variable
    print(type(name))
    print(fees1)

def anotherstudent():
    print(name)
    print("fees 2 is :", fees2)

welcome()
anotherstudent()
global a
a=10
def add():
    a=10
    print(a)
    a*=2 # a= a+2
    print(a)

add()