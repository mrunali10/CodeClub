#Validate Password
#12 characters long ,at least one uppercase, at least one lowercase, special character, at least one digit
#Mrunali Patel -023
import re
password = input("Enter Password:")
if len(password) < 12:
	print("Password must be at least 12 characters long")
else:		
	pattern = "((?=.*\d)(?=.*\w)(?=.*[A-Z])(?=.*[0-9]){12})"
	validation = re.findall(pattern,password)
	if len(validation) == 0:
		print("Please enter proper password as specified")
	else:
		print(str(validation))
		
	
