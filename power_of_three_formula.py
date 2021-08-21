
from q_type import benchmark

def diagonal_test(P, k, diagonal):
	for p in P:
		if p + k in diagonal:
			return False
	return True 

def create_table(n):
	P = [0]
	k = 1
	diagonal = set() 
	diagonal.add(0)
	while len(P) < n:
		if diagonal_test(P,k, diagonal) == True:
			P.append(k)
			diagonal.add(2*k)
		k +=1
	return P

def plus_one(S):
	have_i_added = False
	i = 0
	while i < len(S) and have_i_added == False:
		if S[i] == 0:
			S[i] +=1
			have_i_added = True
		i += 1
	for j in range(i-1):
		S[j] = 0
	if have_i_added == False:
		S.append(1)
		S[i-1] =0
	return S


def base_two(S):
	n = 0 
	for i,s in enumerate(S):
		n+= s*2**i
	return n

def power_two_test(S):
	count = 0 
	for s in S:
		if s == 1:
			count += 1
	if count > 1:
		return False
	return True

def base_three_recovery(S):
	n = 0 
	found_one = False
	index = 0
	for i,s in enumerate(S):
		if s != 0 and found_one == False:
			n+= S[i]*3**i
			found_one = True
			index = i
	for i,s in enumerate(S):
		if i > index:
			n+= 2*S[i]*3**i
	return n 


N = 20
S = [0]

for i in range(N):
	S = plus_one(S)
	n = base_two(S)
	m = base_three_recovery(S)
	P = create_table(n)
	r = 2*P[n-1]+1 
	print(S,n,m,r)
