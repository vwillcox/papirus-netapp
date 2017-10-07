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
from time import sleep


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
        screen.AddText("3) Reboot Pi", 10, 100)
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
	menu = 0
        size1 = 11
        size2 = 17
	dir_path = os.path.dirname(os.path.realpath(__file__))
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
	speed_test_log = dir_path+'/speedtest.txt'
	screen.Clear()
	graph_code = dir_path+'/ImageDemo.py temp.png'
	speed_test_code = dir_path+'/speedtest.sh'
	show_menu()
	try:
		while True:
			if (menu == 0 and button1.wait_for_release(1)):
				speed_test()
				menu = 1
			if (menu == 1 and button3.wait_for_release(1)):
				power_off()
				menu = 0
			if (menu == 0 and button2.wait_for_release(1)):
				graph_it()
				menu = 1
			if (menu == 1 and button2.wait_for_release(1)):
				reboot_it()
				menu = 0
			if (menu == 0 and button3.wait_for_release(1)):
				scan4it()
				menu = 1
			if (menu == 0 and button4.wait_for_release(1)):
				show_menu_2()
				menu = 1
			if (menu == 1 and button4.wait_for_release(1)):
				show_menu()
				menu = 0

	except KeyboardInterrupt:
		print ("Exiting Appliance Code")
		screen.Clear()
