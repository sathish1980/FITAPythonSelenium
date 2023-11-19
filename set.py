class set():
    fruits ={"chicku","apple","banana","apple"}
    def setImplementation(self):
        print(self.fruits)
        print(len(self.fruits))
        #self.fruits[1]="mango"
        print(self.fruits)
        for eachvalue in self.fruits:
            print(eachvalue)
        self.fruits.add( "mango")
        print(self.fruits)
        additionalfruits = ["lichi","grapes"]
        self.fruits.update(additionalfruits)
        print(self.fruits)
        self.fruits.remove("grapes")
        print(self.fruits)
        self.fruits.discard("orange")
        print(self.fruits)
        self.fruits.pop()
        print(self.fruits)
        #del self.fruits
        print(self.fruits)
        sesonalfruit = {"lichi","mango"}
        output = self.fruits.difference(sesonalfruit)
        print(output)
        print(self.fruits)
        #self.fruits.difference_update(sesonalfruit)
        print(self.fruits)
        output1 = self.fruits.intersection(sesonalfruit)
        print(output1)
        print(self.fruits)
        #self.fruits.intersection_update(sesonalfruit)
        print(self.fruits)
        output1 = self.fruits.issubset(sesonalfruit)
        print(output1)
        output1 = self.fruits.symmetric_difference(sesonalfruit)
        print(output1)
        output1 = self.fruits.issuperset(sesonalfruit)
        print(output1)
        print(type(self.fruits))



obj = set()
obj.setImplementation()
