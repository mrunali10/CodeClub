cnt = { }
for line in open('Test.txt' , 'r'):
	for w in line.split():
		try:
			cnt[w] += 1
		except:
			cnt[w] = 1

print(cnt)



