import sys
import math
from npq_test import npq_test
from npq_printer import npq_printer

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

n = int(sys.argv[1])
P = create_table(n)
M = []
for i in range(n):
	M.append(i+1)
count, test = npq_test(M,M,P,P)
print(count)
print(test)
print(P)
