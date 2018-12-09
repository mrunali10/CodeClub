#Read file transform each word in following way:
#Hello world->ZelloH zorldw
#Mrunali Patel-023
filepath = input("Enter file path:")  #takes file path from user
try:
   f=open(filepath,"r") 		#opens a file
   for line in f:			#reads lines of file
	for splits in line.split(" "):  #splits words			
		halfword = splits[1:len(splits)] + splits[:1] #add first letter to last
		if halfword[-1:].isupper()==True:	#checks case
			print("Z"+halfword)		
		else:
			if(halfword.isspace()==False):
			  print("z"+halfword)
except:
   print("Please enter proper filename")
