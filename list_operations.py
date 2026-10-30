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













