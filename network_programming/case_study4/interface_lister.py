# File: interface_lister.py
import socket
import struct

print("=" * 60)
print(f"LAB MONITOR: Fetching Interface Profiles for {socket.gethostname()}")
print("=" * 60)

# Verify if the operating system supports native programmatic interface discovery
if hasattr(socket, "getifaddrs"):
    # Pull raw linked attributes directly from the OS
    records = socket.getifaddrs()
    interface_profiles = {}
    
    for r in records:
        name = r.name
        if name not in interface_profiles:
            # Initialize storage mapping for each distinct network card entry
            interface_profiles[name] = {
                "IPs": [], 
                "Active": "Unknown", 
                "Multicast": "Not Supported"
            }
        
        # 1. Read System Status Flags (Checks if Active and if Multicast is on)
        if r.flags is not None:
            # Traditional OS Kernels use bitwise flags: 0x1 for UP, 0x8000 for MULTICAST
            is_up = bool(r.flags & 0x1)
            supports_multicast = bool(r.flags & 0x8000) if hasattr(socket, "IFF_MULTICAST") else True
            
            interface_profiles[name]["Active"] = "YES (Up)" if is_up else "NO (Down)"
            interface_profiles[name]["Multicast"] = "YES (Supported)" if supports_multicast else "NO"
            
        # 2. Extract Assigned Address Lines
        if r.addr and r.family in (socket.AF_INET, socket.AF_INET6):
            interface_profiles[name]["IPs"].append(r.addr[0])

    # Display our findings cleanly
    for name, profile in interface_profiles.items():
        print(f"\n[Interface]:   {name}")
        print(f"  -> Active:    {profile['Active']}")
        print(f"  -> Multicast: {profile['Multicast']}")
        print(f"  -> Addresses: {', '.join(profile['IPs']) or 'No IPs Assigned'}")

else:
    # Safe fallback if executed on heavily restrictive sandboxed runtimes
    print("Direct hardware property tracking requires local OS tool access.")
    print("Windows Fallback: Please run 'ipconfig /all' in your terminal.")
    print("Mac/Linux Fallback: Please run 'ifconfig' or 'ip link' in your terminal.")

print("\n" + "=" * 60)