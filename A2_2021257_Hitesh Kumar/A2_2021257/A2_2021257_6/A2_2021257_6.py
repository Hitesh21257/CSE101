def normaltransverse(n):
    return n

def altertrans(n):
    l=n[0::2]
    l1=n[1::2]
    l=[]
    for i in range(len(n)):
        if(i%2==0):
            l.append(n[i])
        else:
           l.append(n[i][::-1])
    return l
def spiraltrans(n):
    l=[] 
    k=0
    nj = len(n)
    while nj!=0:
        if k%4==0:
            l.append((n.pop(0)))
        if k%4==1:
            l3=[]
            for i in range(len(n)):
                l3.append(n[i].pop(-1))
            l.append(l3)
        if k%4==2:
            m=n.pop(-1)
            m.reverse()
            l.append(m)
        if k%4==3:
            l2=[]
            for i in range(len(n)):
                a=n[i][0]
                b=n[i].index(a)
                l2.append(n[i].pop(b))
            l.append(l2[::-1])
        k=k+1
        nj = len(n)
    return l

def boundarytrans(n):
    l=[]
    l.append(n.pop(0))
    l2=[]
    for i in range(len(n)):
        l2.append(n[i].pop(-1))
    l.append(l2)
    m=n.pop(-1)
    m.reverse()
    l.append(m)
    l4=[]
    for i in range(len(n)):
        a=n[i][0]
        b=n[i].index(a)
        l4.append(n[i].pop(b))
    l.append(l4[::-1])
    return l

def transr(z):
    final=[]
    for l in range((2*len(z))-1):
            am=[]
            for m in range(len(z)):
                for n in range((len(z[0]))):
                    if(l==m+n):
                        a=z[m][n]
                        am.append(a)
            final.append(am)
    return final

def transl(z):
    l6=[]
    for i in z:
        l6.append(i[::-1])
    ans=[]
    for l in range(2*len(l6)-1):
        rows=[]
        for m in range(len(l6)):
            for n in range(len(l6[0])):
                if(l==m+n):
                    a=l6[m][n]
                    rows.append(a)
        ans.append(rows)
    return ans

N=int(input("Enter the rank of matrix:"))
A=[]
for i in range(N):
    rows=list(map(int,input("Enter the rows of the matrix:").split()))
    A.append(rows)

print("Choose any from the below options")
print("1)Normal traversal( from left to right for each row)")
print("2)Alternating traversal")
print("3) Spiral traversal from outer to inwards")
print("4)Boundary traversal")
print("5)Diagonal traversal from right to left")
print("6)Diagonal traversal from left to right.")
c=int(input("Choose any one from the above options:"))
if c==1:
    print("You wanted to use Normal traversal")
    Y=normaltransverse(A)
    for i in Y:
        for j in i:
            print(j,end=" ")
if c==2:
    print("You wanted to use Alternating traversal")
    Y=altertrans(A)
    for i in Y:
        for j in i:
            print(j,end=" ")
if c==3:
    print("You wanted to use Spiral traversal")
    Y=spiraltrans(A)
    for i in Y:
        for j in i:
            print(j,end=" ")
if c==4:
    print("You wanted to use Boundary traversal")
    Y=boundarytrans(A)
    for i in Y:
        for j in i:
            print(j,end=" ")
if c==5:
    print("You wanted to use Diagonal traversal from right to left")
    Y=transr(A)
    for i in Y:
        for j in i:
            print(j,end=" ")
if c==6:
    print("You wanted to use Diagonal traversal from left to right")
    Y=transl(A)
    for i in Y:
        for j in i:
            print(j,end=" ")

