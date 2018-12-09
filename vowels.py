f = open('Test.txt','a+')
for line in f.readlines():
	if 'a' in line:
		f.write(line.replace('a','e'))
	elif 'e' in line:
		f.write(line.replace('e','i'))
	elif 'i' in line:
		f.write(line.replace('i','o'))
	elif 'o' in line:
		f.write(line.replace('o','u'))
	elif 'u' in line:
		f.write(line.replace('u','a'))
	else:	
		print("No vowels found")



