n=float(input("Enter marks : "))
if(n>=90):
    grade='O'
elif(n>=80):
    grade='A'
elif(n>=70):
    grade='B'
elif(n>=60):
    grade='C'
elif(n>=50):
    grade='D'
else:
    grade='F'
print("Grade : ",grade)
