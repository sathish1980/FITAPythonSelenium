print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
i=1
while i <= 100:

    i = i + 1;
    if i==50 or i==70:
        continue;
    #print(i)
    #i = i + 1;

courses = ["python","java","c#"]
print(type(courses))
print(courses)

actualcourse = "java"

for eachcourse in courses:
    if(eachcourse==actualcourse):
        continue;
    print(eachcourse)

for eachvale in range(10,20):
    print("first loop: ",eachvale)
    for anotheralue in range(10, 20):
        print(eachvale, anotheralue)

