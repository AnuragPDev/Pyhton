# a compact way to create a list
#normal way
nums=[]
for i in range(5):
    nums.append(i*i)
print(nums)

#list comprehension
nums1=[i*i for i in range(5) ]
print(nums1)
