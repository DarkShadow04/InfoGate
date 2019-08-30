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
	print "   [05] Other\n"0
	print "   [10] Exit the InfoGate\n"
	InfoGate = raw_input("GATE > ")
	
	if InfoGate == "1" or InfoGate == "01":
		print "\n  [01] Nmap"
		print "    [02] Red Hawk"
		print "    [03] D-Tect"
		print "    [04] sqlmap"
		print "    [05] Zenmap\n"
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
			Zenmap()
		elif infogathering == "00" or infogathering == "0":
			restart_program()

		else:
                        print "\nERROR: Wrong Input"
                        timeout(2)
                        restart_program()

if __name__ == "__main__":
	main()
