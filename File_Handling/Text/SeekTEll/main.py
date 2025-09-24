# create the file object in read mode
with open("anurag.txt",'r') as file:

    print(file.tell()) # print the current line index at A
    print(file.readline()) #print "anurag\n" 7  bytes
    print(file.tell()) # pritn 7
    print(file.readline()) # print new line

    print(file.tell()) # print 13

    # if we want to print again same first line we can shift pointer with seek()
    file.seek(0) # move pionter to  start
    print(file.readline())


# with write mode
with open("anurag.txt",'w')as file :
    print(file.tell())
    file.write('anu') # this will replace all the content
    #change the pointer position 
    file.seek(0)
    file.write('m')  # this will replace only the character which is in first position o/p mnu
    
    