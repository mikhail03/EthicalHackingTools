#!/usr/bin/python
__author__ = "Mikhail Bennett"
__Date__ = "June 26th, 2019"
__copyright__= "Copyright 2019, Integrity Cyber Knights"

#####################################################################################
###								Nmap Framework UI  						          ###
###																			  	  ###
#####################################################################################

import sys
import os
import time

####################################################################################################
###	  					Top Nmap Scripts   						                                 ###
###	nmap -p 445 --script smb-os-discovery 192.168.1.0/24						                 ###
###	nmap -p 80 --script dns-brute.nse vulnweb.com				                                 ###
### nmap -p 80 --script hostmap-bfk.nse nmap.org								                 ###
### nmap --traceroute --script traceroute-geolocation.nse -p 80 hackertarget.com                 ###
### nmap --script http-enum 192.168.10.55       								                 ###
###	nmap -p 445 --script smb-enum-users.nse|smb-enum-groups.nse|processes|psexec                 ###
###	nmap -sV -p 445 --script smb-brute 192.168.1.101			                                 ###
### nmap -p 445 --script smb-double-pulsar-backdoor.nse   						                 ###
###	nmap --script vulners -sV -p3389 172.28.21.211										         ### 
###	nmap --script vulscan -sV -p445 172.28.21.211                                                ### 
###	nmap --script vulscan --script-args vulscandb=database_name -sV -p445 172.28.21.211          ### 
###	nmap --script vulscan --script-args vulscandb=scipvuldb.csv -sV -p8888 172.28.21.211         ### 
###	nmap --script vulscan --script-args vulscandb=exploitdb.csv -sV -p103 172.28.21.211          ###
###	nmap --script vulscan --script-args vulscandb=securitytracker.csv -sV -p135 172.28.21.211    ### 
### nmap --script vulners,vulscan --script-args vulscandb=scipvuldb.csv -sV -p445 172.28.21.211  ### 
###	REFERENCE: https://hackertarget.com/7-nmap-nse-scripts-recon/                                ###
###	https://null-byte.wonderhowto.com/how-to/easily-detect-cves-with-nmap-scripts-0181925/       ###           
####################################################################################################



# Followup - Issue with interactive mode function

def mode_banner():
	print '=' * 121

def banner():
	print '=' * 125

def menu_mode():
	x = True
	while(x):
		mode_banner()
		try:
			choice = input("| Please Select Mode [1 or 2]:\t\t\t\t\t\t\t\t\t\t\t\t |\n| \
			\t\t\t\t\t\t\t\t\t\t\t\t | \
			\n|\t  1 - Interactive Mode \t\t\t\t\t\t\t\t\t\t\t\t |\
			\n|\t  2 - Autonomous Mode: MS17-010 Scan\t\t\t\t\t\t\t\t\t\t | \
			\n|\t  3 - Recon Script Mode: Recon Scans\t\t\t\t\t\t\t\t\t\t | \
			\n| \
			\n| input:_|")
			mode_banner()

			if choice == 1:
				interactive_mode()
				break

			elif choice == 2:
				scan()
				break

			elif choice == 3:
				recon_Mode()

			else:
				print "\n\n\t\tWrong selection, please try again or enter ctrl+c to exit\n\n"
				continue
		except:
			print "\n\n\t\tWrong selection, please re-run the program to continue.... \n\n"
			x = False


def interactive_mode():
	status = True
	nmap_path = r'C:\Users\1265748\Nmap\nmap.exe'


	command = nmap_path + " -p445 --script smb-vuln-ms17-010 "
	switch = " -Pn"

	while(status):
		ip = raw_input("\n\nEnter the IP address to be scan:_ ")
	
	 	print("\n\n- NMAP Vuln SCAN: {}".format(ip))
	   	banner()
	   	os.system(command + ip + switch) # Running OS command in command prompt
	   	banner()

	   	answer = raw_input("Continue[Y/N] ?_ ")

	   	try:
		   	if (answer == 'y' or answer == 'Y'):
		   		continue
		   	elif (answer == 'n' or answer == 'N'):
		   		print "\n\n\t\tRecon Complete, Happy Hunting!\n\n"
		   		status = False
		   	else:
		   		print "\n\n\t\tWrong selection, please try again or enter ctrl+c to exit\n\n"
		except:
			print "\n\n\t\tWrong selection, please re-run the program to continue.... \n\n"
			status = False

def recon_Mode():
	x = 10
	print "Initiating......"

	for x in range(10):
		print "/"
		os.system("cls")
		print "\\"



	print "| Welcome to Recon Mode: Script Menu\t\t\t\t\t\t\t\t\t\t\t\t |\n| \
			\t\t\t\t\t\t\t\t\t\t\t\t | \
			\n|\t  1 - Interactive Mode \t\t\t\t\t\t\t\t\t\t\t\t |\
			\n|\t  2 - Autonomous Mode: MS17-010 Scan\t\t\t\t\t\t\t\t\t\t | \
			\n|\t  3 - Recon Mode: Script Scans\t\t\t\t\t\t\t\t\t\t | \
			\n| \
			\n| input:_|"

def scan():
	nmap_path = r'C:\Users\1265748\Nmap\nmap.exe'
	command = nmap_path + " -p445 --script smb-vuln-ms17-010 "
	switch = " -Pn"
	filepath = r'C:\Users\1265748\Documents\Scripts\scan_list.txt'  

	if not os.path.isfile(filepath):
		print("File path {} does not exist. Exiting...".format(filepath))
		sys.exit()

	with open(filepath) as fp:
		line = fp.readline()
   		for cnt, line in enumerate(fp):
   			print "\n\n"
   			print("{}- NMAP Vuln SCAN: {}".format(cnt+1, line.strip()))
   			banner()
   			ip = line.strip()
   			#print ip + "\n\n" # Debugging: Identify current IP in line
   			os.system(command + ip + switch) # Running OS command in command prompt
   			banner()
       		line = fp.readline()




def main():
	menu_mode()

	# nmap_path = r'C:\Users\1265748\Nmap\nmap.exe'
	# command = nmap_path + " -p445 --script smb-vuln-ms17-010 "
	# switch = " -Pn"
	# filepath = r'C:\Users\1265748\Documents\Scripts\test.txt'  

	# if not os.path.isfile(filepath):
	# 	print("File path {} does not exist. Exiting...".format(filepath))
	# 	sys.exit()

	# with open(filepath) as fp:
	# 	line = fp.readline()
 #   		for cnt, line in enumerate(fp):
 #   			print "\n\n"
 #   			print("{}- NMAP Vuln SCAN: {}".format(cnt+1, line.strip()))
 #   			banner()
 #   			ip = line.strip()
 #   			#print ip + "\n\n" # Debugging: Identify current IP in line
 #   			os.system(command + ip + switch) # Running OS command in command prompt
 #   			banner()
 #       		line = fp.readline()
       		


if __name__ == '__main__':
	main()


# References:
# https://stackabuse.com/read-a-file-line-by-line-in-python/
