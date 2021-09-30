def rooks(M,N,P,Q,n):
	rooks = set()
	for i in range(n):
		for j in range(n):
			rooks.add(P[i]+Q[j])
	exponents = list(rooks)
	return exponents 

