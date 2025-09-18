student ={"name":"Peter", "age":20, "marks":23}

# del delete dictionary completely
# del student
# print(student)

# pop will remove the items inside the dict which pass as a input 
popValue=student.pop("nam","not found")
print(student)
print(popValue)

# popitem removes the last inserted key value pair 
deletedItem= student.popitem()
print(deletedItem)
student.clear()
print(student)