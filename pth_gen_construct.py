

from q_type import diagonal_test, create_Q, benchmark
from n_types import create_N_zig_zag, create_N_random, create_N_diagonal, create_N_zig_zag_general
from p_types import gen_arith_prog

k = 2
b = 0
p = 3
n = p**k 

def pth_gen_arith_prog(p,k):
	D = []
	L = []
	for i in range(k):
		D.append((int((p+1)**2/2)-1)**i)
		L.append(p)	
	return D, L

D, L = pth_gen_arith_prog(p,k)	
N = create_N_zig_zag_general(n)
P = gen_arith_prog(n,b,D,L)

Q = create_Q(P,N)
print(max(Q)+max(P)+1)
print(benchmark(n))
print(N)
print(P,Q)

