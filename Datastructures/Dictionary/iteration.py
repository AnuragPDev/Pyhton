student ={"name":"Peter", "age":20, "marks":23}
# print keys 
for key in student:
    print(key)

# print(values)
for values in student:
    print(student[values] )

#print key values 
for key, value in student.items():
    print(key,value)