import os
import time
import argparse
import sys

parser = argparse.ArgumentParser(description='Please fill out option info, follow as :')

parser.add_argument('--host', required=True, help='Host or IP of Redfish server')
parser.add_argument('--port', required=True, help='Port of Redfish server')
parser.add_argument('--dir', required=True, help='Directory of Redfish server')
parser.add_argument('--time', required=True, type=float, help='Time period of each testing')
args = parser.parse_args()
#parameter spec
sleeptime = args.time
target_dir = args.dir
host = args.host + ':'
port = args.port
#user = 
#password = 

def auto_testing():
	for dirname, dirnames, filenames in os.walk(target_dir):
		print(dirname)
		str_info = dirname[6:]
		if 'redfish/v1' in str_info: 
			cmd = 'curl http://'+ host + port + str_info
			print('###################################################')
			print('Auto testing Get cmd for all dir')
			print('Target Host : ', host)
			print('Target Port : ', port)
			print('check point : name = ', str_info)
			print('###################################################')
			print(os.system(cmd))
			time.sleep(sleeptime)

def get_testList():
	index = 1
	for dirname, dirnames, filenames in os.walk(target_dir):
		str_info = dirname[6:]
		if 'redfish/v1' in str_info:
			print(index,'->', str_info)
			index = index + 1
	

def printProgress (iteration, total, prefix = '', suffix = '', decimals = 1, barLength = 100): 
	formatStr = "{0:." + str(decimals) + "f}" 
	percent = formatStr.format(100 * (iteration / float(total))) 
	filledLength = int(round(barLength * iteration / float(total))) 
	bar = '#' * filledLength + '-' * (barLength - filledLength) 
	sys.stdout.write('\r%s |%s| %s%s %s' % (prefix, bar, percent, '%', suffix)), 
	if iteration == total: 
		sys.stdout.write('\n') 
	sys.stdout.flush()


#main
for i in range(0, 100):
	printProgress(i, 100, 'Loading for Auto Testing :', 'Complete', 1, 50)
	time.sleep(0.04)
print('\n')
print("Test Start...")
print("First, Checker Target list")
time.sleep(0.5)
get_testList()

print('Start Auto Testing')
for i in range(0, 2000000000):
	auto_testing()




