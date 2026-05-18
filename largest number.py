def check(x,y,z):
	if(x>y and x>z):
		print(f"{x} is largest")
	elif(y>x and y>z):
		print(f"{y} is largest")
	else:
		print(f"{z} is largest")
check(55,9,31)