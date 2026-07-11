from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    @abstractmethod
    def start(self):
        pass
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        print("\nCar started using Physical Key")

    def stop(self):
        print("Car Stopped!\n")

class Bike(Vehicle):
    def start(self):
        print("\nBike started using Self-start Ignition")

    def stop(self):
        print("Engine shut down safely\n")

class Scooter(Vehicle):
    def start(self):
        print("\nElectric Scooter started using Digital Power Button")

    def stop(self):
        print("Power Turned Off completely\n")

#Driver Code
print("\n===== Choose a Vehicle =====")
print("1. Car")
print("2. Bike")
print("3. Electric Scooter")
print("="*30)
choice=int(input("\nEnter your Choice: "))

if choice==1:
    vehicle=Car()

elif choice==2:
    vehicle=Bike()

elif choice==3:
    vehicle=Scooter()

else:
    print("Invalid Choice")

vehicle.start()
vehicle.stop()
