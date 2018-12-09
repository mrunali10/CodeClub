#Display files from a directory which are created in last 20 minutes
#Mrunali Patel, prn-023


import os
import time
import datetime
dt = datetime.datetime.now()
ago = dt - datetime.timedelta(minutes=20)
for root,dirs,files in os.walk('/home/monu/python scripts/'):
	for name in files:
		path = os.path.join(root,name)		
		st = os.stat(path)
		mtime = datetime.datetime.fromtimestamp(st.st_mtime)
		if mtime > ago: 
			print(name)		

	

