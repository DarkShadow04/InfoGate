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
	print "   [05] Malware Making"
	print "   [06] Wifi Attacks"
	print "   [07] DDos/Dos"
	print "   [08] Exploits"
	print "   [09] Other\n"
	print "   [10] Exit the InfoGate\n"
	InfoGate = raw_input("GATE > ")
	
	if InfoGate == "1" or InfoGate == "01":
		print "    [01] Nmap"
		print "    [02] Red Hawk"
		print "    [03] D-Tect"
		print "    [04] sqlmap"
		print "    [05] Infoga"
		print "    [06] ReconDog"
		print "    [07] IPGeolocation"
		print "    [08] Zenmap\n"
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
			IPGeoLocation()
		elif infogathering == "08" or infogathering == "8":
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

	elif InfoGate == "3" or InfoGate == "03":
		print "\n    [01] Nmap"
		print "    [02] Nikto"
		print "    [03] Dirsearch"
		print "    [04] Wpscan"
		print "    [05] Dnsenum"
		print "    [00] Back to main menu\n"
		enumeraton = raw_input("GATE > ")

		if enumeraton == "01" or enumeraton == "1":
			nmap()
		elif enumeraton == "02" or enumeraton == "2":
			nikto()
		elif enumeraton == "03" or enumeraton == "3":
			dirsearch()
		elif enumeraton == "04" or enumeraton == "4":
			wpscan()
		elif enumeraton == "05" or enumeraton == "5":
			dnsenum()
		elif enumeraton == "00" or enumeraton == "0":
			restart_program()
		else:
			print
			"\nERROR: Wrong Input"
			timeout(2)
			restart_program()

	elif InfoGate == "4" or InfoGate == "04":
		print "\n    [01] Hydra"
		print "    [02] HashID"
		print "    [03] Black Hydra"
		print "    [04] Hash Buster"
		print "    [05] Cupp"
		print "    [06] Social-Engineering"
		print "    [07] Hashzer"
		print "    [08] Hash-Generator"
		print "    [09] Crunch"
		print "    [10] Hashcat\n"
		print "    [00] Back to main menu\n"
		Paswdatk = raw_input("GATE > ")

		if Paswdatk == "01" or Paswdatk == "1":
			hydra()
		elif Paswdatk == "02" or Paswdatk == "2":
			hashid()
		elif Paswdatk == "03" or Paswdatk == "3":
			black_hydra()
		elif Paswdatk == "04" or Paswdatk == "4":
			hash_buster()
		elif Paswdatk == "05" or Paswdatk == "5":
			cupp()
		elif Paswdatk == "06" or Paswdatk == "6":
			social()
		elif Paswdatk == "07" or Paswdatk == "7":
			hashzer()
		elif Paswdatk == "08" or Paswdatk == "8":
			hashgenerator()
		elif Paswdatk == "09" or Paswdatk == "9":
			crunch()
		elif Paswdatk == "10":
			hashcat()
		elif Paswdatk == "00" or Paswdatk == "0":
			restart_program()
		else:
			print
			"\nERROR: Wrong Input"
			timeout(2)
			restart_program()

	elif InfoGate == "5" or InfoGate == "05":
		print "\n    [01] Vbug"
		print "    [02] Vbugmap"
		print "    [03] A-Rat"
		print "    [00] Back to main menu\n"
		malware = raw_input("GATE > ")

		if malware  == "01" or malware == "1":
			vbug()
		elif malware == "02" or malware == "2":
			vbugmap()
		elif malware == "03" or malware == "3":
			a_rat()
		elif malware == "00" or malware == "0":
			restart_program()
		else:
			print
			"\nERROR: Wrong Input"
			timeout(2)
			restart_program()

	elif InfoGate == "6" or InfoGate == "06":
		print "\n    [01] Fluxion"
		print "    [02] Routerspoit"
		print "    [03] Lazy Script"
		print "    [00] Back to main menu\n"
		wifiatk = raw_input("GATE > ")

		if wifiatk  == "01" or wifiatk == "1":
			fluxion()
		elif wifiatk == "02" or wifiatk == "2":
			routersploit()
		elif wifiatk == "03" or wifiatk == "3":
			lscript()
		elif wifiatk == "00" or wifiatk == "0":
			restart_program()
		else:
			print
			"\nERROR: Wrong Input"
			timeout(2)
			restart_program()

	elif InfoGate == "7" or InfoGate == "07":
		print "\n    [01] Fluxion"
		print "    [02] Routerspoit"
		print "    [03] Lazy Script"
		print "    [00] Back to main menu\n"
		ddos = raw_input("GATE > ")

		if ddos  == "01" or ddos == "1":
			fluxion()
		elif ddos == "02" or ddos == "2":
			routersploit()
		elif ddos == "03" or ddos == "3":
			lscript()
		elif ddos == "00" or ddos == "0":
			restart_program()
		else:
			print
			"\nERROR: Wrong Input"
			timeout(2)
			restart_program()

if __name__ == "__main__":
	main()
