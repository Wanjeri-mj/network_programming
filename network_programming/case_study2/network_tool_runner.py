# File: network_tool_runner.py
import shutil
import subprocess

# Define the tools we want to run and their respective arguments.
# Note: "-c 4" sends 4 packets on Linux/Mac. If you are on Windows, change "-c" to "-n".
TOOLS = {
    "ping": ["ping", "-c", "4", "8.8.8.8"], 
    "netstat": ["netstat", "-an"], 
    "nmap": ["nmap", "-F", "127.0.0.1"]
}

print("Scanning system and running network tools...")

# Open the report file in write mode
with open("tool_report.txt", "w") as report:
    for name, cmd in TOOLS.items():
        report.write(f"\n===== {name.upper()} =====\n")
        
        # 1. Verification Step: Check if the tool is actually installed on the computer
        if shutil.which(cmd[0]) is None:
            report.write(f"Skipped: '{name}' tool is not installed on this system.\n")
            print(f"[-] {name} is not installed. Skipping...")
            continue
        
        print(f"[+] Running {name}...")
        try:
            # 2. Execution Step: Safely execute the system command
            # capture_output=True grabs both stdout and stderr so we can write them to our file
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
            
            # Write whatever the tool outputted (or any errors it ran into)
            report.write(result.stdout or result.stderr)
            
        except subprocess.TimeoutExpired:
            report.write(f"Error: Command execution timed out after 15 seconds.\n")
        except Exception as e:
            report.write(f"An unexpected error occurred: {str(e)}\n")

print("\nTask complete! Tool report saved as 'tool_report.txt'.")