l = 0

def max_func(a,b,c):
	if a  >  b and a > c:
		l = a
	elif b > a and b > c:
		l = b
	elif c > a and c > b:
		l = c

	print l
	v = str(l)
	#print v*2
	#for i in range(100):   # print copies of the answer
	#	print l
max_func(7,8,5)	 
			
		
	
