class Atm:
    bank_name="Coder Bank"
    def __init__(self,acc_name,pin,initial_balance):
        self.acc_name=acc_name

        self.__pin=pin
        self.__initial_balance=initial_balance

    def display_balance(self,entered_pin):
        if entered_pin==self.__pin:
            print(f"\nAccount holder: {self.acc_name}")
            print(f"Bank Name: {self.bank_name}")
            print(f"Current Balance: {self.__initial_balance}")
        else:
            print("\n\nInvalid Pin! Access denied")
    def deposit(self,entered_pin,amt):
        if entered_pin==self.__pin:
            if amt>0:
                self.__initial_balance+=amt
                print(f"\n{amt} Rs. deposited successfully in {self.bank_name}")
            else:
                print("\nInvalid deposit Amount!")
        else:
            print("\nInvalid Pin! deposit blocked!")
    def withdraw(self,entered_pin,amt):
        if entered_pin==self.__pin:
            if amt>self.__initial_balance:
                print(f"\nInsuffient balance! you can't withdraw")
            elif amt<=0:
                print("\nInvalid withdrawal amount")
            else:
                self.__initial_balance-=amt
                print(f"\n{amt} Rs. successfully withdrawn!")
        else:
            print("\nInvalid pin! withdrawal blocked!")

acc1=Atm("Dr. Raj",1234,2000) #Object created

#we can access class and public attributes
print(f"Bank Name: {acc1.bank_name}")
print(f"Account holder name (Public attribute): {acc1.acc_name}")

#Demonstration of Encapsulation
# print(acc1.__initial_balance) --> This will create an error 
print("The PIN and Balance attributes are safely encapsulated and hidden!")

#Test 1: Try checking balance with the WRONG pin
acc1.display_balance(1111)
    
#Test 2: Deposit money with the CORRECT pin
acc1.deposit(entered_pin=1234,amt=2000)

#ERROR due to accessing private attributes
#print(acc1.__initial_balance()) 

# Test 3: Attempt a withdrawal with INSUFFICIENT funds
acc1.withdraw(entered_pin=1234,amt=1000000)

# Test 4: Successful withdrawal
acc1.withdraw(entered_pin=1234,amt=500)

# Test 5: Display final statement
acc1.display_balance(entered_pin=1234)


        