a=int(input("Enter 1st Number:"))
b=int(input("Enter 2nd Number:"))
c=int(input("Enter 3rd Number:"))

max=a;

if b>max and c<max:
    max=b;

else:
    max=c;

print(max,"is Max");
