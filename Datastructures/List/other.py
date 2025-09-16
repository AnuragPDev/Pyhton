import copy 
num=[2,3,3,3,4,4,4,4,5,6,6,7,8]
# count() is used to count the occurence of same element
print(num.count(4))

#reverse()
num.reverse()
print(num)

# copy the list
num2 = num
print(num2, num)
print(id(num2), id(num2))  # both are same if we cange one element of a list it will change the other list too 

# to solve that we use copy so that we can have same list with different address 
num3 =num.copy()
print(num3, num)
print(id(num3), id(num))

# sort() will sort the lsit
num2.sort()
print(num2)
num4 = copy.deepcopy(num)
print(num4)