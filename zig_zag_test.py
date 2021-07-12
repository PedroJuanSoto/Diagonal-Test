import math
from sympy import sieve

def diagonal_test(P,N,Q,k):
	diagonal = [] 
	for i in range(len(Q)):
		diagonal.append(P[N[i]-1] + Q[i])
	for p in P:
		if p + k in diagonal:
			return False
	return True 

def create_Q(P,N):
	Q = []
	k = 0
	n = len(P)
	while len(Q) < n:
		if diagonal_test(P,N,Q,k) == True:
			Q.append(k)
		k +=1
	return Q


n = 2**3
N = []
P = []

for i in range(n):
	P.append(sieve[i+1])

delta = []
for i in range(n/2):
	delta.append(n/2 - 2*i)
	delta.append(n/2 - 2*i)

for i in range(1,n/2+1):
	N.append(int(n/2 + i*(-1)**(i+1)))

#Q = create_Q(P,N)
#print(max(Q)+max(P))
#print(3**math.log(n,2))
print(N)
#print(P,Q)
