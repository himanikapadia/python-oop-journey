class CPU:
    #Composition method of CPU class
    def process(self):
        print("CPU is processing Data...")

class RAM:
    def load(self):
        print("RAM is Loading Applications....")

class Battery:
    def power(self):
        print("Battery is Supplying Power....")

class laptop:
    def __init__(self):
        self.cpu=CPU() #Laptop HAS a CPU
        self.ram=RAM() #Laptop HAS a RAM
        self.battery=Battery() #Laptop HAS a Battery

    def start(self):
        print("==== Starting Laptop =====")
        self.battery.power()
        self.cpu.process()
        self.ram.load()
        print("Laptop is ready to use...")

#Drivers Code
lap=laptop()

#Accessing Composition classes using Laptop class object
lap.start()