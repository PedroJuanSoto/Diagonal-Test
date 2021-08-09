
def npq_printer(M,N,P,Q):
	table = [] 
	non_rook = []
	rook = []
	QQ = ['*']
	for q in Q:
		QQ.append(str(q))
	table.append(QQ)
	for i in range(len(P)):
		listy = []
		listy.append(str(P[i]))
		for j in range(len(Q)):
			if M[i] != N[j]:
				listy.append(str(P[i]+Q[j]))
			else:
				listy.append('*'+str(P[i]+Q[j]))
		table.append(listy)

	maxx = 0
	for x in table:
		for y in x:
			if len(y) > maxx:
				maxx = len(y)
	formatted_list = []
	for x in table:
		list_helper = []
		for y in x:
			if len(y) < maxx:
				u = ' '
				for i in range(maxx - len(y) - 1):
					u = ' ' + u 
				u = u + y 	
			else:
				u = y 
			list_helper.append(u)
		formatted_list.append(list_helper)
		
	for x in formatted_list:
		print(x)




