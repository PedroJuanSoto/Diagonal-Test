
from q_type import diagonal_test, create_Q_less_greedy, benchmark
import n_types
import p_types
import sys
import math
import numpy as np
from sympy import sieve


n = int(sys.argv[1])
q_step = int(sys.argv[5])

if sys.argv[2] == "diagonal":
	N = n_types.create_N_diagonal(n)
elif sys.argv[2] == "zigzag":
	N = n_types.create_N_zig_zag(n)
elif sys.argv[2] == "random":
	N = n_types.create_N_random(n)

if sys.argv[3] == "prime":
	P = p_types.create_P_prime(n)
elif sys.argv[3] == "mults":
	P = p_types.create_P_multiples(n,int(sys.argv[4]))
elif sys.argv[3] == "random":
	P = p_types.create_P_random(n,int(sys.argv[4]))

count, Q = create_Q_less_greedy(P,N,q_step)
print(count)
print(benchmark(n))
print(N)
print(P,Q)
