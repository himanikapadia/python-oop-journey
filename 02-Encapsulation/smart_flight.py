class SmartFlight:
    airline_name="Indigo Airlines"

    def __init__(self,passenger_name,passport_no,base_fare):
        self.passenger_name=passenger_name
        self.seat_class="Economy" #default class

        #Encapsulated (Private) Attributes using '__'
        self.__passport_no=passport_no
        self.__base_fare=base_fare

    def display_ticket(self,entered_passNo):
        if entered_passNo==self.__passport_no:
            print(f"\n ---- Boarding Pass: {self.airline_name} -----")
            print(f"Passenger Name: {self.passenger_name}")
            print(f"Seat Category: {self.seat_class}")
            print(f"Paid Ticket fare: {self.__base_fare}")
        else:
            print(f"\nAccess Denied!! Passport Verification failed")

    # 🔼 Secure Method to upgrade to Business Class (Requires verification & extra charges)
    def upgrade_business(self,entered_pass,extra_pay):
        if entered_pass!=self.__passport_no:
            print(f"\nUpgrade Failed! Unauthorised Passport Number.")
            return
        if self.seat_class=="Business":
            print("You are already in Business class!")
        elif extra_pay>=5000:
            self.seat_class="Business"
            self.__base_fare+=extra_pay
            print(f"Success! {self.passenger_name} has been upgraded to Business Class!")
        else:
            print("Upgrade Denied! Insufficent Payment for Business class Upgradation")

        # --- Testing Our Secure Flight Booking System ---


# 1. Book a flight ticket
ticket = SmartFlight("Dr. Neha", "Z1234567", 60000)
ticket.display_ticket(entered_passNo="Z1234567")

# 2. Try to print the private ticket price directly (Will fail due to encapsulation)
# print(ticket.__ticket_price)

# 3. View ticket with WRONG passport
ticket.display_ticket(entered_passNo="22222")

# 4. Attempt an upgrade with correct passport but not enough payment
ticket.upgrade_business("Z1234567",2000)

# 5. Successfully upgrade with correct passport and adequate payment
ticket.upgrade_business("Z1234567", 5500)

# 6. Verify the changes securely
ticket.display_ticket(entered_passNo="Z1234567")

        
