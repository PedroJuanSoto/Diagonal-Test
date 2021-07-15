import numpy as np

def create_N_zig_zag(n):
	N = []
	for i in range(n//2):
		N.append(n//2 + i*(-1))
		N.append(n//2 + i +1)
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
