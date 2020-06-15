# Juniper
Python scripts for Juniper Devices. 
1.  powerdown.py

This script will power down Juniper devices which are listed by IP address or domain name in a text file called juniperdevices.txt

Please note that the text file needs to be in the same directory/folder for the script to successfully execute.
The sequence of devices that are powered down can be changed by changing where the IP address is located in the text file.
e.g. If 192.168.1.1 is the 1st IP address in the text file then this will the 1st device to be powered down.
An example of the text file has been included for illustration purposes

2.  poweruptest.py

This script will check where a list of devices are powered on and responsive. This list is taken from the text file called myfile.txt

Please note that the text file needs to be in the same directory/folder for the script to successfully execute.
This script works by logging onto the devices and printing the prompt to the screen.
