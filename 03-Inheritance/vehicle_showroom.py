class Vehicle:
    def __init__(self,make,model,base_price):
        '''The Parent Class holding common attributes for all vehicles.'''
        self.make=make
        self.model=model
        self.base_price=base_price

    '''Generic display method to be overridden by child classes.'''
    def display(self):
        print(f"Brand: {self.make}\nModel: {self.model}\nBase Price: {self.base_price}")

class ElectricCar(Vehicle):
    '''The Child Class inheriting from Vehicle with specialized features.'''
    def __init__(self, make, model, base_price,battery_capacity):
        super().__init__(make, model, base_price)
        self.battery_capacity=battery_capacity

    def display(self):
        '''Method Overriding: Customizing the display specifically for EVs.'''
        super().display()
        print("Unique Feature:~ ")
        print(f"Battery Capacity: {self.battery_capacity} KWh")

class SuperBike(Vehicle):
    '''Another Child Class inheriting from Vehicle with different features.'''
    def __init__(self, make, model, base_price,top_speed):
        super().__init__(make, model, base_price)
        self.top_speed=top_speed

    def display(self):
        '''Method Overriding: Customizing the display specifically for Sports Bikes.'''
        super().display()
        print("Unique Feature:~ ")
        print(f"Top Speed: {self.top_speed} Km/hr")

#Testing the Showroom Inventory
print("======== Welcome to Premium Showroom ===========")

#creating common car
car1=Vehicle("Co.123","M4",1800000)
car1.display()

print("-"*50)

#1. Instantiating Electric Car Object
tesla=ElectricCar("Tesla","Model S",7500000,100)
tesla.display()

print("-"*50)

#2. Instantiating Super Bike Object
ninja=SuperBike("Kawasaki","Ninja H2R",3800000,400)
ninja.display()

