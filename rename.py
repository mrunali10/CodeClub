#Take directory path from user and take all files and replace spaces with '_' in filename
#Mrunali Patel prin-023
import os
path  = input("Enter the path of your directory:")
if os.path.exists(path)==True:
	os.chdir(path)
	for files in os.listdir(path):
		if ' ' in files:
			tmp = files.replace(' ', '_')
			os.rename(files,tmp)                           
	os.system('ls')	
else:
   print("Directory does not exists please enter existing directory")





