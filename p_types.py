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
	for i in range(n):
		p += np.random.randint(1,step_size)
		P.append(p)
	return P	
