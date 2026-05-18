num=int(input("Enter a number:"))
rev=0
while num>=1:
	x=num%10
	rev=rev*10+x
	num=num//10
print("Reversed number:",rev)