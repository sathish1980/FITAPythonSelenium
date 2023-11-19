"""print("sathish's")
print('sathish kumar')"""
print('''Hi welcom to fita
Thank you choosing FITA''')
a=15
print(type(a))
b='sathish'
print(type(b))
c=str(a)+(b)
print(c)

def taxCalculation():
    amount=10000
    taxPercentage=0.15
    actualAmount=amount*taxPercentage #1500
    print(actualAmount)

def taxCalculationwithArguments(amounts, taxPercentage):
    #taxPercentage=0.15
    actualAmount=amounts*taxPercentage #525.0
    return actualAmount

def totalAmount(amount, taxAmount):
    actualAmount = amount + taxAmount
    print(actualAmount) #4025.0

taxCalculation()
amountValue = 3500
actualTaxAmount = taxCalculationwithArguments(amountValue, 0.15) #525.0
totalAmount(amountValue, actualTaxAmount)
