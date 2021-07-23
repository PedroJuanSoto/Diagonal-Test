P = [1, 2, 3, 5, 6, 7, 9, 11, 12, 14, 17]
Q = [0, 2, 7, 10, 17, 23, 30, 35, 42, 46, 50]
N = [1,2,3,4,5,6,7,8,9,10,11]
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




