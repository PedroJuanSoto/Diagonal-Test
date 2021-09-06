
from q_type import diagonal_test, create_Q, benchmark
from n_types import create_N_zig_zag, create_N_random, create_N_diagonal, create_N_zig_zag_general
from p_types import gen_arith_prog
from sympy import factorint 
from npq_test import npq_test_and_count
from npq_printer import npq_printer




def create_Q_dyn_prog(n):
	factors = factorint(n)
	first_p = list(factors)[0]
	Q = simple_prime_P_N(first_p)
	factors[first_p] += -1
	d = int((first_p+1)**2/2)-1
	for x in list(factors):
		for y in range(factors[x]):
			print(Q)
			new_list = simple_prime_P_N(x)
			QQ = [] 
			for z in new_list:
				for t in Q:
					QQ.append(z*d + t)
			d *= int((x+1)**2/2)-1
			Q = QQ	
	return Q

def simple_prime_P_N(p):
	P = []
	for i in range(p):
		P.append(i)
	N = create_N_zig_zag(p)
	Q = create_Q(P,N)
	return Q



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
	
n = 5
D, L = create_P_arith_prog(n)
print(D,L)
P = gen_arith_prog(n,0,D,L)
print(P)
count, Q = create_Q_dyn_prog(n)
print(Q)
N = create_N_zig_zag_general(n)
M = []
for i in range(n):
	M.append(i+1)
count, test = npq_test_and_count(M,N,P,Q)
print(count)
print(test)
print(benchmark(n))
npq_printer(M,N,P,Q)
