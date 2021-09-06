import sys
import math
from npq_printer import npq_printer

def npq_test_and_count(M,N,P,Q):
	n = len(N)
	if len(P) != n:
		return False
	if len(Q) != n:
		return False
	diagonal = set()
	non_rooks = set()
	for i in range(n):
		for j in range(n):
			if M[i] != N[j]:
				non_rooks.add(P[i]+Q[j])
			else:
				diagonal.add(P[i]+Q[j])
	if len(diagonal.intersection(non_rooks)) != 0:	
		return diagonal.union(non_rooks), len(diagonal)+len(non_rooks), False
	if len(diagonal) != n:
		return diagonal.union(non_rooks), len(diagonal)+len(non_rooks), False
	return diagonal.union(non_rooks), len(diagonal)+len(non_rooks), True

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
exponents, count, test = npq_test_and_count(M,M,P,P)
print(exponents)
print(count)
print(test)
print(P)
if  sys.argv[2] == 'print':
	npq_printer(M,M,P,P)




