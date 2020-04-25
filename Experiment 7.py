A = int(input("Enter number: "))
al,bl = [],[]

for i in range(A+1):
	for j in range (A+1):
		if (i*i + j*j) == A:
			a,b = i,j
			#For not repeating interchanged values of a and b
			al.append(a)
			bl.append(b)
			if b in al and a in bl: continue
			print('a = {},b = {}'.format(a,b))