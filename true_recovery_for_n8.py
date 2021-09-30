
import math

def power_two_test(k):
	i = 1
	while i <= k:
		i *=2	
	if i == k:
		return True
	else:
		return False

def r_col(i,n):
	if i > n:
		return 0
	elif i == 1:
		return n 
	elif i <= n//2:
		return 2*r_col(i,n//2)
	elif i<= n:
		return r_col(i-n//2,n//2) 
	else:
		return 0

def r(i,n):
	if i > n:
		return 0
	if i == 1:
		return 1
	elif i <= n//2:
		return r(i,n//2)
	elif i<= n:
		return r_col(i-n//2,n//2) + r(i-n//2,n//2)

def true_rec(k):
	if power_two_test(k) == True:
		return int(3**math.log2(k))		
	n = 1
	p = 1
	while n <= k:
		n = 2*n	
		p *= 3
	m = p//3
	for i in range(n//2,k):
		m += r(i+1,n)
	return m	


i_values = []
recovery_list = []
for i in range(20):
	i_values.append(i+3)
	recovery_list.append(true_rec(i+3))
print(i_values)
print(recovery_list)
