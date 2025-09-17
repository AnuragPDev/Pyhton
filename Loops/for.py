# loops are used to repeat a block of code multile times 
# for loop 
# when we know the number of times we want to repeat something 

name ="Anurag is a millioanire"
for char in name:
    print(char,end="")


l1=[1,2,3,4,5]
for num in l1:
    print(num,end="")

# we can use range function when we wnat to run the code a specified number of times
for x in range(5):
    print(x)

# break : is used to stop the iteration before it has looped through all the times
for num in l1:
    if num==3:
        break
    print(num)

# continue is used to skip the current iteration of the loop 
for num in l1:
    if num==3:
        continue
    print(num)