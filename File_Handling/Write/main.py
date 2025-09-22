#open file with file object in write mode 

#if the file is not exist
file =open("anurag.txt", 'w') #create file object in wrote mode 
file.write("Hello Anurag")  # write() function is used to wrote in the object
file.close() #close the object

#if the file already exist
file =open("anurag.txt", 'w')   # it will replace the privious text 
result=file.write("Happy navratri")
file.close()


l1=["Anurag\n", "Peter\n", "Thorfinn\n"]
# to write text from list we use writelines
file =open("anurag.txt", 'w')
file.writelines(l1)
file.close()

# append
file=open("anurag.txt",'a')
file.write("This is second line\n")
file.close()



