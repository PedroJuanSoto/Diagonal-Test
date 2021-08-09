P = [0, 1, 2, 7, 8, 9, 14, 15, 16]
Q = [0, 3, 4, 20, 23, 24, 27, 30, 31]
N = [5, 4, 6, 2, 1, 3, 8, 7, 9]
M = [1,2,3,4,5,6,7,8,9]
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

print("M = ", M)
print("N = ", N)
for x in table:
	print(x)

