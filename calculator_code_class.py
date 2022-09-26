class Calculator:
    #def __init__(self,a,b):
        #self.no1=a
        #self.no2=b 
    def addNumbers(self,a,b):
        return a+b
    def subtractNumbers(self,a,b):
        return a-b
    def multiplicateNumbers(self,a,b):
        return a*b
    def divideNumbers(self,a,b):
        return a/b


#from calculator_code_class import Calculator       


choice=1
while choice!=0:
    print("1. Add")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("0. Exit")
    choice = int(input("Enter choice: "))
    frstNo= int(input("Enter first number:"))
    secNo= int(input("Enter second number:"))
    calculator= Calculator()
    if choice == 1:
        additn=calculator.addNumbers(frstNo,secNo)
        print(additn )
    elif choice == 2:
        substr=calculator.subtractNumbers(frstNo,secNo)
        print(substr)
    elif choice == 3:
        multi=calculator.multiplicateNumbers(frstNo,secNo)
        print(multi)
    elif choice == 4:
        divi=calculator.divideNumbers(frstNo,secNo)
        print(divi)
    elif choice == 0:
        print("EXIT")
    else:
        print("no choice exist")
    
    
    
'''
additn=calculator.addNumbers()
print(additn)
substr=calculator.subtractNumbers()
print(substr)
multi=calculator.multiplicateNumbers()
print(multi)
divi=calculator.divideNumbers()
print(divi)

print("1. Add")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("0. Exit")
'''

