import requests
import pandas as pd

# Replace 'YOUR_EC2_PUBLIC_IP' with the actual public IP address of your EC2 instance
server_ip = 'YOUR_EC2_PUBLIC_IP'
server_port = 5000

url = f'http://{server_ip}:{server_port}/predict'

# Sample DataFrame for testing
ses_info_dict = {
    'SPort': 443,
    'DPort': 49718,
    'SPkts': 2,
    'DPkts': 0,
    'SBytes': 138,
    'DBytes': 0,
    'Protocol': 6,
    'SYN': 0,
    'ACK': 2,
    'FIN': 0,
    'PSH': 1,
    'RST': 0,
    'URG': 0,
    'SYN+ACK': 2,
    'Duration': 1.446675062,
    'IsAlive': 1,
    'Service': 0,
    'UniqueDests': 1,
    'UniqueSrcs': 1,
    'UniqueDestSocks': 1,
    'UniqueSrcSocks': 1,
}

# Remove 'target' from the dictionary
ses_info_dict.pop('target', None)

# Convert the dictionary to a DataFrame
df = pd.DataFrame([ses_info_dict])

# Specify the correct order of feature names based on your dataset
correct_feature_names = [
    'SPort', 'DPort', 'SPkts', 'DPkts', 'SBytes', 'DBytes', 'Protocol',
    'SYN', 'ACK', 'FIN', 'PSH', 'RST', 'URG', 'SYN+ACK', 'Duration',
    'IsAlive', 'Service', 'UniqueDests', 'UniqueSrcs', 'UniqueDestSocks', 'UniqueSrcSocks'
]

# Reorder the columns in the DataFrame
df = df[correct_feature_names]

# Convert the DataFrame to JSON without index
data = df.to_json(orient='records', lines=True)

# Send a POST request with the JSON data
response = requests.post(url, data=data, headers={'Content-Type': 'application/json'})

# Check if 'prediction' key is present
if 'prediction' in response.json():
    # Print the prediction result
    print(response.json()['prediction'])
else:
    print("Error: 'prediction' key not found in the response.")