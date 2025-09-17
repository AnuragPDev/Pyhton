# we can also remove the element using inbuilt methods 

num=[1,2,4,5,6,"Peter"]

print(num)
# remove method is used to remove the first occurence of given element
num.remove(2)
print(num)


#pop mthod is used to remove the element from given index and return the poped element


poppedelement=num.pop(4)
print(poppedelement)
print(num)

#clear the list
num.clear()
print(num)

