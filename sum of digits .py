def num(n):
	sum=0
	while n>=1:
		digit=n%10
		sum=sum+digit
		n=n//10
	return sum 
print(num(123))