import random
print("Gacha simulator\nFor every 80 draw, win a guaranted 5 star")
a = 0
counter = 0
while a != 1:
	user = input("Enter a number:")
	try:
		user = int(user)
	except:
		print("You must enter a number")
		continue
	b = 0
	while user > 0:
		if counter == 79:
			print("You win a 5 star as bonus!")
			counter = 0
			user -= 1
			continue
		luck = random.randint(1,100)
		if luck == 1:
			print("You win a 5 star! Yeah!")
			counter += 1
		if 2 <= luck <= 12:
			print("You win a 4 star!")
			counter += 1
		if 13 <= luck <= 24:
			print("You win a 3 star!")
			counter += 1
		if 25 <= luck <= 50:
			print("You win a 2 star!")
			counter += 1
		if 51 <= luck <= 100:
			print("You win a 1 star!")
			counter += 1
		user -= 1