class NotificationService:
    """The Parent Class setting up a general notification footprint."""
    def send(self, message):
        # This will be overridden by the child classes below
        print("Sending a general notification...")

class EmailNoti(NotificationService):
    def __init__(self,emailId):
        self.emailId=emailId

    def send(self,message):
        """Polymorphism: Customizing how an email is sent."""
        print(f"📧 Email Sent to: {self.emailId}")
        print(f"   Subject: Alert | Message: {message}")

class SmsNoti(NotificationService):
    def __init__(self,phone):
        self.phone=phone

    def send(self,message):
        """Polymorphism: Customizing how an SMS is sent."""
        print(f"💬 SMS Sent to: {self.phone}")
        print(f"   Message: {message}")

# --- The Polymorphic Function ---
# This function can accept ANY notification object and execute the .send() command

def send_alert(obj,message):
    obj.send(message)
    print("-" * 50)

# --- Testing the System ---

print("=== 🔔 SMART NOTIFICATION ENGINE ===\n")

# 1. Trigger an Email Alert
email_user = EmailNoti("neha@vnsgu.edu")
send_alert(email_user, message="Your exam schedule has been updated!")

# 2. Trigger an SMS Alert
sms_user = SmsNoti("+91 98765-43210")
send_alert(sms_user, message="OTP for your secure login is 4491.")

