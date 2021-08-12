
from q_type import diagonal_test, create_Q, benchmark
from n_types import create_N_zig_zag, create_N_random, create_N_diagonal, create_N_zig_zag_general
from p_types import gen_arith_prog
from sympy import factorint 
from npq_test import npq_test
from npq_printer import npq_printer


def psuedo_arith_prog(n,b,D,L):
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
		for j in L[i]:
			for l in new_list:
				P_set.add(l+j*D[i])
	P = []
	for p in P_set:
		P.append(p)
	P.sort()
	P = P[:n]
	return P



def create_Q_psuedo_arith_prog(n):
	factors = factorint(n)
	first_p = list(factors)[0]
	D = []
	L = []
	simple_Q = simple_prime_P_N(first_p)
	factors[first_p] += -1
	L.append(simple_Q)
	D.append(1)
	d = int((first_p+1)**2/2)-1
	for x in list(factors):
		for y in range(factors[x]):
			simple_Q = simple_prime_P_N(x)
			D.append(d)
			L.append(simple_Q)
			d *= int((x+1)**2/2)-1
	Q = psuedo_arith_prog(n,0,D,L)	
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
	
n = 12
D, L = create_P_arith_prog(n)
print(D,L)
P = gen_arith_prog(n,0,D,L)
print(P)
#DD, LL = create_Q_arith_prog(n)
#print(DD,LL)
#Q = gen_arith_prog(n,0,DD,LL)
Q = create_Q_psuedo_arith_prog(n)
print(Q)
N = create_N_zig_zag_general(n)
M = []
for i in range(n):
	M.append(i+1)
print(npq_test(M,N,P,Q))
print(max(P)+max(Q)+1)
print(benchmark(n))
npq_printer(M,N,P,Q)
