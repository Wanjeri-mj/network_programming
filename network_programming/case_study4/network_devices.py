# File: network_devices.py
from abc import ABC, abstractmethod

# Step 1: Define the Abstract Base Class (ABC)
# This acts as a strict "contract" or blueprint. It guarantees that ANY hardware 
# we build later MUST have connect, send_data, and disconnect capabilities.
class NetworkDevice(ABC):
    
    @abstractmethod
    def connect(self):
        """Establish physical/wireless link layer connection."""
        pass
        
    @abstractmethod
    def send_data(self, data):
        """Transmit data payloads out over the established medium."""
        pass
        
    @abstractmethod
    def disconnect(self):
        """Gracefully tear down interface operational bindings."""
        pass

# Step 2: Implement the concrete Ethernet Hardware device
class EthernetDevice(NetworkDevice):
    def connect(self): 
        print("[Ethernet] Port link detected. Negotiating line speed (1Gbps)...")
        
    def send_data(self, data): 
        print(f"[Ethernet] Wrapping data into copper-wire frames: '{data}'")
        
    def disconnect(self): 
        print("[Ethernet] Port link down. Shutting down interface transceiver.")

# Step 3: Implement the concrete Wi-Fi Hardware device
class WiFiDevice(NetworkDevice):
    def connect(self): 
        print("[Wi-Fi] Scanning airwaves. Authenticating with WPA3 Security Protocol...")
        
    def send_data(self, data): 
        print(f"[Wi-Fi] Modulating radio frequencies to transmit packets: '{data}'")
        
    def disconnect(self): 
        print("[Wi-Fi] Disassociated from Access Point. Releasing radio bands.")


# --- Simulation Runner ---
if __name__ == "__main__":
    print("=" * 65)
    print("LAB SIMULATION: Initializing Hardware Interface Controller Arrays")
    print("=" * 65)

    # Polymorphism in action! We mix completely different device objects inside a unified list.
    device_inventory = [EthernetDevice(), WiFiDevice()]
    
    # We iterate through the inventory. Python doesn't need to know the specific hardware type
    # beforehand—it simply commands each device to execute its standard operational routine.
    for device in device_inventory:
        device.connect()
        device.send_data("Automated Lab Software Update Package")
        device.disconnect()
        print("-" * 65)