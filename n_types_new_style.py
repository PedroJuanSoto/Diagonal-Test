
def create_N_zig_zag_new_style(n):
	N = []
	if n % 2 == 0:
		for i in range(n//2):
			N.append(n - i)
			N.append(n//2 -i)
	else:
		for i in range(n//2):
			N.append(n//2 -i+1)
			N.append(n - i)
		N.append(1)
	return N

