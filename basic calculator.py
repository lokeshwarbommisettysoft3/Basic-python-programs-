x=float(input("Enter a value:"))
y=float(input("Enter a value:"))
print("Choose operation:")
print("1.Addition")
print("2.Subtract")
print("3.Multiplication")
print("4.Division")
choice=int(input("Enter your choice:"))
if choice==1:
	print("x+y=",x+y)
elif choice==2:
	print("x-y=",x-y)
elif choice==3:
	print("x*y=",x*y)
elif choice==4:
	if y!=0:
		print("x/y=",x/y)
	else:
		print("Division is not possible")
else:
	print("Invalid choice")	