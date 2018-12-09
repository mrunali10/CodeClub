#Display unique lines like unique command displays in linux
#Mrunali prn-23


data = open("givenFile","r").read().splitlines() #reading line from file and splitting
for i in range(len(data)): 
	if i == 0:
		print(data[i]) 
	elif data[i] == data[i-1]:	#checking for unique lines
		continue
	else:
		print(data[i])		#printing unique lines
	
