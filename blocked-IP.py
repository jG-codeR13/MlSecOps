import os
with open("/root/mlops-task-5/blocked.txt","r") as file1:
	for i in file1:
		os.system('iptables -A INPUT -s {} -j DROP'.format(i.rstrip('\n')))
	os.system('systemctl iptables save')
