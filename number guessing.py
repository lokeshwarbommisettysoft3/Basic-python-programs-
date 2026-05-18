target=3
while(1):
	guess=int(input("Guess the number:"))
	if guess==target:
		print("Correct.")
		break
	else:
		print("Try again.")