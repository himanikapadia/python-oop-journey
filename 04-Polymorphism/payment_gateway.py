class PaymentGateway:
    """The Parent Class. It just sets up the basic idea of paying."""
    def process_payment(self, amount):
        # This will be overwritten by the child classes below
        print("Processing a general payment...")


class CreditCardPayment(PaymentGateway):
    """Child Class 1: Handles Card Payments."""
    def __init__(self, card_holder):
        self.card_holder = card_holder

    def process_payment(self, amount):
        """Polymorphism: Changing how payment works for cards."""
        print(f"💳 Card Payment Processed for {self.card_holder}!")
        print(f"   Charged: ₹{amount}")


class UPIPayment(PaymentGateway):
    """Child Class 2: Handles UPI Payments (GPay/PhonePe)."""
    def __init__(self, upi_id):
        self.upi_id = upi_id

    def process_payment(self, amount):
        """Polymorphism: Changing how payment works for UPI."""
        print(f"📱 UPI Payment Processed via ID: {self.upi_id}!")
        print(f"   Transferred: ₹{amount}")


# --- The Polymorphic Function ---
# This single function can handle ANY payment object you give it!
def store_checkout(payment_object, amount):
    payment_object.process_payment(amount)
    print("-" * 40)


# --- Testing the Simple System ---

print("=== 🛍️ MY EASY STORE CHECKOUT ===\n")

# 1. Pay using a Card
card = CreditCardPayment(card_holder="Neha")
store_checkout(card, amount=500)

# 2. Pay using UPI
upi = UPIPayment(upi_id="neha@upi")
store_checkout(upi, amount=150)
