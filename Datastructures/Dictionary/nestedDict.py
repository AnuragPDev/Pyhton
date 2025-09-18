students={

    "student1": {
        "name":"peter",
        "age":23,
        "mob":924842
    },

    "student2":{
        "name":"meg",
        "age":23,
        "mob":924842
    },

    "student3":{
        "name":"thorfinn",
        "age":23,
        "mob":924842}
}

#accessing

# print(students["student1"])

# #get()
# print(students.get("student2","not found").get("name"))

# s="a"
# s1="a"

# print(s*2==s1+s1)

# iterating a nested dictionary

for i , obj in students.items():
    print(i)
    for j  in obj:
        print(j+ ":" , obj[j])