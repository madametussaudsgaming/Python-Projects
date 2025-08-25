#Made with everything I (madametussaudsgaming) have learnt up to Chapter 4, and some things (these square boxes let me do
# multiple assignations in a single line!) i stumbled upon along the way.
import random
import time

fun = random.randint(1, 1000)
key, password, thumbprint, room0, room1, room2, room3, tolerance= [0, 0, 0, 0, 0, 0, 0, 0]
a1, b1, a2, b2, a3, b3, c3 = [0, 0, 0, 0, 0, 0, 0]
points = 1000

print(f"<You are Robot Number {fun}.>")
time.sleep(0.2)
print("<We are testing your reasoning skills and precision.>")
time.sleep(0.2)
print("<Your competency rating will be scored accordingly.>")
time.sleep(0.2)

while ((room1==0 and key==0) or (room2==0 and password==0) or (room3==0 and thumbprint==0)):
	print(" ")
	print("<Which room do you want to enter?>")
	ch1 = int(input("(1, 2, 3): "))
	if ch1 == 1 and room1 != 1:
		print(" ")
		print("Two boxes are presented in front of you.")
		print("The second box is open and visibly contains the key.")
		print(" ")
		print("<There is a key inside one of them.>")
		print("<Which box will you choose?>")
		ch2 = int(input("(1, 2): "))
		if ch2 == 1:
			a1 = 1
			print(" ")
			print("...")
			time.sleep(2)
			print("<This one HAS to be defective.>")
			points = 0
			time.sleep(2)
			print("*exploding sound*")
			break
		elif ch2 == 2:
			b1 = 1
			print(" ")
			print("The key was in the box!")
			key = 1
			room1 = 1
		else:
			print(" ")
			print("<Follow instructions.>")
	elif ch1 == 2 and room2 != 1:
		print(" ")
		print("Two CDs and an old laptop are on a desk.")
		print("The first disc has a smudged label on it.")
		print(" ")
		print("<There is a password inside one of them.>")
		while password == 0 and room2 == 0:
			print("<Which disc will you insert?>")
			ch2 = int(input("(1, 2): "))
			if ch2 == 1:
				a2 = 1
				print(" ")
				print("Looking into the disc, you found the password!")
				password = 1
			elif ch2 == 2:
				print(" ")
				print("There was nothing worthwhile on this disc.")
				print(" ")
				points -= 100
				b2 = 1
			else:
				print(" ")
				print("<Follow instructions.>")
		if password == 1:
			room2 = 1
	elif ch1 == 3 and room3 != 1:
		print(" ")
		print("This is a recreation of a typical living room.")
		print("There is a roll of tape on a table in the middle of the room.")
		print(" ")
		print("<Use the provided tape to collect a thumbprint.>")
		while thumbprint == 0 and room3 == 0:
			print("<Think carefully of where a thumbprint would likely be.>")
			ch2 = int(input("(1 = TV Remote), (2 = Light Switch), (3 = Mini Fridge): "))
			print(" ")
			if ch2 == 1:
				a3 = 1
				print("The buttons' surfaces are too small to have a full thumbprint.")
				print(" ")
				points -= 50
			elif ch2 == 2:
				b3 = 1
				print("You are looking for a THUMBprint; not a FINGERprint.")
				print(" ")
				points -= 50
			elif ch2 == 3:
				c3 = 1
				print("There was a thumbprint on the fridge's handle!")
				print("You take the sample.")
				thumbprint = 1
			else:
				print(" ")
				print("<Follow instructions.>")
		if thumbprint == 1:
			room3 = 1
	elif ch1 == 0 and tolerance == 0:
		print(" ")
		print("<Cute, but you are already in that room.>")
		points += 1
		tolerance = 1
	elif ch1 == 0 and tolerance == 1:
		print(" ")
		print("<It is not as cute the second time.>")
		print("*exploding sound*")
		break
	else:
		print(" ")
		print("There is no point going THAT way.")
if (thumbprint == 0 or password == 0 or key == 0):
	time.sleep(0.1)
	print("<TERMINATED>")
else:
	print(" ")
	print(f"<Points: {points}/1000>")
	if(points >= 850):
		print("<Very Satisfactory.>")
	elif(points >= 500):
		print("<Satisfactory.>")
	elif(points >= 200):
		print("<Disappointing.>")
	elif(points < 200):
		print("<Abysmal Failure.>")
	else:
		print("<UNQUANTIFIABLE.>")