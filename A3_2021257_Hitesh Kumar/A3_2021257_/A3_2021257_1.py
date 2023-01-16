import math

def matmul(A,B):
    prod_=[]
    xl=len(A)
    for i in range(xl):
        ll=[]
        for j in range(len(B[0])):
            ll.append(0)
        prod_.append(ll)
    a=len(A)
    b=len(prod_[0])
    c=len(B)
    for ii in range(a):
        for jj in range(b):
            for kk in range(c):
                prod_[ii][jj]=prod_[ii][jj]+((A[ii][kk])*(B[kk][jj]))
    return prod_
# x=list(map(int,input("Enter space separated x cordinate:").split()))
# y=list(map(int,input("Enter space separated y cordinate:").split()))
# z=list(map(int,input("Enter space separated z cordinate:").split()))
    
def scaling(sx,sy,sz,x,y,z,one):
    SS=[[sx,0,0,0],
        [0,sy,0,0],
        [0,0,sz,0],
        [0,0,0,1]]
    T=[ x,
        y,
        z,
        one]
    scal=matmul(SS,T)
    return scal
def translating(tx,ty,tz,x,y,z,one):
    TT=[[1,0,0,tx],
        [0,1,0,ty],
        [0,0,1,tz],
        [0,0,0,1]]

    t=[x,
       y,
       z,
       one]
    trans=matmul(TT,t)
    return trans
def rotation(x,y,z,axis,phi,one):
    l=math.pi
    aaa=(math.cos(phi*(l/180)))
    bbb=(math.sin(phi*(l/180)))  
    if axis=="X":
        TT=[[1,0,0,0],
            [0,aaa,-bbb,0],
            [0,bbb,aaa,0],
            [0,0,0,1]]
        t=[x,
           y,
           z,
           one]
        rota=matmul(TT,t)
    if axis=="Y":
        TT=[[aaa,0,bbb,0],
            [0,1,0,0],
            [-bbb,0,aaa,0],
            [0,0,0,1]] 
        t=[x,
           y,
           z,
           one]
        rota=matmul(TT,t)
    if axis=="Z":
        TT=[[aaa,-bbb,0,0],
            [bbb,aaa,0,0],
            [0,0,1,0],
            [0,0,0,1]]  
        t=[x,
           y,
           z,
           one]
        rota=matmul(TT,t)
    return rota



# for Matrix A:
# A=[]
# B=[]
# for ii in range(m):
#     l=list(map(float,input().split()))
#     A.append(l)
# print("for matrix B")
# for jj in range(n):
#     ll=list(map(float,input().split()))
#     B.append(ll)
# print(A)
# print(B)
# print(matmul(A,B))

