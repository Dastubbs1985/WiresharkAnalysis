###############################################
#	Dale Stubbs - 14024149	     	  		#
#  This script is designed to read in the 			#
#  Network Captures from the coursework.  		#
#  It gathers the information from the	  		# 
#  capture and plots the information on  			#
#  a graph using MatPlotLib.		  		#
#  Last Edited - 21/11/2016		  		#
###############################################
import dpkt
from dpkt.tcp import TCP
import sys 
import matplotlib.pyplot as plt
import socket
#  Plots a graph based on the port number and time stamp.
def plot_graph1(ports, packets, in_ip):
	plt.plot(packets, ports, 'b-')
	plt.title("14024149 \n Port Scan")
	plt.ylabel('Port Number')
	plt.xlabel('Time Stamp of Packet (Attacker IP: ' + in_ip + ')')
	plt.show()
#  Plots a graph based on the incorrect password attempts and time stamp.
def plot_graph2(attempts, packets, in_ip):
	plt.plot(packets, attempts, 'b-')
	plt.title("14024149\n Password Attack")
	plt.ylabel('Number of Incorrect Password Attempts')
	plt.xlabel('Time Stamp of Each Attempt (Attacker IP: ' + in_ip + ')')
	plt.show()

def main(capture, in_ip):
	#  Reads the PCAP file in using the 'read binary' command
	f = open(capture, 'rb')
	pcap = dpkt.pcap.Reader(f)
	count = 1
	ports = []
	packets1 = []
	packets2 = []
	attempts = []
	#  Loops through each packet in the capture
	for ts, buf in pcap:
		eth = dpkt.ethernet.Ethernet(buf)
		print eth
		ip = eth.data
		#tcp = ip.data
#		icmp = ip.data
#		#  Filters the traffic based on the IP address
#		#print 'Works'
#		if (ip.p == dpkt.ip.IP_PROTO_ICMP) and len(icmp.data.data) > 0:
#			try:
#				print icmp.data.data
#			except:
#				print 'Error'	
		#if type(ip.data) == TCP:
#			source_ip = socket.inet_ntoa(ip.src)
#			if source_ip == in_ip:			
#				#  Appends the Port Number and time stamp to the
#				#  appropriate lists	
#				packets1.append(ts)
#				ports.append(tcp.dport)
#				#  Filters traffic again based on the '530' response code
#				#  being present in the TCP Data.
#				#  530 is the code for 'Incorrect Login'							
#				if '530' in str(tcp.data):
#					packets2.append(ts)
#					attempts.append(count)
#					count += 1
#				if 'Echo' in str(tcp.data):
#					print 'Ping Detected'
	#  Check to see if the attack is a port scan or password attack.
	if len(attempts) < 10:
		plot_graph1(ports, packets1, in_ip)
	else:
		plot_graph2(attempts, packets2, in_ip)
main(sys.argv[1], sys.argv[2])