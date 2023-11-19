class list():
    name ="sathish"
    #fruits = ["apple","orange","pineapple","grape","apple"]
    #occasionalFruits = ["Mango","watermelon"]
    fruits = ("apple", "orange", "pineapple", "grape", "apple")
    occasionalFruits = ("Mango", "watermelon")
    #a=tuple(fruits)
    def listimple(self):
        a=10,20
        print(type(self.fruits))
        print(self.fruits)
        print(self.fruits[0:2])
        print(len(self.fruits))

        if("grape" in self.fruits):
            print("yes")
        for eachvalue in self.fruits:
            print(eachvalue)
            if(eachvalue=="grapes"):
                print('yes')
                break
        print("#################")
        for eachvalue in range(0,len(self.fruits)):
            print(self.fruits[eachvalue])
        #self.fruits[1]="banana"
        #self.fruits[1:3] = ["banana","lemon"]
        print(self.fruits)
        #self.fruits.insert(10,"berry")
        print(self.fruits)
        #self.fruits.append("chiku")
        print(self.fruits)
        #self.fruits.extend(self.occasionalFruits)
        print(self.fruits)
        #self.fruits.remove("chiku")
        print(self.fruits)
        #self.fruits.pop(1) # delte by index
        print(self.fruits)
        #self.fruits.pop() # last value will be removed
        print(self.fruits)
        #newist = self.fruits.copy()
        #self.fruits.clear()
        print(self.fruits)
        #print(newist)
       # newist.sort(reverse = True)
       # print(newist)

       # del self.fruits
       # print(self.fruits)

obj = list()
obj.listimple()