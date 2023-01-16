
n=int(input("Tell  the degree of the polynomial:"))

if(n==0):
    print("It is a constant function")
    k=int(input("Tell the constant term:"))
    u=int(input("Tell  the Lower bound:"))
    l=int(input("Tell  the Upper bound:"))
    d=int(input("Tell the step you vary X:"))
    for i in range(u,l+1,d):
        print("#"*k)
        print()
if(n==1):
    print("It is a linear function")
    a=int(input("Tell  the coefficient of X:"))
    k=int(input("Tell  the constant term:"))
    u=int(input("Tell  the Lower bound:"))
    l=int(input("Tell  the Upper bound:"))
    d=int(input("Tell the step you vary X:"))
    for i in range(u,l+1,d):
        val=round((a*i+k))
        print("#"*val)
        print()
if(n==2):
    print("It is a quadratic function")
    a=int(input("Tell the coefficient of x sq. :"))
    b=int(input("Tell  the coefficient of X:"))
    k=int(input("Tell  the constant term:"))
    u=int(input("Tell  the Lower bound:"))
    l=int(input("Tell  the Upper bound:"))
    d=int(input("Tell the step you vary X:"))
    for i in range(u,l+1,d):
        val=round((a*(i**2))+(b*i)+k)
        print("#"*val)

if(n==3):
    print("It is a cubic function")
    a=int(input("Tell me the coefficient of x cube:"))
    b=int(input("Tell the coefficient of x sq. :"))
    c=int(input("Tell  the coefficient of X:"))
    k=int(input("Tell  the constant term:"))
    u=int(input("Tell  the Lower bound:"))
    l=int(input("Tell  the Upper bound:"))
    d=int(input("Tell the step you vary X:"))
    for i in range(u,l+1,d):
        val=round((a*(i**3)+(b*(i**2))+(c*i)+k))
        print("#"*val)


