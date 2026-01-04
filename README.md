# hlab_scripts
Assortment of scripts to automate my hosted apps.

# ipc_auth
A simple script to automate the reauthentication of the Tuya accound, when streams occasionally drop, and restarting the service is ineffective.

## Requirements
* Linux
* Python3
* A functional instance of tuya-ipc-terminal, installed as a systemd service (https://github.com/seydx/tuya-ipc-terminal)
* * Running at port 8555 for my purpose, can be changed to suit your setup
* pexpect (can be installed using "pip3 install pexpect")

## Usage
* Set your password:
* * In your home direct
* Within the python file itself (in the configuration section)...
* * Set your Tuya region according to your account
* * Set the email in use for your Tuya account
* * Set the datacenter location according to your account
