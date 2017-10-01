print("1.Addition\n2.Substraction\n3.Multiplication\n4.Division")

c=int(input("Enter Your Choice:"))

if c<1 or c>4:
    print("Wrong Choice")

else:
    a=float(input("Enter 1st Number:"))
    b=float(input("Enter 2nd Number:"))

    if c==1:
        print(a,"+",b,"=",a+b)

    else:
        if c==2:
            print(a,"-",b,"=",a-b)

        else:
            if c==3:
                print(a,"*",b,"=",a*b)

            else:
                if c==4:
                    print(a,"/",b,"=",a/b)

input("Press Enter to Continue...")
