## InfoGate.py - InfoGate v3.0
# -*- coding: utf-8 -*-
##
import os
import sys
from time import sleep as timeout
from infgat import *

def main():
	banner()
	print "   [01] Information Gathering"
	print "   [02] Scanning"
	print "   [03] Enumeration"
	print "   [04] Password Attacks"
	print "   [05] Other\n"
	print "   [10] Exit the InfoGate\n"
	InfoGate = raw_input("GATE > ")
	
	if InfoGate == "1" or InfoGate == "01":
		print "    [01] Nmap"
		print "    [02] Red Hawk"
		print "    [03] D-Tect"
		print "    [04] sqlmap"
		print "    [05] Infoga"
		print "    [06] ReconDog"
		print "    [07] Zenmap\n"
		print "    [00] Back to main menu\n"
		infogathering = raw_input("GATE > ")
		
		if infogathering == "01" or infogathering == "1":
			nmap()
		elif infogathering == "02" or infogathering == "2":
			red_hawk()
		elif infogathering == "03" or infogathering == "3":
			dtect()
		elif infogathering == "04" or infogathering == "4":
			sqlmap()
		elif infogathering == "05" or infogathering == "5":
			infoga()
		elif infogathering == "06" or infogathering == "6":
			reconDog()
		elif infogathering == "07" or infogathering == "7":
			Zenmap()
		elif infogathering == "00" or infogathering == "0":
			restart_program()

		else:
                        print "\nERROR: Wrong Input"
                        timeout(2)
                        restart_program()

	elif InfoGate == "2" or InfoGate == "02":
		print "\n    [01] Nmap"
		print "    [02] AndroZenmap"
		print "    [03] SQLiv"
		print "    [04] sqlmap"
		print "    [05] sqlscan"
		print "    [06] Wordpresscan"
		print "    [07] WPScan"
		print "    [08] Striker"
		print "    [09] Routersploit"
		print "    [10] Xshell"
		print "    [11] SH33LL"
		print "    [12] BlackBox"
		print "    [13] XAttacker"
		print "    [14] OWScan\n"
		print "    [00] Back to main menu\n"
		scanning = raw_input("GATE > ")

		if scanning == "01" or scanning == "1":
			nmap()
		elif scanning == "02" or scanning == "2":
			androZenmap()
		elif scanning == "03" or scanning == "3":
			sqliv()
		elif scanning == "04" or scanning == "4":
			sqlmap()
		elif scanning == "05" or scanning == "5":
			sqlscan()
		elif scanning == "06" or scanning == "6":
			wordpreSScan()
		elif scanning == "07" or scanning == "7":
			wpscan()
		elif scanning == "08" or scanning == "8":
			striker()
		elif scanning == "09" or scanning == "9":
			routersploit()
		elif scanning == "10":
			xshell()
		elif scanning == "11":
			sh33ll()
		elif scanning == "12":
			blackbox()
		elif scanning == "13":
			xattacker()
		elif scanning == "14":
			owscan()
		elif scanning == "00" or scanning == "0":
			restart_program()
		else:
			print
			"\nERROR: Wrong Input"
			timeout(2)
			restart_program()


if __name__ == "__main__":
	main()
