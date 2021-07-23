P = [3,4,5,7,9,10,12,15,16,17,18]
Q = [0,2,9,10,15,19,22,24,30,36,39]
N = [6,5,7,4,8,3,9,2,10,1,11]
M = [1,2,3,4,5,6,7,8,9,10,11]
table = [] 
non_rook = []
rook = []
for i in range(len(P)):
	listy = []
	for j in range(len(Q)):
		if M[i] != N[j]:
			listy.append(P[i]+Q[j])
		else:
			listy.append(str(P[i]+Q[j]))
	table.append(listy)


for x in table:
	print(x)
