# papirus-netapp
A Network appliance for the PaPiRus from PiSupply

I have now cleaned up some of the code.

Recent Changes (7th October 2017)

1) Added code to fetch the runtime path, now you can run this from a directory of your choosing.
2) Fixed some of the display code so it looks a little better when running
3) Added install.sh - So you can now clone the repo and run sudo ./install.sh to get all the python libraries installed 


------
# Using this App
1) Clone the repository
2) Install the pre-requisits
2.1) You can now sudo ./install.sh to install everything you need on the Raspberry Pi.
3) Run python main.py

This assumes that you have already installed all the PaPiRus bits and have the screen working on your Raspberry Pi.


-----
# Required Software

sudo apt-get install python-matplotlib python-nmap

sudo pip install matplotlib

sudo pip install gpiozero

sudo pip install speedtest-cli

sudo pip install ipgetter

sudo pip install statistics

sudo pip install ascii_graph

sudo pip install pexpect

sudo pip install nmap

sudo pip install matplotlib

