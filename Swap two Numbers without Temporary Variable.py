x=int(input("Enter 1st Number:"))
y=int(input("Enter 2nd Number:"))

print("Numbers Before Swapping:")
print(x,",",y)

x=x+y
y=x-y
x=x-y
print("Numbers After Swapping:")
print(x,",",y)
