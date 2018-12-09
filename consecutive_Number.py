#Display sum of repeating numbers
#Mrunali prn-23

import re
data = open("givenFile","r").read()  #opening file and reading it
data = re.findall('[^\n\t\s\r\f\v]',data) #removing new line char,tabchar,specialchar,etc
sum1=0
for i in range(len(data)-1):
	if data[i] == data[i+1]:  # checking for same numbers
		s = data[i]+data[i+1]	#adding same numbers to variable
		sum1+= int(s) 	# coverting string to numbers and adding it 
print("Sum of numbers=")
print(sum1)	#printing sum of numbers
