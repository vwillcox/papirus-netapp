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
 
function pip_install {
   local package_name=$1
   echo "Installing $package_name"
   pip install $package_name 2>&1 >/dev/null
   pip3 install $package_name 2>&1 >/dev/null
}

echo "Welcome to The PaPiRus Netapp Appliance Installer"
pause 'Press [Enter] to install the required bits and pieces or CTRL+C to stop...'
echo "Installing mpack zip ssmtp mailutils mpack python-pip python3-pip python-w1thermsensor python3-w1thermsensor python-spidev python3-spidev"
apt-get update
apt-get install python-pip python3-pip python-w1thermsensor python3-w1thermsensor python-spidev python3-spidev -y 2>&1 >/dev/null
if [ "$?" -ne 0 ]; then
  echo "Error while running apt-get (maybe run apt-get update?)";
  exit 1;
fi
echo "Done"
echo "Now installing python modules"
pip_install gpiozero
pip_install speedtest-cli
pip_install ipgetter
pip_install statistics
pip_install ascii_graph
pip_install pexpect
pip_install nmap
pip_install matplotlib
pip_install pyotp

echo "All done! Enjoy"
