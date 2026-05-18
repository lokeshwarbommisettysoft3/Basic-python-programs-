m1=float(input("Physics marks:"))
m2=float(input("English marks:"))
m3=float(input("Maths marks:"))
m4=float(input("C language marks:"))
total=m1+m2+m3+m4
average=total/4
print("Total marks:",total)
print("Average:",average)
if average>=90:
	print("S Grade")
elif average>=80:
	print("A Grade")
elif average>=70:
	print("B Grade")
elif average>=60:
	print("C Grade")
elif average>=50:
	print("D Grade")
elif average>=40:
	print("E Grade")
else:
	print("Fail")