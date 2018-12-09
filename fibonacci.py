n = raw_input("Enter range for fibonacci series:") #taking user input which is string

if n.isdigit() == True: #checking that the user input is not float,string or negetive
	n = int(n)  #converting the string input from user to integer
	if(n > 0): #checking for the number greater than zero

		startingvalue = 0
		nextvalue = 1
		if(n==1): #if user input will be 1 then directly printing firstvalue
		    print(startingvalue)
		else:
	 	   print(startingvalue) #printing 0 and 1 directly for fibonacci
	           print(nextvalue)
		   for i in range(2,n): #loop for iterating through the given range
			total = startingvalue + nextvalue #adding startingvalue to nextvalue for getting fibonacci series
			startingvalue = nextvalue      #swapping values
			nextvalue = total
			print(total)  #printing fibonacci series
	else:
	  print("Please enter number greater than zero")
	
else: 
   print("Please enter valid number as input.")	






#******TESTCASES******
#Test case1:Enter range for fibonacci series:0
#Output=Please enter number greater than zero

#Test case2:Enter range for fibonacci series:1
#Output=0

#Test case3:Enter range for fibonacci series:-77
#Output=Please enter valid natural number

#Test case4:Enter range for fibonacci series:abc
#Output=Please enter valid natural number

#Test case5:Enter range for fibonacci series:4.55
#Output=Please enter valid natural number

#Test case6:Enter range for fibonacci series:5
#Output=0
#	1
#	1
#	2
#	3
