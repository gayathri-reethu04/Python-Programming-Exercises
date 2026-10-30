x=(10,20,30,40,50)
print("Original tuple  : ",x)
print("Accessing element  : ",x[2])
print("Lenght of tuple : ",len(x))
print("Count : ",x.count(20))
print("Multiple elements : ",x*2)
print("Maximum and Minimum element of tuple : ",max(x),min(x))
print("Sum of tuple : ",sum(x))
y=(60,70,80,90)
z=x+y
print("Adding two tuples : ",z)
a,b,c,d=y
print("Unpacking tuple elements : ",a,b,c,d)
print("Converting tuple to list : ",list(z))
