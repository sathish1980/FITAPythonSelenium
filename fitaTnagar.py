from FitaBase import FitaBase


class fittnagar(FitaBase):

    print("Hi")

    def getTax(self):
        print(self._baseprice)
        self.setBasePrice(500)
        print(self.getBasePrice())
        return 70

obj=fittnagar()
print(obj.getTax())