from abc import ABC,abstractmethod
class Payment(ABC):
    #Abstract class

    @abstractmethod
    def verify_security_token(self):
        """Hidden engineering step that every gateway must handle differently."""
        pass

    @abstractmethod
    def pay(self,amount):
        pass

class GooglePay(Payment):

    def verify_security_token(self):
        print("Verifying UPI security token with Google servers...")

    def pay(self,amount):
        self.verify_security_token()
        print(f"The Payment of Rs. {amount} is Successfully paid using GOOGLE PAY!\n")

class PhonePay(Payment):

    def verify_security_token(self):
            print("Connecting to secure PhonePe payment bank vault...")

    def pay(self,amount):
        self.verify_security_token()
        print(f"The Payment of Rs. {amount} is Successfully paid using PHONE PAY!\n")

class Paytm(Payment):

    def verify_security_token(self):
                print("Verifying Paytm Wallet encrypted session...")
    
    def pay(self,amount):
        self.verify_security_token()
        print(f"The Payment of Rs. {amount} is Successfully paid using PAYTM!\n")

amount=float(input("Enter Amount to pay: "))

print("\n-------- Online Payment Options --------")
print("1. Google Pay")
print("2. Phone Pay")
print("3. Paytm\n")

choice=int(input("Enter your choice: "))

if choice==1:
    payment=GooglePay()

elif choice==2:
    payment=PhonePay()

elif choice==3:
    payment=Paytm()

else:
    print("Invalid choice")
    exit()

# Passing amount to object
payment.pay(amount)

