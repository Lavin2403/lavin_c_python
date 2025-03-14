a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
if (a>b) and (a>c):
    print("The greatest of 3 numbers is ",a)
elif (b>a) and (b>c):
    print("The greatest of 3 numbers is ",b)
elif (c>a) and (c>b):
    print("The greatest of 3 numbers is ",c)
else:
    print("All 3 numbers are equal: ",a,b,c)