with open("practice.txt",'w') as file:
    file.write("Python\n")
    file.write("Java\n")
    file.write("C++\n")
    file.write("JavaScript\n")

with open('practice.txt','a') as file:
    file.write('Go\n')
    file.write('Rust\n')

# read all the lines into a list and print it 
with open('practice.txt', 'r') as file:
    res=[line.strip() for line in file.readlines()]
    print(res)

# print only third line 
with open('practice.txt', 'r') as file:
    lines=file.readlines()
    print(lines[2].strip())

# read first three line without loading entire file 
with open('practice.txt', 'r') as file:
    print(file.readline().strip())
    print(file.readline().strip())
    print(file.readline().strip())