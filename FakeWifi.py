# coding=UTF-8

# We have to change the ‘mode’ from ‘Managed‘ to ‘monitor‘.
# https://taufanlubis.wordpress.com/2010/05/14/how-to-fix-ioctlsiocsiwmode-failed-device-or-resource-busy-problem/
# sudo ifconfig wlan0 down
# sudo iwconfig wlan0 mode monitor
# sudo ifconfig wlan0 up
# sudo iwconfig wlan0
import sys, getopt, json, time, commands
from subprocess import Popen
from pprint import pprint
from random import randint
physicalCard = 'wlan0'
def startFakeWifi(argv):


	duration = 4
	fileName = ""
	now_aps = []
	if len(argv) > 2 :
		fileName = argv[1]
		duration = argv[2]
	else :
		print "usage: <jsonFileName> <duration>"
		print len(argv)
		exit();
	print fileName + ' with duration:'+duration
	

	commands.getoutput("ifconfig "+physicalCard+" down")
	commands.getoutput("iwconfig "+physicalCard+" mode monitor")
	commands.getoutput("ifconfig "+physicalCard+" up")
	while 2>1:
		with open(fileName) as data_file:    
		    path = json.load(data_file)
		for point in path:
			for mProcess in now_aps:
				mProcess.kill()
			now_aps = []
			for ap in point['aps']:
				now_aps.append(openWifiHotspot(ap['SSID'], ap['BSSID'], randint(2,10)))
			print '#{:d}:{:d}aps'.format(point['order'],len(point['aps'])) 
			time.sleep(float(duration))
def openWifiHotspot(ssid, macAd, channel):
	m_argcs = ['airbase-ng',
				'-c', str(channel), '-e', ssid, '-a', macAd, physicalCard]
	r = Popen(m_argcs)
	#print str(r)
	#print r.pid
	#print r.poll()
	return r
if __name__ == "__main__":
	startFakeWifi(sys.argv)

