def function1(n):
    if(n==0):
        return 1
    else:
        return n*function1(n-1)
def generateData(n):
    for i in range(n):
        a=open(r"C:\Users\HITESH KUMAR\OneDrive\Desktop\python\input_" + str(i+1) + ".txt","w")
        w=input("Enter the numbers:")
        a.write(w)
        a.close()
        b=open(r"C:\Users\HITESH KUMAR\OneDrive\Desktop\python\output_" + str(i+1) +".txt","w")
        m=function1(int(w))
        b.write(str(m))
    b.close()
N=int(input("Enter the no. of inputs you give:"))
generateData(N)

