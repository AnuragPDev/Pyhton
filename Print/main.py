# print() function is used to print theb output

print(2+4)

print("Hello")

print("""line 1
      line 2
      line 3
      """)
age =45
name ="Anurag"
#we can also use f string to print alsong with the values in best format
print(f"Hello this is {name} , your age is {age}")


# multiple value in single print using comma 
print(age, name )

# sep sepreater in python 
print("python","is","fun" , sep="-")
print("Python is fun", sep=")") #this will not work it will seprate multiple string

# use end by default python prints in different line 
print("hello" , end=" ")
print("World")

with open("output.txt", "w") as f:
    print("Hello File", file=f)
