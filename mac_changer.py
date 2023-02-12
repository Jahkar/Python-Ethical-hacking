#!/usr/bin/env python

import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC address")
    parser.add_option("-m", "--new_mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please enter and specify the interface, use --help for more info.")
    elif not options.new_mac:
        parser.error("[-] Please enter and specify new MAC, use --help for more info.")
    return options

def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def display_current_mac_address(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Error could not read the MAC address.")

options = get_arguments()

current_mac = display_current_mac_address(options.interface)

print("Current MAC: " + str(current_mac))

change_mac(options.interface, options.new_mac)

current_mac = display_current_mac_address(options.interface)
if current_mac == options.new_mac:
    print("[+] MAC address was changed to: " + str(current_mac))
else:
    print("[-] MAC address did not get changed.")






# here we are utilizing our own defined function(s) in our mac address changer program.
# The purpose of this program is to change the mac address
# through the terminal, while taking user input and displaying options and
# displaying the changed values. We achieved this through importing
# 3 modules ( subprocess, optparse, and re ( regular expressions ) )
# The first of the modules is subprocess which allows us to spawn new processes
# And the 2nd being optparse which allows us to parse commandlines in the terminal.
# And 3rd, re which is our regular expression.
# Allows us to set rules to match a pattern in the text box of the ifconfig or any large texts.
# And only displays the changed variable ( MAC address ).
# We also are checking for user error(s) by implementing if else statements and then returning the value of user input
# which is the varaible named options.

# 1. We import the subprocess module, which allows us to run commands on the command line.
# 2. We import the optparse module, which allows us to create a command line interface.
# 3. We import the re module, which allows us to use regular expressions.
# 4. We create a function called get_arguments() that will parse the command line arguments.
# 5. We create a function called change_mac() that will change the MAC address.
# 6. We create a function called display_current_mac_address() that will display the current MAC address.
# 7. We create a variable called options that will store the command line arguments.
# 8. We create a variable called current_mac that will store the current MAC address.
# 9. We print the current MAC address.
# 10. We call the change_mac() function to change the MAC address.
# 11. We create a variable called current_mac that will store the current MAC address.
# 12. We check if the current MAC address is the same as the new MAC address.
# 13. We print the current MAC address.
