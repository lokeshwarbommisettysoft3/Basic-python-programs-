num=int(input("Enter a number:"))
a=0
b=1
print("Fibonacci sequence:")
for i in range(num):
	print(a)
	temp=a
	a=b
	b=temp+b