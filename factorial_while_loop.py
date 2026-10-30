x=int(input("Enter number "))
if(x==0 or x<0):
    print("Factorial is impossible ")
else:
    i=1
    fact=1
    while(i<=x):
        if(i==0):
            pass
        elif(i>x):
            break
        fact*=i
        i+=1
    else:
        print("Factorial of ",x,"is",fact)
