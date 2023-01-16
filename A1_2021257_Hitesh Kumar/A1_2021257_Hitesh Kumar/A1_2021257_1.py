
print("Choose from following options: ")
print("1.Right-angled triangle")
print("2.Isosceles triangle")
print("3.Kite")
print("4.Half Kite")
print("5.X")




c = int(input("Enter your choice: "))
if (c==1):
    print("Right-angled triangle")   
    n=int(input("please tell me a number:"))
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,'',end="")
        print()

elif(c==4):
    print("Half Kite")
    n=int(input("please tell me a number:"))
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,'',end="")
        for j in range(i,n):
            print('',end="")
        print()

    for i in range(1,n+1):
        for j in range(1,n+1-i):
            print(j,'',end="")
        print()

elif(c==2):
    print("Isosceles triangle")

    n=int(input("please tell the row no.:"))
    if n%2==0:
        for i in range(1,n+1):
            for j in range(i,n):
                print(" ",end='')
            for j in range(1,2*i):
                print(j,end="")
            print("")
    else:
        print("Isosceles triangle is not defined for odd numbers")

elif(c==3):
    print("Kite")

    n=int(input("please tell the  no.:"))
    if n%2==0:
        for i in range(1,n):
            for j in range(i,n):
                print(" ",end='')
            for j in range(1,2*i):
                print(j,end="")
            print()
        for i in range(1,n+1):
            for j in range(1,i):
                print(' ',end="")
            for j in range(1,((2*n)+2)-(2*i)):
                print(j,end="")
            print()
    else:
        print("Kite is not defined for odd numbers")

elif(c==5):
    print("X")
    n=int(input("please tell a number:"))
    if (n%2==0):
        for i in range(1,n):
            for j in range(1,i):
                print(" ",end="")
            for j in range(1,(2*n+2)-2*i):
                print(j,end="")
            print()
        for i in range(1,n+1):
            for j in range(i,n):
                print(" ",end="")
            for j in range(1,2*i):
                print(j,end="")
            print()
    else:
        print("X is not defined with odd numbers")






