#!/usr/bin/python

import RPi.GPIO as GPIO
from getip import get_lan_ip
from papirus import PapirusTextPos
import ipgetter, subprocess, shlex, os
from PIL import ImageFont
import ImageDemo, scan4pi
from time import sleep
import pyotp
from datetime import datetime

button1 = 16
button2 = 26
button3 = 20
button4 = 21

#your Google OTP Code
google = "YOUCODEHERE"
#Your Other code
lastpass = "YOURCODEHERE"
# add any more here

# Set them as Time Based One Time Passcodes
Googleotp = pyotp.TOTP(google)
lastpassotp = pyotp.TOTP(lastpass)


def show_menu():
	screen.Clear()
	screen.AddText("Main Menu", 10, 10)
	screen.AddText("1) Advanced Menu", 10, 40)
	screen.AddText("2) Scan 4 Pi's", 10, 70)
	screen.AddText("3) Speed Graph", 10, 100)
	screen.AddText("4) Speed Test", 10, 130)
	screen.WriteAll()

def show_menu_2():
        screen.Clear()
        screen.AddText("Advanced Menu", 10, 10)
        screen.AddText("1) Main Menu", 10, 40)
        screen.AddText("2) Power Off Pi", 10, 70)
        screen.AddText("3) Show OTP's", 10, 100)
        screen.WriteAll()


def show_otp():
	timestamp = datetime.now().strftime('%H:%M:%S')
	screen.Clear()
	screen.AddText("Your OTP's are:", 10, 10, size2)
	screen.AddText("Generated at: " + timestamp, 10, 40, size2)
	screen.AddText("vincent@willcox.tk: " + Googleotp.now(), 10, 70, size1)
	screen.AddText("LastPass is now: " + lastpassotp.now(), 10, 100, size1)
	screen.WriteAll()

def speed_test():
	screen.Clear()
	screen.AddText("Running Speedtest now", 20, 70, size2)
        screen.WriteAll()
        subprocess.call(shlex.split(speed_test_code))
        screen.Clear()
        f = open(speed_test_log)
        lines = f.readlines()
        f.close()
        speedline1 = lines[-5].strip()
        speedline2 = lines[-4].strip()
        speedline3 = lines[-3].strip()
        speedline4 = lines[-2].strip()
        screen.AddText(speedline1, 5, 5, size1)
        screen.AddText(speedline2, 10, 35, size2)
        screen.AddText(speedline3, 10, 65, size2)
        screen.AddText(speedline4, 10, 95, size2)
        screen.AddText(ext_ip, 10, 125, size2)
        screen.AddText(int_ip, 10, 155, size2)
        screen.WriteAll()

def graph_it():
	ImageDemo.main('temp.png')

def scan4it():
	scan4pi.main()

def reboot_it():
	screen.Clear()
        screen.AddText("Rebooting", 20, 70, size2)
        screen.WriteAll()
	sleep(2)
	screen.Clear()
	os.system('sudo shutdown -r now')

def power_off():
        screen.Clear()
        screen.AddText("Shutting Down", 20, 70, size2)
        screen.WriteAll()
        sleep(2)
        screen.Clear()
	os.system('sudo shutdown now')


if "__main__" == __name__:
	possible_fonts = [
        '/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf',            # R.Pi
        '/usr/share/fonts/truetype/ttf-dejavu/DejaVuSansMono-Bold.ttf',   # R.Pi
        '/usr/share/fonts/truetype/freefont/FreeMono.ttf',                # R.Pi
        ]

        FONT_FILE = ''
        for f in possible_fonts:
                if os.path.exists(f):
                        FONT_FILE = f
                break

        if '' == FONT_FILE:
                raise 'no font file found'

	GPIO.setmode(GPIO.BCM)
	GPIO.setup(button1, GPIO.IN)
	GPIO.setup(button2, GPIO.IN)
	GPIO.setup(button3, GPIO.IN)
	GPIO.setup(button4, GPIO.IN)
	menu = 0
        size1 = 11
        size2 = 17
	#dir_path = os.path.dirname(os.path.realpath(__file__))
        dir_path = os.path.dirname(os.path.abspath(__file__))
	int_ip = get_lan_ip()
	myip = ipgetter.myip()
	screen = PapirusTextPos(False)
	screen.AddText("Starting Appliance", 20, 70, size2, FONT_FILE)
	screen.WriteAll()
	ext_ip = 'External: ' +  myip
	int_ip = 'Internal: '  + int_ip
	speed_test_log = dir_path+'/speedtest.txt'
	screen.Clear()
	graph_code = dir_path+'/ImageDemo.py temp.png'
	speed_test_code = dir_path+'/speedtest.sh'
	show_menu()
	try:
		while True:
			#Primary Menu Options
			if (menu == 0 and GPIO.input(button1) == False) :
				speed_test()
				menu = 1
			if (menu == 0 and GPIO.input(button2) == False) :
                                graph_it()
                                menu = 1
			if (menu == 0 and GPIO.input(button3) == False) :
                                scan4it()
                                menu = 1
                        if (menu == 0 and GPIO.input(button4) == False) :
                                show_menu_2()
                                menu = 1

			#Advanced Meny Options
			if (menu == 1 and GPIO.input(button3) == False) :
				power_off()
				menu = 0
			if (menu == 1 and GPIO.input(button2) == False) :
				show_otp()
				menu = 0
			if (menu == 1 and GPIO.input(button4) == False) :
				show_menu()
				menu = 0

	except KeyboardInterrupt:
		print ("Exiting Appliance Code")
		screen.Clear()
