

from q_type import diagonal_test, create_Q, benchmark
from n_types import create_N_zig_zag, create_N_random, create_N_diagonal, create_N_zig_zag_general
from p_types import gen_arith_prog
from npq_printer import npq_printer

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

count, test = npq_test(M,N,P,Q)
print(count)
print(test)
print(benchmark(n))
print(N)
print(P,Q)
M = []
for i in range(n):
	M.append(i+1)
npq_printer(M,N,P,Q)
