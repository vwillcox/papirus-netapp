#!/usr/bin/python

from getip import get_lan_ip

from papirus import PapirusTextPos
import ipgetter
import subprocess
import shlex
import os
import ImageFont
from gpiozero import Button
import ImageDemo
import scan4pi

def show_menu():
	screen.Clear()
	screen.AddText("Main Menu", 10, 10)
	screen.AddText("1) Main Menu", 10, 40)
	screen.AddText("2) Scan 4 Pi's", 10, 70)
	screen.AddText("3) Speed Graph", 10, 100)
	screen.AddText("4) Speed Test", 10, 130)
	screen.WriteAll()

def speed_test():
	screen.Clear()
	screen.AddText("Running Speedtest now", 20, 70)
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

        size1 = 11
        size2 = 17
        #font1 = ImageFont.truetype(FONT_FILE, TEXT_FONT_SIZE1)
        #font2 = ImageFont.truetype(FONT_FILE, TEXT_FONT_SIZE2)

	int_ip = get_lan_ip()
	myip = ipgetter.myip()
	screen = PapirusTextPos(False)
	screen.AddText("Starting Appliance", 20, 70, size2, FONT_FILE)
	screen.WriteAll()
	button1 = Button(16, pull_up=False)
	button2 = Button(26, pull_up=False)
	button3 = Button(20, pull_up=False)
	button4 = Button(21, pull_up=False)
	ext_ip = 'External: ' +  myip
	int_ip = 'Internal: '  + int_ip
	speed_test_log = '/home/pi/netapp/speedtest.txt'
	screen.Clear()
	graph_code = '/home/pi/netapp/ImageDemo.py temp.png'
	speed_test_code = '/home/pi/netapp/speedtest.sh'
	show_menu()
	try:
		while True:
			if button1.wait_for_release(1):
				speed_test()
			if button2.wait_for_release(1):
				graph_it()
			if button3.wait_for_release(1):
				scan4it()
			if button4.wait_for_release(1):
				show_menu()
	except KeyboardInterrupt:
		print ("Exiting Appliance Code")
