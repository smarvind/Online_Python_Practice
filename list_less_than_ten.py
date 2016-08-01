a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


#b = a[0:4]
#for i in b:
#	print i

c = raw_input("Enter a number:")
l = []
for i in a:
	if int(i) < int(c):
		l.append(i)
print l
