class Atm:
    bank_name="Coder Bank"
    def __init__(self,acc_name,pin,initial_balance):
        self.acc_name=acc_name

        self.__pin=pin
        self.__initial_balance=initial_balance

acc1=Atm("Dr. Raj",1234,2000) #Object created

#we can access class and public attributes
print(f"Bank Name: {acc1.bank_name}")
print(f"Account holder name (Public attribute): {acc1.acc_name}")

#Demonstration of Encapsulation
# print(acc1.__initial_balance) --> This will create an error 
print("\n The PIN and Balance attributes are safely encapsulated and hidden!")
        
