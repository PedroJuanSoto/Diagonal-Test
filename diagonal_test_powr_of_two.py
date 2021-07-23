import n_types
import p_types
import sys
import math
from sympy import sieve

def diagonal_test(P,N,Q,k,diagonal):
	diagonal = [] 
	for i in range(len(Q)):
		diagonal.append(P[N[i]-1] + Q[i])
	for p in P:
		if p + k in diagonal:
			return False
	return True 

def create_Q(P,N):
	Q = []
	k = 0
	n = len(P)
	diagonal = set()
	while len(Q) < n:
		if diagonal_test(P,N,Q,k,diagonal) == True:
			diagonal.add(P[N[len(Q)]-1] + k)
			Q.append(k)
		k +=1
	return Q


k = int(sys.argv[1])
n = 2**k

if sys.argv[2] == "diagonal":
	N = n_types.create_N_diagonal(n)
elif sys.argv[2] == "zigzag":
	N = n_types.create_N_zig_zag(n)
elif sys.argv[2] == "random":
	N = n_types.create_N_random(n)

if sys.argv[3] == "prime":
	P = p_types.create_P_prime(n)
elif sys.argv[3] == "mults":
	P = p_types.create_P_multiples(n,int(sys.argv[4]))
elif sys.argv[3] == "random":
	P = p_types.create_P_random(n,int(sys.argv[4]))

Q = create_Q(P,N)
print(max(Q)+max(P))
print(3**math.log(n,2))
#print(N)
#print(P,Q)
