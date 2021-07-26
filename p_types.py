import numpy as np
from sympy import sieve

def create_P_prime(n):
	P = []
	for i in range(n):
		P.append(sieve[i+1])
	return P


def create_P_multiples(n, multiple):
	P = [] 
	for i in range(n):
		P.append(multiple*i)
	return P

def create_P_random(n, step_size):
	p = 0 
	P = []
	p += np.random.randint(step_size)
	P.append(p)
	for i in range(n-1):
		p += np.random.randint(1,step_size)
		P.append(p)
	return P	


def permute_P(P):
	permute = np.random.permutation(len(P)) 
	new_P = []
	for i in range(len(P)):
		new_P.append(P[permute[i]])
	return new_P

def gen_arith_prog(n,b,D,L):
	D_len = len(D)
	L_len = len(L)
	if L_len != D_len:
		return 'error'
	test = 1
	current_l = []
	P_set = set()
	P_set.add(b)
	for i in range(D_len):
		new_list = list(P_set)
		for j in range(L[i]):
			for l in new_list:
				P_set.add(l+j*D[i])
	P = list(P_set)
	P.sort
	P = P[:n]
	return P
	


print(gen_arith_prog(8,5,[2,3],[4,5]))

