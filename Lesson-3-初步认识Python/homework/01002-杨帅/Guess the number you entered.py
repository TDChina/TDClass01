import random

a = int(raw_input("Please enter a number(0-100):"))
b = random.randint(0,100)

while b != a:
	if b > a:
		b -= 1
	else:
		b += 1

print "Thenumber you entered is:%d" % b