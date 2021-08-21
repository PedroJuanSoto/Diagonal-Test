from q_type import diagonal_test, create_Q, benchmark
from n_types import create_N_zig_zag, create_N_random, create_N_diagonal, create_N_zig_zag_general
from p_types import gen_arith_prog

n =  23
b = 0
D = [2,7,17,37,83]
L = [2,2,2,2,2]

N = create_N_zig_zag(n)
#N = create_N_random(n)
#N = create_N_diagonal(n)
#N = create_N_zig_zag_general(n)
P = gen_arith_prog(n,b,D,L)

count, Q = create_Q(P,N)
print(count)
print(benchmark(n))
print(N)
print(P,Q)


