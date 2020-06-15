from netmiko import ConnectHandler # For interacting with Juniper devices
from getpass import getpass # For avoiding putting clear-text password in python file
from tcping import Ping # For sending ping to non-netmiko supported device i.e. TC opengear


username = 'implement'
password = getpass() # Get password from the user

print('-' * 50)
print('Juniper Devices')
print('-' * 50)

with open("myfile.txt") as fp: 
    ips = fp.readlines() 
    for ip in ips: # Loop through textfile with IPs in it

        # Dictionary that hold the device details
        junos_device = {
            'host': ip,
            'username': username,
            'password': password,
            'device_type': 'juniper_junos',
        }
        
        # Establish SSH connection to the network device using **kwargs to pull in details from dictionary
        net_connection = ConnectHandler(**junos_device)
        # Find the prompt of the device
        output = net_connection.find_prompt()
        # Print out prompt for each device
        print(output + ' is powered on')


print('-' * 50)
print('TC Device')
# Send single ping to device
tc1 = Ping('1.1.1.1', 22, 60)
result = tc1.ping(1)
# If successful print to console & vice versa
if result == None: 
    print('device is powered on')
else:
    print('device is powered off')
