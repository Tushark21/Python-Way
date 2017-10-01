a1=0
a2=1
n=int(input("Enter Number of Terms you want to Display (>2):"))

i=0;
print(a1)                               #Printing 1st Element
print(a2)				#Printing 2nd Element
	
while i<n-2:
    an=a1+a2
    a1=a2
    a2=an
    print(an)
    i+=1
