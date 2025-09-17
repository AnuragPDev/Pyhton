# tuple is linear data structure used to store value of same or different data types 
# we create tupe with round bracket
# it is ordered immutable 
t1 = (1,2,4,3,5)
print(t1, type(t1))

# t1[4]=6 #error type error
print(t1)

# accessing the element 
print(t1[0])
print(t1[1])
print(t1[2])
print(t1[3])
print(t1[4])

#slicing
print(t1[1:3])

#allow duplicates 
t2=("CHit","Anurag", "Peter", "Anurag", "Sachin")
print(t1)

# concatenation
print(t1+t2)

# repeatation
print(2*t1*3)


# since its immuatble there is only few methods 
# count(): the number of occurence

print(t2.count("Anurag"))
#index() : return the index of the first occurence

print(t2.index("Anurag"))