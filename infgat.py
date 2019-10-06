## infgat.py - useful module of InfoGate
# -*- coding: utf-8 -*-
import os
import sys
import time


InfoGate_banner = """
..............
            ..,;:ccc,.
          ......''';lxO.
.....''''..........,:ld;
           .';;;:::;,,.x,
      ..'''.            0Xxoc:,.  ...
  ....                ,ONkc;,;cokOdc',.
 .                   OMo           ':ddo.
                    dMc               :OO;
                    0M.                 .:o.
                    ;Wd
                     ;XO,
                       ,d0Odlc;,..
                           ..',;:cdOOd::,.
                                    .:d;.':;.
                                       'd,  .'
                                         ;l   ..
                                          .o
                                            c
                                            .'
                                             .
Author             : Dark_Shadow04
contact            : darkshadow100497@gmail.com
Github             : https://github.com/DarkShadow04
My Blog            : http://arabaab.blogspot.com

Subcribe my blog for Tools, Tricks & Scripts ^_^
"""
backtomenu_banner = """
  [99] Back
  [00] Exit
"""
def restart_program():
	python = sys.executable
	os.execl(python, python, * sys.argv)
	curdir = os.getcwd()

def backtomenu_option():
	print backtomenu_banner
	backtomenu = raw_input("GATE > ")

	if backtomenu == "99":
		restart_program()
	elif backtomenu == "00":
		sys.exit()
	else:
		print "\nERROR: Wrong Input"
		time.sleep(2)
		restart_program()

def banner():
	print InfoGate_banner

def nmap():
	print '\n###### Installing Nmap'
	os.system('apt update && apt upgrade')
	os.system('apt install nmap')
	print '###### Done'
	print "###### Type 'nmap' to start."
	backtomenu_option()

def red_hawk():
	print '\n###### Installing RED HAWK'
	os.system('apt update && apt upgrade')
	os.system('apt install git php')
	os.system('git clone https://github.com/Tuhinshubhra/RED_HAWK')
	os.system('mv -v RED_HAWK Scanning')
	print '###### Done'
	backtomenu_option()

def dtect():
	print '\n###### Installing D-Tect'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/bibortone/D-Tech')
	os.system('mv D-TECT ~')
	print '###### Done'
	backtomenu_option()

def sqlmap():
	print '\n###### Installing sqlmap'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2')
	os.system('git clone https://github.com/sqlmapproject/sqlmap')
	os.system('mv sqlmap ~')
	print '###### Done'
	backtomenu_option()

def Zenmap():
	print '\n###### Installing Zenmap'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2')
	os.system('sudo apt-get install zenmap')
	print '###### Done'
	backtomenu_option()

def infoga():
	print '\n###### Installing Infoga'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('python2 -m pip install requests urllib3 urlparse')
	os.system('git clone https://github.com/m4ll0k/Infoga')
	os.system('mv Infoga ~')
	print '###### Done'
	backtomenu_option()

def reconDog():
	print '\n###### Installing ReconDog'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/UltimateHackers/ReconDog')
	os.system('mv ReconDog ~')
	print '###### Done'
	backtomenu_option()

def androZenmap():
	print '\n###### Installing AndroZenmap'
	os.system('apt update && apt upgrade')
	os.system('apt install nmap curl')
	os.system('curl -O https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/scripts/androzenmap.sh')
	os.system('mkdir ~/AndroZenmap')
	os.system('mv androzenmap.sh ~/AndroZenmap')
	print '###### Done'
	backtomenu_option()

def IPGeoLocation():
	print '\n###### Installing IPGeoLocation'
	os.system('apt update && apt upgrade')
	os.system('apt install python3')
	os.system('git clone https://github.com/maldevel/IPGeoLocation')
	os.system('apt-get install python3-setuptools')
	print '###### Done'
	backtomenu_option()

def sqliv():
	print '\n###### Installing SQLiv'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/Hadesy2k/sqliv')
	os.system('mv sqliv ~')
	print '###### Done'
	backtomenu_option()

def sqlscan():
	print '\n###### Installing sqlscan'
	os.system('apt update && apt upgrade')
	os.system('apt install git php')
	os.system('git clone http://www.github.com/Cvar1984/sqlscan')
	os.system('mv sqlscan ~')
	print '###### Done'
	backtomenu_option()

def wordpreSScan():
	print '\n###### Installing Wordpresscan'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 python2-dev clang libxml2-dev libxml2-utils libxslt-dev')
	os.system('git clone https://github.com/swisskyrepo/Wordpresscan')
	os.system('mv Wordpresscan ~')
	os.system('cd ~/Wordpresscan && python2 -m pip install -r requirements.txt')
	print '###### Done'
	backtomenu_option()

def wpscan():
	print '\n###### Installing WPScan'
	os.system('apt update && apt upgrade')
	os.system('apt install git ruby curl')
	os.system('git clone https://github.com/wpscanteam/wpscan')
	os.system('mv wpscan ~ && cd ~/wpscan')
	os.system('gem install bundle && bundle config build.nokogiri --use-system-libraries && bundle install && ruby wpscan.rb --update')
	print '###### Done'
	backtomenu_option()

def striker():
	print '\n###### Installing Striker'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2')
	os.system('git clone https://github.com/UltimateHackers/Striker')
	os.system('mv Striker ~')
	os.system('cd ~/Striker && python2 -m pip install -r requirements.txt')
	print '###### Done'
	backtomenu_option()

def routersploit():
	print '\n###### Installing Routersploit'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('python2 -m pip install requests')
	os.system('git clone https://github.com/reverse-shell/routersploit')
	os.system('mv routersploit ~;cd ~/routersploit;python2 -m pip install -r requirements.txt;termux-fix-shebang rsf.py')
	print '###### Done'
	backtomenu_option()

def xshell():
	print '\n###### Installing Xshell'
	os.system("apt update && apt upgrade")
	os.system("apt install lynx python2 figlet ruby php nano w3m")
	os.system("git clone https://github.com/Ubaii/Xshell")
	os.system("mv Xshell ~")
	print '###### Done'
	backtomenu_option()

def sh33ll():
	print '\n###### Installing SH33LL'
	os.system("apt update && apt upgrade")
	os.system("apt install git python2")
	os.system("git clone https://github.com/LOoLzeC/SH33LL")
	os.system("mv SH33LL ~")
	print '###### Done'
	backtomenu_option()

def blackbox():
	print '\n###### Installing BlackBox'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git && python2 -m pip install optparse passlib')
	os.system('git clone https://github.com/jothatron/blackbox')
	os.system('mv blackbox ~')
	print '###### Done'
	backtomenu_option()

def xattacker():
	print '\n###### Installing XAttacker'
	os.system('apt update && apt upgrade')
	os.system('apt install git perl')
	os.system('cpnm install HTTP::Request')
	os.system('cpnm install LWP::Useragent')
	os.system('git clone https://github.com/Moham3dRiahi/XAttacker')
	os.system('mv XAttacker ~')
	print '###### Done'
	backtomenu_option()

def owscan():
	print '\n###### Installing OWScan'
	os.system('apt update && apt upgrade')
	os.system('apt install git php')
	os.system('git clone https://github.com/Gameye98/OWScan')
	os.system('mv OWScan ~')
	print '###### Done'
	backtomenu_option()

def hydra():
	print '\n###### Installing Hydra'
	os.system('apt update && apt upgrade')
	os.system('apt install hydra')
	print '###### Done'
	backtomenu_option()

def hashid():
	print '\n###### Installing HashID'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 && python2 -m pip install hashid')
	print "###### Done"
	print "###### Type 'hashid -h' to show usage of hashid"
	backtomenu_option()

def black_hydra():
	print '\n###### Installing Black Hydra'
	os.system('apt update && apt upgrade')
	os.system('apt install hydra git python2')
	os.system('git clone https://github.com/Gameye98/Black-Hydra')
	os.system('mv Black-Hydra ~')
	print '###### Done'
	backtomenu_option()

def hash_buster():
	print '\n###### Installing Hash-Buster'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/UltimateHackers/Hash-Buster')
	os.system('mv Hash-Buster ~')
	print '###### Done'
	backtomenu_option()

def cupp():
	print '\n###### Installing Cupp'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/Mebus/cupp')
	os.system('mv cupp ~')
	print '###### Done'
	backtomenu_option()

def social():
	print '\n###### Installing Social-Engineering'
	os.system("apt update && apt upgrade")
	os.system("apt install python2 perl")
	os.system("git clone https://github.com/LOoLzeC/social-engineering")
	os.system("mv social-engineering ~")
	print '###### Done'
	backtomenu_option()

def hashzer():
	print '\n###### Installing Hashzer'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2')
	os.system('python2 -m pip install requests')
	os.system('git clone https://github.com/Anb3rSecID/Hashzer')
	os.system('mv Hashzer ~')
	print '###### Done'
	backtomenu_option()

def hashgenerator():
	print '\n###### Installing Hash-Generator'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2 && python2 -m pip install passlib progressbar')
	os.system('git clone https://github.com/ciku370/hash-generator')
	os.system('mv hash-generator ~')
	print '###### Done'
	backtomenu_option()

def crunch():
	print '\n###### Installing Crunch'
	os.system('apt update && apt upgrade')
	os.system('apt install unstable-repo')
	os.system('apt install crunch')
	print "###### Done"
	backtomenu_option()

def hashcat():
	print '\n###### Installing Hashcat'
	os.system('apt update && apt upgrade')
	os.system('apt install unstable-repo')
	os.system('apt install hashcat')
	print "###### Done"
	backtomenu_option()

def nikto():
	print '\n###### Installing Nikto'
	os.system('apt update && apt upgrade')
	os.system('apt install perl')
	os.system('wget https://github.com/sullo/nikto/archive/master.zip')
	os.system('unzip master.zip')
	os.system('rm -rvf master.zip')
	os.system('cd nikto-master/program')
	os.system('perl nikto.pl')
	print "###### Done"
	backtomenu_option()

def dirsearch():
	print '\n###### Installing Dirsearch'
	os.system('apt update && apt upgrade')
	os.system('apt install python')
	os.system('apt install git')
	os.system('git clone https://github.com/maurosoria/dirsearch')
	os.system('cd dirsearch')
	os.system('python dirsearch.py -h ')
	print "###### Done"
	backtomenu_option()

def wpscan():
	print '\n###### Installing Wpscan'
	os.system('apt update && apt upgrade')
	os.system('apt install gem')
	os.system('apt install rake')
	os.system('git clone https://github.com/wpscanteam/wpscan')
	os.system('cd wpscan/')
	os.system('bundle install && rake install')
	print "###### Done"
	backtomenu_option()

def dnsenum():
	print '\n###### Installing Dnsenum'
	os.system('apt update && apt upgrade')
	os.system('apt-get install dnsenum')
	print "###### Done"
	backtomenu_option()

def vbug():
	print '\n###### Installing Vbug'
	os.system('apt update && apt upgrade')
	os.system(' pkg install python2')
	os.system('git clone https://github.com/DarkShadow04/vbug.git')
	print "###### Done"
	backtomenu_option()

def vbugmap():
	print '\n###### Installing Vbugmap'
	os.system('apt update && apt upgrade')
	os.system(' pkg install python2')
	os.system('git clone https://github.com/DarkShadow04/vbugmap.git')
	print "###### Done"
	backtomenu_option()

def a_rat():
	print '\n###### Installing A-Rat'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/Xi4u7/A-Rat')
	os.system('mv A-Rat ~')
	print '###### Done'
	backtomenu_option()

def fluxion():
	print '\n###### Installing Fluxion'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('git clone https://www.github.com/FluxionNetwork/fluxion.git')
	os.system('apt-get install hostapd')
	os.system('apt-get install isc-dhcp-server')
	os.system('apt-get install lighttpd')
	os.system('apt-get install php-cgi')
	os.system('apt-get install mdk4')
	print '###### Done'
	backtomenu_option()


def lscript():
	print '\n###### Installing Lazy Script'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/arismelachroinos/lscript.git')
	os.system('cd lscript')
	os.system('chmod +x install.sh')
	os.system('./install.sh')
	print '###### Done'
	backtomenu_option()

def DDOSIM():
	print '\n###### Installing DDOSIM'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/r00tabega/DDOSIM.git')
	os.system('cd DDOSIM')
	os.system('chmod +x ddosim-install.sh')
	os.system('sudo ./ddosim-install.sh')
	print '###### Done'
	backtomenu_option()

def torshammer():
	print '\n###### Installing Torshammer'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/dotfighter/torshammer')
	os.system('mv torshammer ~')
	print '###### Done'
	backtomenu_option()

def fl00d12():
	print '\n###### Installing Fl00d & Fl00d2'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 curl')
	os.system('mkdir ~/fl00d')
	os.system('curl -O https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/scripts/fl00d.py')
	os.system('curl -O https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/scripts/fl00d2.py')
	os.system('mv fl00d.py ~/fl00d && mv fl00d2.py ~/fl00d')
	print '###### Done'
	backtomenu_option()

def goldeneye():
	print '\n###### Installing GoldenEye'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2')
	os.system('git clone https://github.com/jseidl/GoldenEye')
	os.system('mv GoldenEye ~')
	print '###### Done'
	backtomenu_option()

def xerxes():
	print '\n###### Installing Xerxes'
	os.system('apt update && apt upgrade')
	os.system('apt install git')
	os.system('apt install clang')
	os.system('git clone https://github.com/zanyarjamal/xerxes')
	os.system('mv xerxes ~')
	os.system('cd ~/xerxes && clang xerxes.c -o xerxes')
	print '###### Done'
	backtomenu_option()

def sanlen():
	print '\n###### Installing santet-online'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2 && python2 -m pip install requests')
	os.system('git clone https://github.com/Gameye98/santet-online')
	os.system('mv santet-online ~')
	print '###### Done'
	backtomenu_option()

def metasploit():
	print '\n###### Installing Metasploit'
	os.system("apt update && apt upgrade")
	os.system("apt install git wget curl")
	os.system("pkg intall unstable-repo")
	os.system("apt install metasploit")
	print '###### Done'
	print "###### Type 'msfconsole' to start."
	backtomenu_option()

def commix():
	print '\n###### Installing Commix'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/commixproject/commix')
	os.system('mv commix ~')
	print '###### Done'
	backtomenu_option()

def brutal():
	print '\n###### Installing Brutal'
	os.system('apt update && apt upgrade')
	os.system('apt install git')
	os.system('git clone https://github.com/Screetsec/Brutal')
	os.system('mv Brutal ~')
	print '###### Done'
	backtomenu_option()

def wpsploit():
	print '\n###### Installing WPSploit'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('git clone git clone https://github.com/m4ll0k/wpsploit')
	os.system('mv wpsploit ~')
	print '###### Done'
	backtomenu_option()

def websploit():
	print '\n###### Installing Websploit'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2')
	os.system('python2 -m pip install scapy')
	os.system('git clone https://github.com/The404Hacking/websploit')
	os.system('mv websploit ~')
	print '###### Done'
	backtomenu_option()

def txtool():
	print '\n###### Installing TXTool'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2 nmap php curl')
	os.system('python2 -m pip install requests')
	os.system('git clone https://github.com/kuburan/txtool')
	os.system('mv txtool ~')
	print '###### Done'
	backtomenu_option()

def binploit():
	print '\n###### Installing Binary Exploitation'
	os.system('apt update && apt upgrade')
	os.system('apt install gdb radare2 ired ddrescue bin-utils yasm strace ltrace cdb hexcurse memcached llvmdb')
	print "###### Done"
	print "###### Tutorial: https://youtu.be/3NTXFUxcKPc"
	backtomenu_option()

def asu():
	print '\n###### Installing ASU'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2 php')
	os.system('python2 -m pip install requests bs4 mechanize')
	os.system('git clone https://github.com/LOoLzeC/ASU')
	os.system('mv ASU ~')
	print '###### Done'
	backtomenu_option()

def spiderbot():
	print '\n###### Installing SpiderBot'
	os.system("apt update && apt upgrade")
	os.system("apt install git php")
	os.system("git clone https://github.com/Cvar1984/SpiderBot")
	os.system("mv SpiderBot ~")
	print '###### Done'
	backtomenu_option()

def ngrok():
	print '\n###### Installing Ngrok'
	os.system('apt update && apt upgrade')
	os.system('apt install git')
	os.system('git clone https://github.com/themastersunil/ngrok')
	os.system('mv ngrok ~')
	print '###### Done'
	backtomenu_option()

def sudo():
	print '\n###### Installing sudo'
	os.system('apt update && apt upgrade')
	os.system('apt install ncurses-utils git')
	os.system('git clone https://github.com/st42/termux-sudo')
	os.system('mv termux-sudo ~ && cd ~/termux-sudo && chmod 777 *')
	os.system('cat sudo > /data/data/com.termux/files/usr/bin/sudo')
	os.system('chmod 700 /data/data/com.termux/files/usr/bin/sudo')
	print '###### Done'
	backtomenu_option()

def ubuntu():
	print '\n###### Installing Ubuntu'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/Neo-Oli/termux-ubuntu')
	os.system('mv termux-ubuntu ~ && cd ~/termux-ubuntu && bash ubuntu.sh')
	print '###### Done'
	backtomenu_option()

def fedora():
	print '\n###### Installing Fedora'
	os.system('apt update && apt upgrade')
	os.system('apt install wget git')
	os.system('wget https://raw.githubusercontent.com/nmilosev/termux-fedora/master/termux-fedora.sh')
	os.system('mv termux-fedora.sh ~')
	print '###### Done'
	backtomenu_option()

def nethunter():
	print '\n###### Installing Kali NetHunter'
	os.system('apt update && apt upgrade')
	os.system('apt install git')
	os.system('git clone https://github.com/Hax4us/Nethunter-In-Termux')
	os.system('mv Nethunter-In-Termux ~')
	print '###### Done'
	backtomenu_option()

