x=int(input("Enter number :  "))
fact=1
if(x==0):
    print("Factorial is not possible")
else:
    for i in range(1,x+1):
        if(i==0):
            pass
        elif(i<1):
            continue
        elif(i>x):
            break
        fact*=i
    else:
            print("Factorial of ",x,"is ",fact)
