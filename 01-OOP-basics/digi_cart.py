class DigitalCart():
    def __init__(self,username): #constructor for new customer
        self.username=username
        self.items={}
    def add_items(self, item_name,price):
        self.items[item_name]=price
        print(f"Added {item_name} to {self.username}'s cart")
    def checkout(self): # Final invoice
        total=sum(self.items.values())
        print(f"\n---- {self.username}'s Invoice: -------")
        for item,price in self.items.items():
            print(f"- {item}: {price} Rs.")
        print(f"Total Amount : {total} Rs.")

#creating objects
dc=DigitalCart("Abc")
dc.add_items("Wireless mouse",500)
dc.add_items("Bluetooth speakers",2000)
dc.checkout()