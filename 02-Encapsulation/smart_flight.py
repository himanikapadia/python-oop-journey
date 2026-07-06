class SmartFlight:
    airline_name="Indigo Airlines"

    def __init__(self,passenger_name,passport_no,base_fare):
        self.passenger_name=passenger_name
        self.seat_class="Economy" #default class

        #Encapsulated (Private) Attributes using '__'
        self.__passport_no=passport_no
        self.__base_fare=base_fare

        # --- Creating the Base Object Today ---
ticket = SmartFlight("Dr. Neha", "Z1234567", 60000)

print(f" Airline (Class Variable): {ticket.airline_name}")
print(f" Passenger (Public): {ticket.passenger_name}")
print("\n Passport and Fare attributes are safely encapsulated and hidden!")
        
