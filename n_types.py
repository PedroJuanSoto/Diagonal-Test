import numpy as np
from sympy import factorint 

def create_N_zig_zag(n):
	N = []
	if n % 2 == 0:
		for i in range(n//2):
			N.append(n//2 + i*(-1))
			N.append(n//2 + i +1)
	else:
		for i in range(n//2):
			N.append(n//2 + i +1)
			N.append(n//2 + i*(-1))
		N.append(n)
	return N

def create_N_random(n):
	N = np.random.permutation(n) 
	for i in range(n):
		N[i] += 1
	return N

def create_N_diagonal(n):
	N = [] 
	for i in range(n):
		N.append(i+1)
	return N



def create_N_zig_zag_general(n):
	N = [1]
	factors = factorint(n)
	for x in list(factors):
		for y in range(factors[x]):
			new_list = create_N_zig_zag(x)
			NN = [] 
			d = len(N)
			for z in new_list:
				for t in N:
					NN.append((z-1)*d + t)
			N = NN	
	return N


