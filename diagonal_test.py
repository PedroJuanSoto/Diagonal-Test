
import n_types
import p_types
import sys
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

n = int(sys.argv[1])


if sys.argv[2] == "diagonal":
	N = n_types.create_N_diagonal(n)
elif sys.argv[2] == "zigzag":
	N = n_types.create_N_zig_zag_general(n)
elif sys.argv[2] == "random":
	N = n_types.create_N_random(n)

if sys.argv[3] == "prime":
	P = p_types.create_P_prime(n)
elif sys.argv[3] == "mults":
	P = p_types.create_P_multiples(n,int(sys.argv[4]))
elif sys.argv[3] == "random":
	P = p_types.create_P_random(n,int(sys.argv[4]))

if sys.argv[5] == "permute_P":
	P = p_types.permute_P(P)

Q = create_Q(P,N)
print(max(Q)+max(P))
print(benchmark(n))
print(N)
print(P,Q)
