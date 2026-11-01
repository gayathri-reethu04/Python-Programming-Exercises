std={"name":"Reethu",
     "course":"MCA",
     "college":"Aditya University"}
print(std)
std["contact"]=912345678
print("Adding dictionary : ",std)
print("Poping keys : ",std.pop("course"))
print("Accessing all keys : ",std.keys())
print("Accessing all values : ",std.values())
print("Accessing all items : ",std.items())
del std["contact"]
print("Deleting contact ",std)
