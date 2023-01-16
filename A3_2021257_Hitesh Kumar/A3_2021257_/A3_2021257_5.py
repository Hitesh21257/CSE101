class Student:
    def __init__(self,n,cg,br):
        self.name=n
        self.cgpa=cg
        self.branch=br
        self.isplaced=False
    def isEligible(self,x):
        ss=True
        if self.cgpa<x.req_cgpa:
            ss=False
        elif self.branch not in x.branch_wise:
            ss=False
        elif self.isplaced==True:
            ss=False
        
        if ss==True:
            print(f'Student {self.name} is eligible for the company {x.name_com}')
            self.apply(x)
        else:
            print(f'Student {self.name} is not  eligible for the company {x.name_com}')
    def apply(self,x):
        x.appliedstudent.append(self)

    def getplaced(self):
        self.isplaced=True

class Company:
    def __init__(self,n,rc,branch,po):
        self.name_com=n
        self.req_cgpa=rc
        self.branch_wise=branch
        self.position_open=po
        self.appliedstudent= []
        # self.cgpa=cgpa
        self.appl_open=True
    def hirestudents(self):
        s = []
        for i in self.appliedstudent:
            s.append(i.cgpa)
        p = s.copy()
        p.sort(reverse=True)
        ans = []
        for i in p:
            ans.append(self.appliedstudent[s.index(i)])
        self.appliedstudent=self.appliedstudent[:self.position_open]
        for i in self.appliedstudent:
            i.getplaced()
        self.close_application()
    def close_application(self):
        print(f'The Company {self.name_com} has hired the following Students:')
        for jjj in (self.appliedstudent):
            print(jjj.name)

n=int(input("Enter the no. of students:"))
nos=[]
cgpa=[]
bra=[]
for i in range(1,n+1):
    a=input(f'Enter name of student {i}:')
    nos.append(a)
    try:
        b=float(input(f'Enter cgpa of student {i}:'))
        assert 0<=b<=10   
        cgpa.append(b)
    except:
        print("The cgpa is invalid please provide the correct cgpa")
        b=float(input(f'Enter cgpa of student {i}:'))
        cgpa.append(b)
    c=input(f'Enter branch of student{i}:')
    bra.append(c)
ll = []
for jj in range(n):
    sobj=Student(nos[jj],cgpa[jj],bra[jj])
    ll.append(sobj)
n1=int(input("Enter the no. of company:"))
for i in range(1,n1+1):
    aa=input(f'Enter name of Company {i} :')
    bb=float(input(f'Enter required cgpa for company {i}:'))
    cc=list(map(str,input().split()))
    dd=int(input("Enter no. of positions open for comapany"+str(i)))
    Y=Company(aa,bb,cc,dd)
    for i in ll:
        i.isEligible(Y)
    Y.hirestudents()