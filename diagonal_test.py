import math

def diagonal_test(P, k):
	diagonal = [] 
	for i in range(len(P)):
		diagonal.append(2*P[i])
	for p in P:
		if p + k in diagonal:
			return False
	return True 

def create_table(n):
	P = [0]
	k = 1
	while len(P) < n:
		if diagonal_test(P,k) == True:
			P.append(k)
		k +=1
	return P

n = 2**10
P = create_table(n)
print(2*P[n-1])
print(3**math.log(n,2))
