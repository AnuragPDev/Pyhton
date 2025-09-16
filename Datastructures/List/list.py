# list define = list is a lianer data strcuture in python which is  mutable in nature is used to store the data of same or different data types

name = ['a','b','c']

# accessing list
# with index 

print(name[0] ,end ="")
print(name[1],end ="")
print(name[2],end ="")
print(name[-1],end ="")
print(name[-2],end ="")
print(name[-3],end ="")
# with for loop 

for i in name:
    print(i)

# change element
name[0]="A"


print(name, type(name))

# slicing

num=[1,2,3,4,5,6,7,8,9,10]

print(num[0:3])
print(num[4:]) # print all element from index 4 to last

print(num[-1:-3]) # print empty list because slicing moves in forward +1 step 
print(num[-1:-3:-1]) # print empty list because slicing moves in forward +1 step 
print(num[::-1])  # reverse the list
print(num[-3:-1])

