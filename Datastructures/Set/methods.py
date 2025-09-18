s1={1,3,7,5,"Peter"}
s2={2,4,6 ,8,"Peter"}
# union : combine two sets removing duplicate 
uni=s1.union(s2)
uni1=s1|s2
print(uni)
print(uni1)

# intersection: returns common element
i1=s1.intersection(s2)
print(i1)               #return peter
i2 = s1 & s2
print(i2)

# difference : return the elements present only in first set 
# diff= s1.difference(s2)
diff =s1-s2
print(diff)

#symmentic diffrence return unique element from both the set 
sym_diff= s1.symmetric_difference(s2)
print(sym_diff)



