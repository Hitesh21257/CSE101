class Person():
    def __init__(self,f,l,age):
        self.firstname=f
        self.lastname=l 
        self.age=age
    def object_info(self):
        ss=[self.firstname,self.lastname ,self.age]
        return ss

n=int(input("Enter the no. of persons:"))
lfinal=[]
for i in range(n):
    x=list(map(str,input("Enter the details of a person with space separated:").split()))
    lfinal.append(x)

def sort_attribute(x):
    x.sort()
    return x
q=int(input("Specify No. of query:"))
llll=[]
for j in range(q):
    l=[]
    kk=input(f"Query{j+1}:")
    if kk=="firstname":
        for k in range((n)):
            l.append(lfinal[k][0])
    if kk=="lastname":
        for k in range((n)):
            l.append(lfinal[k][1])
    if kk=="age":
        for k in range((n)):
            l.append((lfinal[k][2]))
    a=sort_attribute(l)
    lf=[]
    for i in a:
        for k in range(n):
            for mm in range(3):
                if i in (lfinal[k][mm]):
                    lf.append(lfinal[k])
    
    for nn in range(n):
        ll=[]
        for m in range(3):
            ll.append(lf[nn][m])
        u=ll[0]
        v=ll[1]
        w=ll[2]
        asdf=Person(u,v,w)
        llll.append(asdf.object_info())

print('-------------------------------------------------------------')
print("Welcome to the application ")

for mmm in range(1,n+1):
    print(f"Firstname for person {mmm}  : {lfinal[mmm-1][0]}")
    print(f"Lastname  for Person {mmm}  :{lfinal[mmm-1][1]}")
    print(f"Enter age for Person  {mmm} :{lfinal[mmm-1][2]}")
    print()

for i in llll:
    print(*i)
print()
print("--Thanks for using the Application------")
        