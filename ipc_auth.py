#!/usr/bin/env python3
import pexpect
import os
import sys
import time
import subprocess

###Adjust the following config variables as needed###
### Store your password in a local .ipc_secret file ###
###hint: echo "yourpassword" > .ipc_secret ###

# --- CONFIGURATION ---
SERVICE_NAME = "tuya-rtsp"
REGION = 'us-west'
EMAIL = 'yourtuyaemail@example.com'
CMD = f"/usr/local/bin/tuya-ipc-terminal auth refresh {REGION} {EMAIL} --password"
# Ensure this file exists with your password inside
SECRETS_FILE = os.path.join(os.path.dirname(__file__), '.ipc_secret')
# ---END CONFIGURATION---

def get_password():
    '''Grab the password, store in a variable for later use'''
    try:
        with open(SECRETS_FILE, 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        print(f"Error: Missing .ipc_secret file at {SECRETS_FILE}")
        sys.exit(1)

def auth():
    '''
    Automates the authentication process for the tuya-ipc-terminal tool.
    Depends on the password being stored in a local .ipc_secret file
    '''
    password = get_password()
    
    # 1. STOP THE SERVICE
    print(f"Stopping {SERVICE_NAME}...")
    subprocess.run(["sudo", "systemctl", "stop", SERVICE_NAME])
    time.sleep(2)

    # 2. PERFORM INTERACTIVE LOGIN
    child = pexpect.spawn(CMD, encoding='utf-8')
    
    # Look for the prompt
    index = child.expect(['Code:', 'Enter password: ', pexpect.TIMEOUT], timeout=30)
    
    if index == 0 or index == 1:
        print("Prompt detected. Sending password...")
        child.sendline(password)
        # Wait for login to complete (adjust string if you know the success message)
        time.sleep(5) 
        child.close() # Close the interactive session
        print("Login sequence finished.")
    else:
        print("Timeout: No password prompt appeared. Are we already logged in?")
        child.close()

    # 3. RESTART THE SERVICE
    print(f"Restarting {SERVICE_NAME}...")
    subprocess.run(["sudo", "systemctl", "start", SERVICE_NAME])
    print("Service restarted.")

if __name__ == "__main__":
    auth()