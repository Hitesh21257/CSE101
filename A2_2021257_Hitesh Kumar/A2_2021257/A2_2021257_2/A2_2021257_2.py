n=float(input("Enter the no. of vertices in the 3d shape:"))
x=list(map(float,input().split()))
xxx=x.copy()
y=list(map(float,input().split()))
yyy=y.copy()
z=list(map(float,input().split()))
zzz=z.copy()
q=int(input("Find the total no. of query:"))
for i in range(q):
   print("1 for Scaling")
   print("2 for translating")
   print("3 for rotating")
   c=int(input("Please  select from the above options"))
   if(c==1):
      print("You wanted to use Scaling ")
      sx=float(input("Amount of scale in x-axis:"))
      sy=float(input("Amount of scale in y-axis:"))
      sz=float(input("Amount of scale in z-axis:"))
      T=[[sx,0,0,0],
         [0,sy,0,0],
         [0,0,sz,0],
         [0,0,0,1]]

      A=[x,
         y,
         z]
      xnew=[(sx)*i for i in x]
      ynew=[(sy)*i for i in y]
      znew=[(sz)*i for i in z]
      x=xnew
      y=ynew
      z=znew
   if(c==2):
      print("You wanted to use Translating ")
      tx=float(input("Amount of translation in x-axis:"))
      ty=float(input("Amount of translation in y-axis:"))
      tz=float(input("Amount of translation in z-axis:"))
      T=[[1,0,0,tx],
         [0,1,0,ty],
         [0,0,1,tz],
         [0,0,0,1]]
      A=[x,
         y,
         z,
         1]
      xnew=[(((1)*i)+tx) for i in x]
      ynew=[(((1)*i)+ty) for i in y]
      znew=[(((1)*i)+tz) for i in z]
      x=xnew
      y=ynew
      z=znew
   if(c==3):
      print("You wanted to use Rotation")
      print("1)If You wanted to rotate with x-axis")
      print("2)If you wanted to rotate with y-axis")
      print("3)If you wanted to rotate wpth z-axis")
      d=float(input("Choose any one from the above problem:"))
      if d==1:
         angle=float(input("Enter the angle in degrees:"))
         import math 
         l=math.pi
         a=(math.cos(angle*(l/180)))
         b=(math.sin(angle*(l/180)))
         T=[[1,0,0,0],[0,a,-b,0],[0,b,a,0],[0,0,0,1]]
         A=[x,y,z,1]
         xnew=[]
         for i in x:
            s=1*i
            xnew.append(s)
         ynew=[]
         for i in range(len(y)):
            s=(a*y[i]) - (b*z[i])
            ynew.append(s)
         znew=[]
         for i in range(len(z)):
            s=(b*y[i]) + (a*z[i])
            znew.append(s)
         x=xnew.copy()
         y=ynew.copy()
         z=znew.copy()
      if d==2:

         angle=float(input("Enter the angle in degrees:"))
         import math 
         l=math.pi
         a=(math.cos(angle*(l/180)))
         b=(math.sin(angle*(l/180)))
         T=[[a,0,b,0],[0,1,0,0],[-b,0,a,0],[0,0,0,1]]
         A=[x,y,z,1]
         xnew=[]
         for i in range(len(x)):
            s=(a*x[i])+(b*z[i])
            xnew.append(s)
         ynew=[]
         for i in y:
            s=1*i
            ynew.append(s)
         znew=[]
         for i in range(len(x)):
            s=(-b*x[i])+(a*z[i])
            znew.append(s)
         x=xnew.copy()
         y=ynew.copy()
         z=znew.copy()
      if d==3:
         angle=float(input("Enter the angle in degrees:"))
         import math 
         l=math.pi
         a=(math.cos(angle*(l/180)))
         b=(math.sin(angle*(l/180)))
         T=[[a,-b,0,0],[b,a,0,0],[0,0,1,0],[0,0,0,1]]
         A=[x,y,z,1]
         xnew=[]
         for i in range(len(x)):
            s=(a*x[i])-(b*y[i])
            xnew.append(s)
         ynew=[]
         for i in range(len(x)):
            s=(b*x[i])+(a*y[i])
            ynew.append(s)
         znew=[]
         for i in z:
            s=1*i
            znew.append(s)
         x=xnew.copy()
         y=ynew.copy()
         z=znew.copy()

print(xnew)
print(ynew)
print(znew)

q=open("Text file for question 2.txt","w")
q.write(f'{xxx}  {yyy}  {zzz} \n {xnew} {ynew} {znew} ')





         

      





