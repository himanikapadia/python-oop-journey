import datetime
class SmartDevice:
    def __init__(self,device_id,name,brand):
        self.device_id=device_id
        self.name=name
        self.brand=brand
        self.is_on=False
        self.last_sync=datetime.datetime.now()

    def toggle_power(self):
         self.is_on= not self.is_on
         self.last_sync=datetime.datetime.now()
         status="ON" if self.is_on else "OFF"
         print(f"{self.name} has been turned {status}.")

    def display_status(self):
        status="Active" if self.is_on else "Standby"
        sync_str = self.last_sync.strftime("%H:%M:%S")
        print(f" [{self.device_id}] {self.brand} {self.name} | Status: {status:<7} | Last Sync: {sync_str}")

class SmartThermo(SmartDevice):
    def __init__(self, device_id, name, brand,curr_temp):
        super().__init__(device_id, name, brand)
        self.curr_temp=curr_temp

    def setTemp(self,new_temp):
        self.curr_temp=new_temp
        self.last_sync=datetime.datetime.now()
        print(f"{self.name} target temperature updated to {self.curr_temp}°C.")

    def display_status(self):
        super().display_status()
        print(f"    '-> Target Temperature setup: {self.curr_temp}°C.")

class SmartSecurityCamera(SmartDevice):
    def __init__(self, device_id, name, brand,storage_capacity):
        super().__init__(device_id, name, brand)
        self.storage_capacity=storage_capacity
        self.is_recording=False

    def toggle_recording(self):
        if not self.is_on:
            print(f" X Cannot record: Turn on {self.name} first!")
            return 
        self.is_recording = not self.is_recording
        status = "STARTED" if self.is_recording else "STOPPED"
        print(f"🎥 Live Stream Recording {status} on {self.name}.")

    def display_status(self):
        """Method Overriding: Appending security streams to base status report."""
        super().display_status()
        rec_status = "RECORDING" if self.is_recording else "IDLE"
        print(f"    '-> Security Stream Mode: {rec_status} | Local Cloud Storage: {self.storage_capacity}GB")

        # --- Testing the Smart Home Network Hub ---

print("=== 🏡 CONNECTING TO SMARTHOME HUB ===\n")

# 1. Setup a Living Room Thermostat
thermostat = SmartThermo("T-404", "Nest Thermostat E", "Google", 24.0)
thermostat.toggle_power()
thermostat.setTemp(21.5)
thermostat.display_status()

print("-" * 70)

# 2. Setup a Front Door Security Camera
camera = SmartSecurityCamera("C-808", "Cam Outdoor 3", "Wyze", 128)
# Try recording while camera power is off
camera.toggle_recording() 
camera.toggle_power()
camera.toggle_recording()
camera.display_status()
        
