student ={"name":"Peter", "age":20, "marks":23}

print(student)
# direct assign
student["school"]="KKSN"
print(student)

#update will update the dict with the items from the given argument

student.update({"dob": 2002})
print(student)

print(student["age"])
