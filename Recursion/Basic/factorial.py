def factorial(n):
    #base case 
    if n==0 or n==1:
        return 1
    
    return n * factorial(n-1)





def main():
    num=5
    result =factorial(num)
    print(f"Factorial of {num} is {result}")




if __name__=="__main__":
    main()
