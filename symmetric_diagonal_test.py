import sys
import math

def diagonal_test(P, k, diagonal):
	for p in P:
		if p + k in diagonal:
			return False
	return True 

def create_table(n):
	P = [0]
	k = 1
	diagonal = set() 
	diagonal.add(0)
	while len(P) < n:
		if diagonal_test(P,k, diagonal) == True:
			P.append(k)
			diagonal.add(2*k)
		k +=1
	return P

k = int(sys.argv[1])
n = 2**k
P = create_table(n)
print(2*P[n-1])
print(3**math.log(n,2))
