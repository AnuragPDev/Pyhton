# once we create a set we cant change it , but we can add the items 
# add()

s1={"Anurag", 2,3,3,0,1, True, False}
s1.add("Cheeku")
print(s1)

s2={4,5,6}
s1.update(s2)
print(s1)

# adding string
s1.update("Anurag")
print(s1)

# adding dictionary
s1.update({"name":"anurag", "age":27})
print(s1)