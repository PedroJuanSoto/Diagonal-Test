import math
from sympy import sieve
from sympy import factorint 

def diagonal_test(P,N,Q,k,diagonal,non_rooks):
	for p in P:
		if p + k in diagonal:
			return False
	if P[N[len(Q)]-1] + k in non_rooks:
		return False
	return True 

def create_Q(P,N):
	Q = []
	k = 0
	n = len(P)
	diagonal = set()
	non_rooks = set()
	while len(Q) < n:
		if diagonal_test(P,N,Q,k,diagonal,non_rooks) == True:
			diagonal.add(P[N[len(Q)]-1] + k)
			for i in range(N[len(Q)]):
				non_rooks.add(P[N[i]-1] + k)
			for i in range(N[len(Q)]+1,len(P)):
				non_rooks.add(P[N[i]-1] + k)
			Q.append(k)
		k +=1
	return Q

def benchmark(n):
	factors = factorint(n)
	z = 1
	for x in list(factors):
		for y in range(factors[x]):
			z *= math.floor((x+1)**2/2)-1		
	return z
