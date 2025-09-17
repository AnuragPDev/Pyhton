s1={"Anurag", 2,3,3,0,1, True}
# remove() is used to remove the element from  set but is shows error if item is not exist
print(s1)
s1.remove(0)
print(s1)
# s1.remove(0)
# print(s1) #error 

#discard() is used to delete item without throwing an error

s1.discard(0)
print(s1)

#pop()
print(s1.pop())
