import cases
def function2(n):
    m=1
    for i in range(1,n+1):
        m=m*(i)
    return m 
def testing(n):
    lin=[]
    lou=[]
    lfo=[]
    for i in range(1,n+1):
        y=open(r"C:\Users\HITESH KUMAR\OneDrive\Desktop\python\input_"+ str(i) +".txt","r")
        z=y.read()
        z2=function2(int(z))
        lfo.append(z2)
        lin.append(int(z))
        y1=open(r"C:\Users\HITESH KUMAR\OneDrive\Desktop\python\output_"+ str(i) +".txt","r")
        z1=y1.read()
        lou.append(int(z1))
    for i in range(len(lou)):
        if(lou[i]==lfo[i]):
            return "SUCCESS"
        else:
            return "FAILED"
N=int(input("Tell the no. of inputs you wanted to tested:"))
print(testing(N))

