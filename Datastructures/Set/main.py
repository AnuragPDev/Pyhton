# sets are unordered , unchangeable and unindexed

s ={1,1,2,5,3,7,6}
print(s)

#unchangeable 
# s[2]=23
# print(s) #TypeError: 'set' object does not support item assignment

# cant have duplicate
s1={"Anurag", 2,3,3,0,1, True, False}
print(s1) #{0, 1, 2, 3, 'Anurag'}  in sets the value of true and false is equal to 1 and 0 respectively

#accessing element 
# we cant access the set element like list but we can loop through the sets
for i in s1:
    print(i)