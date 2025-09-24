# read(): used to print the output as a single string 
with open("anurag.txt",'r')as f:
    s=f.read() # we can also give the number of chars we want to print
    print(s)


# we can also give the number of chars we want to print
with open("anurag.txt",'r')as f:
    s=f.read(10) 
    print(s)


# readline() used to print line of the file
with open("anurag.txt",'r') as file:
    s1= file.readline().strip()
    s= file.readline().strip()
    print(s,s1)



# if the file is large we dont know how much line we want to print so we use loop till our readline gives ""

with open("anurag.txt", 'r')as file:
    line= file.readline()
    while line!="":
        print(line.strip())
        line =file.readline()


# we can also give number of characters we want

with open("anurag.txt",'r')as file:
    print(file.readline(7).strip())