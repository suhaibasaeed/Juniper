from netmiko import ConnectHandler # For interacting with Juniper devices
from getpass import getpass # For avoiding putting clear-text password in python file

username = 'implement'
password = getpass() # Get password from the user

print('-' * 50)
print('Juniper Devices')
print('-' * 50)

with open("juniperdevices.txt") as fp:
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
        # Find prompt of device - will be used  later in verification step
        prompt = net_connection.find_prompt()
        # Send command to request device to shutdown
        output = net_connection.send_command_timing('request system power-off')
        # If we see device asking for confirmation to shutdown say yes
        if 'Power Off' in output:
            output += net_connection.send_command_timing('yes')
        else: # Otherwise there is an error and print this to screen
            raise ValueError("Expected Power Off confirm message in output")
        # If we receive confirmation from device that it's shutting down print to screen
        if 'System shutdown' in output:
            print(prompt + ' was successfully powered off')
        else: # If we don't get confirmation then inform user by printing to screen
            print(prompt + ' was not shutdown')
