import subprocess
import platform
import time

def internet_shutdown():
    def execute_command(command):
        subprocess.run(command, capture_output=True)

    system_platform = platform.system()

    if system_platform == "Windows":
        # Disconnect Wi-Fi on Windows
        execute_command(["netsh", "interface", "set", "interface", "Wi-Fi", "admin=disable"])

        # Reconnect Wi-Fi on Windows
        execute_command(["netsh", "interface", "set", "interface", "Wi-Fi", "admin=enable"])

    elif system_platform == "Linux":
        # Disconnect Wi-Fi on Linux
        execute_command(["sudo", "ifconfig", "wlan0", "down"])

        # Reconnect Wi-Fi on Linux
        execute_command(["sudo", "ifconfig", "wlan0", "up"])

    elif system_platform == "Darwin":
        # Disconnect Wi-Fi on macOS
        execute_command(["sudo", "ifconfig", "en0", "down"])

        # Reconnect Wi-Fi on macOS
        execute_command(["sudo", "ifconfig", "en0", "up"])

    else:
        print("Unsupported operating system")

if __name__ == "__main__":
    print("Disconnecting internet. Please wait...")
    internet_shutdown()
    time.sleep(5)  # Wait for 5 seconds to simulate a disconnection
    print("Reconnecting internet...")
    # You may add code here to perform additional actions after reconnecting if needed
