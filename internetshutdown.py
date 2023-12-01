import subprocess
import platform
import time

def disconnect_internet():
    system_platform = platform.system()

    if system_platform == "Windows":
        # Disconnect Wi-Fi on Windows
        subprocess.run(["netsh", "interface", "set", "interface", "Wi-Fi", "admin=disable"], capture_output=True)

    elif system_platform == "Linux":
        # Disconnect Wi-Fi on Linux
        subprocess.run(["sudo", "ifconfig", "wlan0", "down"], capture_output=True)

    elif system_platform == "Darwin":
        # Disconnect Wi-Fi on macOS
        subprocess.run(["sudo", "ifconfig", "en0", "down"], capture_output=True)

    else:
        print("Unsupported operating system")

def reconnect_internet():
    system_platform = platform.system()
    
    if system_platform == "Windows":
        # Disconnect Wi-Fi on Windows
        subprocess.run(["netsh", "interface", "set", "interface", "Wi-Fi", "admin=enable"], capture_output=True)

    elif system_platform == "Linux":
        # Disconnect Wi-Fi on Linux
        subprocess.run(["sudo", "ifconfig", "wlan0", "up"], capture_output=True)

    elif system_platform == "Darwin":
        # Disconnect Wi-Fi on macOS
        subprocess.run(["sudo", "ifconfig", "en0", "up"], capture_output=True)

    else:
        print("Unsupported operating system")
   
    
    
if __name__ == "__main__":
    print("Disconnecting internet. Please wait...")
    disconnect_internet()
    time.sleep(5)  # Wait for 5 seconds to simulate a disconnection
    print("Reconnecting internet...")
    # You may add code here to reconnect the internet if needed
    reconnect_internet()
