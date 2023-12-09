import socket
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import time
import shutil
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime
import smtplib
import subprocess
import subprocess
import threading
import shutil
import colorsys

def run_java_program():
    try:
        # Your code for running the Java program
        java_command = ["java", "PremiumPop"]
        output = subprocess.check_output(java_command, stderr=subprocess.STDOUT, text=True)
        print(output)
    except subprocess.CalledProcessError as e:
        print("Error:", e.output)
    except Exception as e:
        print("An error occurred:", str(e))
# Function to convert HSV to RGB
hsv_to_rgb = lambda h, s, v: tuple(int(c * 255) for c in colorsys.hsv_to_rgb(h, s, v))
YELLOW = "\033[94m"
RESET = "\033[0m"
# Your ASCII art
ascii_art = '''
                                                                                                                                                                           
                                                                                                                                                                           
                                                                                                                                                                           
                                                                                                                                                                           
                                                                                                                                                                           
 /$$$$$$$$                                     /$$$$$$$                            /$$$$$$$             /$$$$$$                          /$$                              
|_____ $$                                     | $$__  $$                          | $$__  $$           /$$__  $$                        | $$                              
     /$$/   /$$$$$$   /$$$$$$   /$$$$$$       | $$  \ $$  /$$$$$$  /$$   /$$      | $$  \ $$  /$$$$$$ | $$  \__//$$$$$$  /$$$$$$$   /$$$$$$$  /$$$$$$   /$$$$$$   /$$$$$$$
    /$$/   /$$__  $$ /$$__  $$ /$$__  $$      | $$  | $$ |____  $$| $$  | $$      | $$  | $$ /$$__  $$| $$$$   /$$__  $$| $$__  $$ /$$__  $$ /$$__  $$ /$$__  $$ /$$_____/
   /$$/   | $$$$$$$$| $$  \__/| $$  \ $$      | $$  | $$  /$$$$$$$| $$  | $$      | $$  | $$| $$$$$$$$| $$_/  | $$$$$$$$| $$  \ $$| $$  | $$| $$$$$$$$| $$  \__/|  $$$$$$ 
  /$$/    | $$_____/| $$      | $$  | $$      | $$  | $$ /$$__  $$| $$  | $$      | $$  | $$| $$_____/| $$    | $$_____/| $$  | $$| $$  | $$| $$_____/| $$       \____  $$
 /$$$$$$$$|  $$$$$$$| $$      |  $$$$$$/      | $$$$$$$/|  $$$$$$$|  $$$$$$$      | $$$$$$$/|  $$$$$$$| $$    |  $$$$$$$| $$  | $$|  $$$$$$$|  $$$$$$$| $$       /$$$$$$$/
|________/ \_______/|__/       \______/       |_______/  \_______/ \____  $$      |_______/  \_______/|__/     \_______/|__/  |__/ \_______/ \_______/|__/      |_______/ 
                                                                   /$$  | $$                                                                                              
                                                                  |  $$$$$$/                                                                                              
                                                                   \______/                                                                                              
                                                                                                                                                                         
                                                                                                                                                                          
                                                                                                                                                                          
                                                                                                                                                                           
                                                                                                                                                                          
                                                                                                                                                                           
                                                                                                                                                                       '''

# Your yellow lock image with labels
image = f"""{YELLOW}
                    .-=+**+=-:.                   
             .:-+*##############*+=-:.            
        -=+############################*=-.       
       :##################################=       
       :###############*++*###############=       
       :############*-.     -*############=       
       :###########*. =*###+. +###########=       
       :###########- =######+ .###########=       
       :##########*- =******+ .*##########=       
       :########=                -########=       
        ########:    Firewall     ########:       
        *#######:    Network      #######*        
        =#######:    System       #######*        
         #######:     Router      ######=         
          =#####-                 #####*          
           =####*=---------------*####*           
            -########################=            
             .+####################*:             
               :*#################-               
                 -*#############=                 
                   .=*#######+:                   
                      .-++=:                      
{RESET}"""

# Define premium colors (in HSV format)
colors = [
    (0.0, 1.0, 1.0),   # Red
    (0.08, 1.0, 1.0),  # Orange
    (0.16, 1.0, 1.0),  # Yellow
    (0.32, 1.0, 1.0),  # Green
    (0.48, 1.0, 1.0),  # Cyan
    (0.64, 1.0, 1.0),  # Blue
    (0.72, 1.0, 1.0),  # Purple
]

# Split the ASCII art and the image into lines
ascii_lines = ascii_art.split('\n')
image_lines = image.split('\n')

# Determine the maximum number of lines between the ASCII art and the image
max_lines = max(len(ascii_lines), len(image_lines))

# Print colorful text line by line using premium colors with a UI-friendly look, alternating between ASCII art and image
for i in range(max_lines):
    # Determine the color index based on the line number
    color_idx = i % len(colors)
    hue, saturation, value = colors[color_idx]
    r, g, b = hsv_to_rgb(hue, saturation, value)
    
    # Print ASCII art line
    if i < len(ascii_lines):
        colored_ascii_line = f"\033[38;2;{r};{g};{b}m{ascii_lines[i]}\033[0m".ljust(80)
        print(colored_ascii_line, end='')

    # Print image line
    if i < len(image_lines):
        
        colored_image_line = f"\033[38;2;0;0;255m{image_lines[i]}\033[0m".rjust(80)
        print(colored_image_line)

    time.sleep(0.1) 

# Specify the file path to your NSL-KDD dataset text file
train_dataset_file = r"/home/batman/Downloads/updated_dataset.txt"

# Read the training text file without specifying column names
train = pd.read_csv(train_dataset_file, delimiter=",", header=None)
column_names = ["SPort", "DPort", "SPkts", "DPkts", "SBytes", "DBytes", "Protocol", "SYN", "ACK", "FIN", "PSH", "RST", "URG", "SYN+ACK", "Duration", "IsAlive", "Service", "UniqueDests", "UniqueSrcs", "UniqueDestSocks", "UniqueSrcSocks", "attack"]
column_names2 = ["SPort", "DPort", "SPkts", "DPkts", "SBytes", "DBytes", "Protocol", "SYN", "ACK", "FIN", "PSH", "RST", "URG", "SYN+ACK", "Duration", "IsAlive", "Service", "UniqueDests", "UniqueSrcs", "UniqueDestSocks", "UniqueSrcSocks"]
train.columns = column_names
X_train = train.drop(train.columns[-1], axis=1)
y1_train = train[train.columns[-1]]

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the receiver's address and port
receiver_address = ('10.0.2.15', 12345)
s.bind(receiver_address)
s.listen(1)

# Define ANSI escape codes for colors
color_red = "\033[91m"
color_reset = "\033[0m"

# Text to print
text = "                                                                            Hello, This is Zero Day Defenders AI Tool. Now, I am starting to monitor."

# Add red color to the text
colored_text = f"{color_red}{text}{color_reset}"

# Print the colored text
print(colored_text)


while True:
    # Listen for incoming connections
    connection, sender_address = s.accept()
    print("Data is coming......")

    # Specify where to save the received file
    received_file_path = 'new2.txt'

    # Receive and save the file data
    with open(received_file_path, 'wb') as file:
        while True:
            data = connection.recv(1024)
            if not data:
                break
            file.write(data)

    # Read the test text file without specifying column names
    test_dataset_file = r"/home/batman/new2.txt"
    test = pd.read_csv(test_dataset_file, delimiter=",", header=None)
    # Remove 'attack_type' and 'label' from test data
    test.columns = column_names2

    # Separate the features (X) and the target labels (y1 for attack_type)
    X_train = train.drop(train.columns[-1], axis=1)
    y1_train = train[train.columns[-1]]

    X_test = test

    # Perform one-hot encoding on the categorical features
    X_train_encoded = pd.get_dummies(X_train)
    X_test_encoded = pd.get_dummies(X_test)

    # Ensure that the columns in X_test_encoded are in the same order as X_train_encoded
    X_test_encoded = X_test_encoded.reindex(columns=X_train_encoded.columns, fill_value=0)

    # Create a Random Forest Classifier for y1 (attack_type)
    clf1 = RandomForestClassifier()
    clf1.fit(X_train_encoded, y1_train)

    # Make predictions on the test data for y1 (attack_type)
    y1_pred = clf1.predict(X_test_encoded)

 
    # Text to print
    text = "                                                                        --------------Detecting Real Time Data--------------"

    # Add red color to the text
    colored_text = f"{color_red}{text}{color_reset}"

    # Print the colored text
    print(colored_text)

    for i in y1_pred:
        time.sleep(1)
        if i == 0:
            print("                                                                               normal")
        elif i == 1:
            print("                                                                               System")
            java_thread=threading.Thread(target=run_java_program)
            java_thread.start()
            current_time = datetime.datetime.now()

            # Format and print the current time
            formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

            Recipients_Name = "Hemanth"

            # Email configuration
            smtp_server = 'smtp.gmail.com'
            smtp_port = 587
            smtp_username = 'hemanthgangula7@gmail.com'
            smtp_password = 'pijl gwny iurf ytfy'
            sender_email = 'hemanthgangula7@gmail.com'
            receiver_email = 'dattuajay005@gmail.com'
            subject = '⚠️Cyber Pulse Alert - Network Intrusion Detected'

            # Define the attack_type
            attack_type = 'System Attack'  # Replace with the actual attack type

            # Create the message content
            message = f'''
            <html>
            <head></head>
            <body>
            <p>Dear {Recipients_Name},</p>

            <p>I hope this message finds you well. We would like to inform you that our Network Intrusion Detection System, "</b>Cyber Pulse</b>," has detected a security incident on our network. Please find the details of the incident below:</p>

            <b>Incident Details:</b>
            <ul>
                <li><b>Attack Type:</b> {attack_type}</li>
                <li><b>Date and Time:</b> {formatted_time}</li>
                <li><b>Source IP:</b> 10.0.2.15</li>
                <li><b>Destination IP:</b> 10.0.2.4</li>
                <li><b>Description:</b> Isolate your network</li>
            </ul>

            <b>Precautions Taken:</b>
            <p>Upon detection of this incident, "Cyber Pulse" has automatically initiated the following precautions to mitigate any potential risks:</p>
            <ul>
                <li>Isolated affected systems from the network.</li>
                <li>Conducted a thorough investigation to assess the extent of the intrusion.</li>
                <li>Patched any vulnerabilities that may have been exploited.</li>
                <li>Enhanced monitoring and security measures to prevent future occurrences.</li>
            </ul>

            <b>Recommendations:</b>
            <p>In light of this incident, we strongly recommend the following actions for all users:</p>
            <ul>
                <li>Change your passwords immediately.</li>
                <li>Ensure that all systems and software are up-to-date with the latest security patches.</li>
                <li>Exercise caution with suspicious emails, links, or attachments.</li>
                <li>Report any unusual or suspicious activity to our IT Security team promptly.</li>
            </ul>

            <p>Our team is actively working to address this incident, and we will keep you updated on any developments. If you have any questions or concerns, please do not hesitate to reach out to our IT Security team at <a href="https://hemanthtechlearn.blogspot.com/">Cyber Pulse</a>.</p>

            <p>"Cyber Pulse" is dedicated to your security, and we are committed to maintaining a safe and secure network environment. Thank you for your cooperation and vigilance.</p>

            <p>Best regards,</p>
            <p>Cyber Pulse<br>Zero Day Defenders</p>
            <p>SRKR ENGINEERING COLLEGE<br>zerodaydefenders@cyberpulse.com<br>zerodaydefenders@cyberpulse.com</P>
            <p></p>
            </body>
            </html>
            '''

            # Create a message object
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = receiver_email
            msg['Subject'] = subject

            # Attach the message body as HTML
            msg.attach(MIMEText(message, 'html'))

            try:
                # Connect to Gmail's SMTP server
                server = smtplib.SMTP(smtp_server, smtp_port)
                server.starttls()

                # Login to your Gmail account
                server.login(smtp_username, smtp_password)

                # Send the email
                server.sendmail(sender_email, receiver_email.split(','), msg.as_string())

                # Close the connection
                server.quit()

                print("                                                                                        Warning---->Email sent successfully!")
            except Exception as e:
                print(f"Email sending failed. Error: {str(e)}")
        elif i == 2:
            print("Router")
            try:
                java_command = ["java", "PremiumPopup"]
                # Execute the Java command and capture the output
                output = subprocess.check_output(java_command, stderr=subprocess.STDOUT, text=True)

                # Print the output of the Java program
                print(output)

            except subprocess.CalledProcessError as e:
                # Handle any errors that occur during execution
                print("Error:", e.output)

            except Exception as e:
                # Handle other exceptions
                print("An error occurred:", str(e))
            current_time = datetime.datetime.now()

            # Format and print the current time
            formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

            Recipients_Name = "Hemanth"

            # Email configuration
            smtp_server = 'smtp.gmail.com'
            smtp_port = 587
            smtp_username = 'hemanthgangula7@gmail.com'
            smtp_password = 'pijl gwny iurf ytfy'
            sender_email = 'hemanthgangula7@gmail.com'
            receiver_email = 'dattuajay005@gmail.com'
            subject = '⚠️Cyber Pulse Alert - Network Intrusion Detected'

            # Define the attack_type
            attack_type = 'Network Attack'  # Replace with the actual attack type

            # Create the message content
            message = f'''
            <html>
            <head></head>
            <body>
            <p>Dear {Recipients_Name},</p>

            <p>I hope this message finds you well. We would like to inform you that our Network Intrusion Detection System, "</b>Cyber Pulse</b>," has detected a security incident on our network. Please find the details of the incident below:</p>

            <b>Incident Details:</b>
            <ul>
                <li><b>Attack Type:</b> {attack_type}</li>
                <li><b>Date and Time:</b> {formatted_time}</li>
                <li><b>Source IP:</b> 10.0.2.15</li>
                <li><b>Destination IP:</b> 10.0.2.4</li>
                <li><b>Description:</b> Isolate your network</li>
            </ul>

            <b>Precautions Taken:</b>
            <p>Upon detection of this incident, "Cyber Pulse" has automatically initiated the following precautions to mitigate any potential risks:</p>
            <ul>
                <li>Isolated affected systems from the network.</li>
                <li>Conducted a thorough investigation to assess the extent of the intrusion.</li>
                <li>Patched any vulnerabilities that may have been exploited.</li>
                <li>Enhanced monitoring and security measures to prevent future occurrences.</li>
            </ul>

            <b>Recommendations:</b>
            <p>In light of this incident, we strongly recommend the following actions for all users:</p>
            <ul>
                <li>Change your passwords immediately.</li>
                <li>Ensure that all systems and software are up-to-date with the latest security patches.</li>
                <li>Exercise caution with suspicious emails, links, or attachments.</li>
                <li>Report any unusual or suspicious activity to our IT Security team promptly.</li>
            </ul>

            <p>Our team is actively working to address this incident, and we will keep you updated on any developments. If you have any questions or concerns, please do not hesitate to reach out to our IT Security team at <a href="https://hemanthtechlearn.blogspot.com/">Cyber Pulse</a>.</p>

            <p>"Cyber Pulse" is dedicated to your security, and we are committed to maintaining a safe and secure network environment. Thank you for your cooperation and vigilance.</p>

            <p>Best regards,</p>
            <p>Cyber Pulse<br>Zero Day Defenders</p>
            <p>SRKR ENGINEERING COLLEGE<br>zerodaydefenders@cyberpulse.com<br>zerodaydefenders@cyberpulse.com</P>
            <p></p>
            </body>
            </html>
            '''

            # Create a message object
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = receiver_email
            msg['Subject'] = subject

            # Attach the message body as HTML
            msg.attach(MIMEText(message, 'html'))

            try:
                # Connect to Gmail's SMTP server
                server = smtplib.SMTP(smtp_server, smtp_port)
                server.starttls()

                # Login to your Gmail account
                server.login(smtp_username, smtp_password)

                # Send the email
                server.sendmail(sender_email, receiver_email.split(','), msg.as_string())

                # Close the connection
                server.quit()

                print("Email sent successfully!")
            except Exception as e:
                print(f"Email sending failed. Error: {str(e)}")
        elif i == 3:
            print("firewall")
        elif i == 4:
            print("router")

connection.close()

s.close()
