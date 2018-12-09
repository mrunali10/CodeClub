#Display epoch time from time given
#Mrunali Patel, prn-023

from datetime import datetime
seconds = input("Enter number of seconds=") # taking millisec from user on which any file created
result = datetime.fromtimestamp(seconds) # calculating time 
print(result)




