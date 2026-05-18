num=int(input("Enter a number:"))
k=num
n=len(str(num))
sum=0
while num>=1:
	x=num%10
	sum=sum+x**n
	num=num//10
if k==sum:
	print(f"{k} is armstrong")
else:
	print(f"{k} is not armstrong")