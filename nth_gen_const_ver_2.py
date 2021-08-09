
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
		for j in range(L[i]):
			for l in new_list:
				P_set.add(l+j*D[i])
	P = []
	for p in P_set:
		P.append(p)
	P.sort()
	P = P[:n]
	return P


def create_Q_dyn_prog(n):
	factors = factorint(n)
	first_p = list(factors)[0]
	Q = simple_prime_P_N(first_p)
	print(factors)
	factors[first_p] += -1
	print(factors)
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

def create_Q_psuedo_arith_prog(n):
	factors = factorint(n)
	first_p = list(factors)[0]
	D = []
	L = []
	Q = simple_prime_P_N(first_p)
	factors[first_p] += -1
	first_l = max(Q)
	L.append(first_l)
	D.append(1)
	d = int((first_p+1)**2/2)-1
	for x in list(factors):
		for y in range(factors[x]):
			D.append(d)
			L.append(x)
			d *= int((x+1)**2/2)-1
	Q = psuedo_arith_prog()	
	return Q




def create_Q_arith_prog(n):
	factors = factorint(n)
	first_p = list(factors)[0]
	N = create_N_zig_zag(first_p)
	P = []
	for i in range(first_p):
		P.append(i)
	DDD = create_Q(P,N)
	r = 1
	DD = []
	for x in list(factors):
		for y in range(factors[x]):
			r *= int((x+1)**2/2)-1
			for d in DDD:
				DD.append(r+d)
	D = DDD + DD 
	return D


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
	
n = 18 
D, L = create_P_arith_prog(n)
print(D,L)
P = gen_arith_prog(n,0,D,L)
print(P)
#DD, LL = create_Q_arith_prog(n)
#print(DD,LL)
#Q = gen_arith_prog(n,0,DD,LL)
Q = create_Q_dyn_prog(n)
print(Q)
N = create_N_zig_zag_general(n)
M = []
for i in range(n):
	M.append(i+1)
print(npq_test(M,N,P,Q))
print(max(P)+max(Q)+1)
print(benchmark(n))
npq_printer(M,N,P,Q)
