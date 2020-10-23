number = 17
prime = True

for i in range(2, number):
	if(number % i == 0):
		prime = False

if(prime == True):
	print("Prime")
else:
	print("Not Prime")