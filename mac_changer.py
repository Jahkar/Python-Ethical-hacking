#!/usr/bin/env python

import subprocess
import optparse

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


options = get_arguments()
change_mac(options.interface, options.new_mac)

# here we are utilizing our own defined function(s) in our mac address changer program.
# The purpose of this program is to change the mac address
# through the terminal, while taking user input and displaying options. We achieved this through importing
# 2 modules ( subprocess and optparse ) The first of the modules is subprocess which allows us to spawn new processes
# And the 2nd being optparse which allows us to parse commandlines in the terminal.
# We also are checking for user error(s) by implementing if else statements and then returning the value of user input
# which is the varaible named options.