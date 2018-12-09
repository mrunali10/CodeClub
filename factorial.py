n = raw_input("Enter number for which you want factorial:") #taking input from user 
if n.isdigit() == True: #checking user input that its digit or not
    n = int(n) #converting string to integer
    if(n > 0): #checking user input to be greater than zero
       factorial = 1 
       for i  in range(1,n+1): #loop calculating for factorial
	  factorial = factorial * i  #factorial
       print("Factorial:")
       print(factorial) #print the factorial 
    else:
      print("Please enter a number greater than zero")
else:
   print("Please enter valid natural number") 



#**********Test Cases**********
#Testcase1:Enter number for which you want factorial:0
#Output=Please enter a number greater than zero

#Testcase2:Enter number for which you want factorial:4
#Output=Factorial:
#        24

#Testcase3:Enter number for which you want factorial:-66
#Output=Please enter valid natural number

#Testcase4:Enter number for which you want factorial:9.55
#Output=Please enter valid natural number

#Testcase5:Enter number for which you want factorial:abc
#Output=Please enter valid natural number

#Testcase6:Enter number for which you want factorial:1
#Output=Factorial:
#       1
