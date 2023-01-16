for i in range(100):
    print("1)Finding the reverse of a number")
    print("2)Cheking  the number to be palindrome or not")
    print("3)Checking the number to be Narcissitic or not")
    print("4)Finding the sum of digits of that number")
    print("5)Finding the sum of squares of digit of a number")
    print("6)Exit the application")



    a=int(input("Choose any one from the above choices:"))

    #defining a function for getting reverse of that number
    def reverse(x):
        n1=str(x)
        n2=n1[::-1]
        return n2

    #defining a function for checking the number to be palindrome or not
    def palin(x):
        n1=str(x)
        n2=n1[::-1]
        if(n1==n2):
            return True
        else:
            return False

    #defining a function for checking the number to be Narcissitic or not
    def nar(x):
        sum=0
        n1=x
        for i in range(122):  
            sum=sum+((x%10)**3)
            x=x//10
        if(n1==sum):
            return True
        else:
            return False

    #defining a function for calculating the sum of digits
    def sumdig(x):
        s1=0 
        for i in range(1000):
            s1=s1+x%10
            x=x//10
        return s1

    #defining a function for calculating the sum of squares of digit of a number

    def sumsq(x):
        sum=0
        for i in range(1000):
            sum=sum+(x%10)**2
            x=x//10
        return sum
        


    if(a==1):
        print("You want to reverse the number")
        n=int(input("Tell me a number:"))
        ans=reverse(n)
        print(ans)

    if(a==2):
        print("You wanted to check the number to be palindrome or not")
        n=int(input("Tell me a number:"))
        ans=palin(n)
        print(ans)

    if(a==3):
        print("You wanted to check the number to be Narcissitic or not")
        n=int(input("Tell me a number:"))
        ans=nar(n)
        print(ans)

    if(a==4):
        print("You wanted to check the sum of digits")
        n=int(input("Tell me a number:"))
        ans=sumdig(n)
        if(ans<=9):
            print(ans)
        elif(ans>9):
            z1=ans
            y1=sumdig(ans)
            if(y1<=9):
                print(y1+z1)
            else:
                a1=ans
                a2=y1
                a3=sumdig(y1)
                print(a1+a2+a3)
    
            
    if(a==5):
        print("You wanted to calculate the sum of squares of digits")
        n=int(input("Tell me a number:"))
        ans=sumsq(n)
        l1=[]
        l1.append(ans)
        y1=ans
        while(y1>9):
            y2=sumsq(y1)
            l1.append(y2)
            y1=y2

    finalsum=0
    for i in l1:
        finalsum=finalsum+i
    print(finalsum)

    if(a==6):
        print("Exit the application")
        break









        






