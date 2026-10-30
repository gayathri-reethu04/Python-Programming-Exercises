x=["apple","banana","kiwi"]     #List of strings
print("Original list  :  ",x)
x.append("orange")
print("Appended list  :  ",x)
x.insert(2,"jackfruit")
print("Inserted list  : ",x)
a=x[0:3:]
print("Slicing : ",a)
b=x[3:5:]
print("\t",b)
c=x[::-1]
print("Reverse slicing : ",c)
d=x[::2]
print("Slicing with step  :  ",d)
e=x[::-3]
print("Slicing with step reverse : ",e)
x.reverse()
print("Reverse list  :  ",x)
print("Length of 1st list : ",len(x))
print()



y=[10,20,30,40,50,60,70,80]     #List of integers
print("Original list",y)
print("Poping element  :  ",y.pop())
print("Poping 3rd element  : ",y.pop(2))
print("Remove element  : ",y.remove(10))
y.append(20)
print("Append element  : ",y)
y.extend([40,60,40,20])
print("Extended list  : ",y)
print("Count  :  ",y.count(20))
y.sort()
print("Sorting element  : ",y)
y.sort(reverse=True)
print("Reverse sorting  : ",y)
z=y.copy()
print("Copy list  :  ",z)
print("Lenght of 2nd list : ",len(y))
print()
s=x+y
print("Combining two list  : ",s)
print("Lenght of combined list : ",len(s))












