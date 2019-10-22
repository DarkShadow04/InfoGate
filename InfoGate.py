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
	print "   [09] Other(Termux)\n"
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
		print "    [08] Zenmap
		print "    [09] Saycheese
		print "    [10] Locator\n"
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
		elif infogathering == "09" or infogathering == "9":
			saycheese()
		elif infogathering == "10":
			locator()
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
		print "\n    [01] DDOSIM"
		print "    [02] Torshammer"
		print "    [03] Fl00d & Fl00d2"
		print "    [04] GoldenEye"
		print "    [05] Xerxes"
		print "    [06] santet-online\n"
		print "    [00] Back to main menu\n"
		ddos = raw_input("GATE > ")

		if ddos  == "01" or ddos == "1":
			DDOSIM()
		elif ddos == "02" or ddos == "2":
			torshammer()
		elif ddos == "03" or ddos == "3":
			fl00d12()
		elif ddos == "04" or ddos == "4":
			goldeneye()
		elif ddos == "05" or ddos == "5":
			xerxes()
		elif ddos == "06" or ddos == "6":
			sanlen()
		elif ddos == "00" or ddos == "0":
			restart_program()
		else:
			print
			"\nERROR: Wrong Input"
			timeout(2)
			restart_program()

	elif InfoGate == "8" or InfoGate == "08":
		print "\n    [01] Metasploit-Termux"
		print "    [02] commix"
		print "    [03] Brutal"
		print "    [04] WPSploit"  
		print "    [05] Websploit"
		print "    [06] Routersploit"
		print "    [07] XAttacker"
		print "    [08] TXTool"
		print "    [09] Binary Exploitation"
		print "    [10] ASU\n"
		print "    [00] Back to main menu\n"
		exploit = raw_input("GATE > ")
		
		if exploit == "01" or exploit == "1":
			metasploit()
		elif exploit == "02" or exploit == "2":
			commix()
		elif exploit == "03" or exploit == "3":
			brutal()
		elif exploit == "04" or exploit == "4":
			wpsploit()
		elif exploit == "05" or exploit == "5":
			websploit()
		elif exploit == "06" or exploit == "6":
			routersploit()
		elif exploit == "07" or exploit == "7":
			xattacker()
		elif exploit == "08" or exploit == "8":
			txtool()
		elif exploit == "09" or exploit == "9":
			binploit()
		elif exploit == "10":
			asu()
		elif exploit == "00" or exploit == "0":
			restart_program()
		else:
			print "\nERROR: Wrong Input"
			timeout(2)
			restart_program()

	elif InfoGate == "9" or InfoGate == "09":
		print "\n    [01] SpiderBot"
		print "    [02] Ngrok"
		print "    [03] Sudo"
		print "    [04] Ubuntu"
		print "    [05] Fedora"
		print "    [06] Kali Nethunter"
		print "    [00] Back to main menu\n"
		moretool = raw_input("GATE > ")

		if moretool == "01" or moretool == "1":
			spiderbot()
		elif moretool == "02" or moretool == "2":
			ngrok()
		elif moretool == "03" or moretool == "3":
			sudo()
		elif moretool == "04" or moretool == "4":
			ubuntu()
		elif moretool == "05" or moretool == "5":
			fedora()
		elif moretool == "06" or moretool == "6":
			nethunter()
		elif moretool == "00" or moretool == "0":
			restart_program()
		else:
			print "\nERROR: Wrong Input"
			timeout(2)
			restart_program()

	elif InfoGate == "10":
		sys.exit()

	else:
		print "\nERROR: Wrong Input"
		timeout(2)
		restart_program()

if __name__ == "__main__":
	main()
