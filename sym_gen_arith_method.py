
from q_type import diagonal_test, create_Q, benchmark
from n_types import create_N_zig_zag, create_N_random, create_N_diagonal, create_N_zig_zag_general
from p_types import gen_arith_prog

k = 4
b = 0
n = 2**k 

def sym_gen_arith_prog(k):
	D = [1]
	L = [2]
	for i in range(k-1):
		r = 0 
		for d in D:
			r += d
		D.append(2*r+1)
		L.append(2)	
	return D, L

D, L = sym_gen_arith_prog(k)	
N = create_N_zig_zag_general(n)
P = gen_arith_prog(n,b,D,L)

Q = create_Q(P,N)
print(max(Q)+max(P)+1)
print(benchmark(n))
print(N)
print(P,Q)

