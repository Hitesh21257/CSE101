
n=int(input("Please tell me the no. of terms you want to put in the polynomial:"))
l1=[]
for i in range(1,n+1):
    n=float(input("please tell me the exponents:"))
    l1.append(n)
print("List of exponents was:",l1)

#Define the function for  calculating the value of f(x)

def fun(x):
    sum=0
    for i in l1:
        sum=sum+(x)**i
    return sum
#Define the function for calculating the derivative of f(x)

def der(x):
    sum=0
    for i in l1:
        sum=sum+(i*(x)**(i-1))
    return sum

#find out root of the polynomail
x1=1
for i in range(1000):
    x2=(x1)-(fun(x1)/der(x1))
    if(abs(x1-x2))<0.001:
        break
    x1=x2
if(type(x2)==complex):
    print("The root of the eqaution:",0)
else:
    print("The root of the equation is :",round(x2,2))
