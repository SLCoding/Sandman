#!/usr/bin/env python

import socket
import struct

def wake_on_lan(macaddress):
	""" Switches on remote computers using WOL. """
	if len(macaddress) == 12 + 5:
	sep = macaddress[2]
		macaddress = macaddress.replace(sep, '')
	else:
		raise ValueError('Incorrect MAC address format')

	data = ''.join(['FFFFFFFFFFFF', macaddress * 20])
	send_data = '' 

	for i in range(0, len(data), 2):
		send_data = ''.join( [send_data, struct.pack('B', int(data[i: i + 2], 16))] )

	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
	sock.sendto(send_data, ('<broadcast>', 7))   

if __name__ == '__main__':
	wake_on_lan('00:27:0e:2f:0b:77')