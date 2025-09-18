# dictionary is used to store the data in the key value pair 
student1={"name":"Anurag",
          "age":34,
          "bank_balance":8000000}

student2={"name":"Peter",
          "age":32,
          "bank_balance":80000}

student3={"name":"Meg",
          "age":30,
          "bank_balance":80000}

# accesseing items 
x,y,z= student1["name"], student2["name"],student3["name"]
print(x,y,z)

# using get() method 
print(student1.get("nam","Not found")) # it will return non if keys is not there else it will print default value whcih is not found in our case

# accessing keys 
print(student1.keys())
 #accessing values

print(student1.values())

# items() is used to return all the key vaule pair as tuple in list
x= student1.items()
print(x)