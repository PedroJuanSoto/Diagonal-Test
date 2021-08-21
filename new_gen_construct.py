import sys
from q_type import diagonal_test, create_Q, benchmark
from n_types import create_N_zig_zag, create_N_random, create_N_diagonal, create_N_zig_zag_general
from p_types import gen_arith_prog
from sympy import factorint 
from npq_test import npq_test
from npq_printer import npq_printer



def create_P_arith_prog(n):
	D = [1]
	L = []
	r = 1
	factors = factorint(n)
	for x in list(factors):
		for y in range(factors[x]):
			r *= int((x+1)**2/2)-1
			D.append(r)
			L.append(x)	
	D.pop()
	return D, L

def create_N_zig_zag_new_style(n):
	N = []
	if n % 2 == 0:
		for i in range(n//2):
			N.append(n - i)
			N.append(1 + i)
	else:
		for i in range(n//2):
			N.append(n - i)
			N.append(1 + i)
		N.append(n//2+1)
	return N


def create_N_zig_zag_general_new_style(n):
	N = [1]
	factors = factorint(n)
	for x in list(factors):
		for y in range(factors[x]):
			new_list = create_N_zig_zag_new_style(x)
			NN = [] 
			d = len(N)
			for z in new_list:
				for t in N:
					NN.append((z-1)*d + t)
			N = NN	
	return N

n = int(sys.argv[1])
want_print = False
if sys.argv[2] == 'True':
	want_print = True

N = create_N_zig_zag_general_new_style(n)
D, L = create_P_arith_prog(n)
if want_print == True:
	print(D,L)
P = gen_arith_prog(n,0,D,L)
if want_print == True:
	print(P)
Q = create_Q(P,N)
if want_print == True:
	print(N)
if want_print == True:
	print(P,Q)
M = []
for i in range(n):
	M.append(i+1)

count, test = npq_test(M,N,P,Q)
print(count)
print(test)
print(benchmark(n))
if want_print == True:
	npq_printer(M,N,P,Q)
	
