from A3_2021257_1 import *

def test_matmul(A,B,true_C):
    ans=matmul(A,B)
    if ans==true_C:
        return True
    else:
        return False
def test_scale(x,y,z,sx,sy,sz,true_x,true_y,true_z,one):
    ans=scaling(sx,sy,sz,x,y,z,one)
    if ans[0]==true_x and ans[1]==true_y and ans[2]==true_z:
        return True
    else:
        return False
def test_translate(x,y,z,tx,ty,tz,true_xt,true_yt,true_zt,one):
    ans=translating(tx,ty,tz,x,y,z,one)
    if ans[0]==true_xt and ans[1]==true_yt and ans[2]==true_zt:
        return True
    else:
        return False

def test_rotating(x,y,z,axis,phi,true_xr,true_yr,true_zr,one):
    ans=rotation(x,y,z,axis,phi,one)
    if ans[0]==true_xr and ans[1]==true_yr and ans[2]==true_zr:
        return True
    else:
        return False
print("1)For testing of matmul function")
print("2)For testing of scaling")
print("3)For testing of translating")
print("4)For testing of rotation")

e=int(input("Choose from the above option:"))
if e==1:
    print("You wanted to test the matmul function")
    n=int(input("Enter the no. of rows in matrix A:"))
    A=[]
    for i in range(n):
        aa=list(map(float,input("Enter the rows of Matrix A with space separated:").split()))
        A.append(aa)
    B=[]
    nn=int(input("Enter the no. of rows of matrix B:"))
    for ii in range(nn):
        aaa=list(map(float,input("Enter the rows of Matrix B with space separated:").split()))
        B.append(aaa)
    true_c=[]
    for i in range(n):
        a=list(map(float,input("Enter the rows of Final matrix with space separated:").split()))
        true_c.append(a)
    print(test_matmul(A,B,true_c))
    # print(matmul(A,B))
    # print(true_c)
if e==2:
    print("You wanted to test the Scaling")
    nnn=int(input("Enter the no. of vertices:"))
    x=list(map(float,input("Enter space separated x cordinate:").split()))
    y=list(map(float,input("Enter space separated y cordinate:").split()))
    z=list(map(float,input("Enter space separated z cordinate:").split()))
    one=[]
    for j in range(nnn):
        one.append(1)
    sx=float(input("Enter the value of sx:"))
    sy=float(input("Enter the value of sy:"))
    sz=float(input("Enter the value of sz:"))
    true_x=list(map(float,input("Enter the final x axis of scaling:").split()))
    true_y=list(map(float,input("Enter the final y axis of scaling:").split()))
    true_z=list(map(float,input("Enter the final z axis of scaling:").split()))
    print(test_scale(x,y,z,sx,sy,sz,true_x,true_y,true_z,one))
if e==3:
    print("You wanted to test the translating")
    nnn=int(input("Enter the no. of vertices:"))
    x=list(map(float,input("Enter space separated x cordinate:").split()))
    y=list(map(float,input("Enter space separated y cordinate:").split()))
    z=list(map(float,input("Enter space separated z cordinate:").split()))
    one=[]
    for j in range(nnn):
        one.append(1)
    tx=float(input("Enter the value of tx:"))
    ty=float(input("Enter the value of ty:"))
    tz=float(input("Enter the value of tz:"))
    true_xt=list(map(float,input("Enter the final x axis of translating:").split()))
    true_yt=list(map(float,input("Enter the final y axis of translating:").split()))
    true_zt=list(map(float,input("Enter the final z axis of translating:").split()))
    print(test_translate(x,y,z,tx,ty,tz,true_xt,true_yt,true_zt,one))

if e==4:
    print("You wanted to test the rotation")
    nnn=int(input("Enter the no. of vertices:"))
    x=list(map(float,input("Enter space separated x cordinate:").split()))
    y=list(map(float,input("Enter space separated y cordinate:").split()))
    z=list(map(float,input("Enter space separated z cordinate:").split()))
    one=[]
    for j in range(nnn):
        one.append(1)
    axis=input("Enter the axis from  (X/Y/Z) :")
    phi=float(input("Enter the angle in degree:"))
    true_xr=list(map(float,input("Enter the final x axis of the chossing axis:").split()))
    true_yr=list(map(float,input("Enter the final y axis of of the chossing axis:").split()))
    true_zr=list(map(float,input("Enter the final z axis of of the chossing axis:").split()))
    print(test_rotating(x,y,z,axis,phi,true_xr,true_yr,true_zr,one))