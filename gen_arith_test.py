from q_type import diagonal_test, create_Q, benchmark
from n_types import create_N_zig_zag, create_N_random, create_N_diagonal, create_N_zig_zag_general
from p_types import gen_arith_prog

n = 83 
b = 0
D = [2,7,13,17]
L = [7,7,5,5]

N = create_N_zig_zag_general(n)
P = gen_arith_prog(n,b,D,L)

Q = create_Q(P,N)
print(max(Q)+max(P)+1)
print(benchmark(n))
print(N)
print(P,Q)


