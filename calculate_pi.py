def calpi(n,p = 0.0): #created function which takes two arguments 
	for i in range(1,n+1): #loop for calculating pi as per range
	    if(i%2==0): #differencing odd and even numbers
		p -= (4.0/(2*i-1)) #one number is subtracted
	    else:
		p += (4.0/(2*i-1)) # one number is added
	print("Calculated pi:")
	print(p) #calculated pi

number = raw_input("Enter number for calulating pi:") #taking user input
if number.isdigit() == True: #checking user input is digit is not
	number = int(number) #converting string to integer
	if(number > 0): #if number is greater tha zero than above function is called
	   calpi(number)
	else:
	  print("Please enter number greater than zero")
else:
  print("Please enter a natural number")
	
	
#******TEST CASES*****

#Testcase1:Enter number for calulating pi:5
#Output= Calulated pi:
#        3.33968253968

#Testcase2:Enter number for calulating pi:0
#Output=Please enter number greater than zero

#Testcase3:Enter number for calulating pi:-55
#Output=Please enter a natural number

#Testcase4:Enter number for calulating pi:6.99
#Output=Please enter a natural number

#Testcase5:Enter number for calulating pi:abc
#Output=Please enter a natural number

#Testcase6:Enter number for calulating pi:1
#Output=Calculated pi
#	4.0


    
