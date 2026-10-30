print("1.Addition\n2.Substraction\n3.Multiplication\n4.Division")
choice=int(input("Enter choice  :  "))
a=int(input("Enter 1st number  :  "))
b=int(input("Enter 2nd number  :  "))
if(choice==1):
    print("Addition  :   ",a+b)
elif(choice==2):
    print("Substraction  :   ",a-b)
elif(choice==3):
    print("Multiplication  :  ",a*b)
elif(choice==4):
    if(b==0):
        print("Undefine")
    else:
        print("Division  :  ",a/b)
else:
    print("Invalid choice")
