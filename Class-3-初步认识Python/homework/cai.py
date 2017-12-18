import random
n = int(random.uniform(1,100))
while True:
	i = int(raw_input('the number is'))
	if i > n:
		print ('bigger')
	if i < n:
		print ('smaller')
	if i == n:
		print ('win')
		break