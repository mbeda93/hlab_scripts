# hlab_scripts

Assortment of scripts to automate my hosted apps. 
Written specifically for my setup, but can be easily changed to suit your needs (assuming you're on a Linux system). These are intended to be used as part of automations powered by n8n, but can just as easily be used as any other script.

  

## ipc_auth.py

A simple script to automate the reauthentication of a Tuya account on a running ```tuya-ipc-terminal``` instance, Reauthenticates and restarts the local RTSP streams when they drop out due to expired auth token.

  

### Requirements

* Linux

* Python3

* A functional instance of tuya-ipc-terminal, installed as a systemd service 
  * Setup here: (https://github.com/seydx/tuya-ipc-terminal)
  * Running at port 8555 for my purpose, but can be changed to suit your setup

* pexpect (can be installed using "pip3 install pexpect")

  

### Setup (one time)

* Set your password:
  * In the same directory as the script...
    * Pass ``cat YourPassword > .ipc_secret`` on the command line
      * This will not go anywhere online, will stay on the system.
      * This will eventually move into  a single file with all the user-needed data

* More configuration (Within the python file itself)...
  * Set your Tuya region according to your account

  * Set the email in use for your Tuya account
 
  * Set the datacenter location according to your account
### Usage
* Run ```./ipc_fix.py```  (you might need to ```chmod +x ./ipc_fix.py``` depending on your system)
* That's it.
    * n8n simply uses its ssh node in an automation to call upon these the same as a user would at the terminal, so nothing too fancy there.