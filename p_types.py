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


P = create_P_prime(9)
P = permute_P(P)
print(P)
