#Display user's name from /etc/passwd file
#Mrunali prn-23


data = open("/etc/passwd","r").readlines() #reading lines from file /etc/passwd
for line in data:          
	lines = line.split(":") #splitting names by ":"
	print(lines[0])		#printing user names



