import logging
import json
from datetime import datetime

# Configure the logging module
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s [%(levelname)s] - %(message)s',
                    filename='attack_history.log')

# File to store attack details in JSON format
json_file_path = 'attack_history.json'

# Function to log attack details and store in JSON file
def log_attack_details(attack_type, source_ip):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"Attack Type: {attack_type}, Source IP: {source_ip}, Timestamp: {timestamp}"
    logging.warning(log_message)

    # Load existing data from JSON file or create an empty list
    try:
        with open(json_file_path, 'r') as json_file:
            attack_history = json.load(json_file)
    except FileNotFoundError:
        attack_history = []

    # Append new attack details to the list
    attack_history.append({
        'attack_type': attack_type,
        'source_ip': source_ip,
        'timestamp': timestamp
    })

    # Write the updated list back to the JSON file
    with open(json_file_path, 'w') as json_file:
        json.dump(attack_history, json_file, indent=2)

# Example of logging an attack event
if __name__ == "__main__":
    # Simulate an attack event
    attack_type = "SQL Injection"
    attacker_ip = "192.168.1.101"
    log_attack_details(attack_type, attacker_ip)
