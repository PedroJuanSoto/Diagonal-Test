
from q_type import benchmark
from npq_printer import npq_printer

def npq_test_and_count(M,N,P,Q):
	n = len(N)
	if len(P) != n:
		return False
	if len(Q) != n:
		return False
	diagonal = set()
	non_rooks = set()
	for i in range(n):
		for j in range(n):
			if M[i] != N[j]:
				non_rooks.add(P[i]+Q[j])
			else:
				diagonal.add(P[i]+Q[j])
	if len(diagonal.intersection(non_rooks)) != 0:	
		return len(diagonal)+len(non_rooks), False
	if len(diagonal) != n:
		return len(diagonal)+len(non_rooks), False
	return len(diagonal)+len(non_rooks), True

n = 5

N = [1,5,2,4,3]
P = [0,4,7,5,1]
Q = [0,2,4,5,11]
M = []
for i in range(n):
	M.append(i+1)
count, test = npq_test_and_count(M,N,P,Q)
print(count)
print(test)
print(benchmark(n))
npq_printer(M,N,P,Q)


