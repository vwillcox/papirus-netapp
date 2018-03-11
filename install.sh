#!/usr/bin/env bash
# Network Testing Appliance
# Uses the speedtest.net servers and SpeedTest-CLI
# SpeedTest-cli by Matt Martz

# Version 2 PaPiRus  NetApp
# Installer Script (run as root/sudo please)

if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root"
   exit 1
fi
  function pause(){
   read -p "$*"
}

echo "Welcome to The PaPiRus Netapp Appliance Installer"
pause 'Press [Enter] to install the required bits and pieces or CTRL+C to stop...'
echo "Installing mpack zip ssmtp mailutils mpack python-pip python3-pip python-w1thermsensor python3-w1thermsensor python-spidev python3-spidev nmap"
apt-get update
apt-get install python-pip python3-pip python-w1thermsensor python3-w1thermsensor python-spidev python3-spidev nmap -y 2>&1 >/dev/null
if [ "$?" -ne 0 ]; then
  echo "Error while running apt-get (maybe run apt-get update?)";
  exit 1;
fi
echo "Done"
echo "Now installing python modules"
pip install -r requirements.txt
pip3 install -r requirements.txt

echo "All done! Enjoy"
