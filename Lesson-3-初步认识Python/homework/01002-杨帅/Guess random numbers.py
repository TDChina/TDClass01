import random

a = random.randint(0,100)

b = int(raw_input("Please enter the number you guessed(0-100):"))

while b != a:
	if b > a:
		print "The ansewer is less than the number you entered"
	else:
		print "The ansewer is greater than the number you entered"
	b = int(raw_input("Please enter the number you guessed(0-100):"))

print "Congratulations!The right ansewer is:%d" % b