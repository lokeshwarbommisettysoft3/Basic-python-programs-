num=int(input("Enter a number:"))
sum=0
while num>=1:
	x=num%10
	sum=sum+x
	num=num//10
print("Sum of digits:",sum)
	