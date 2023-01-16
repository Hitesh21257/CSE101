with open("AnswerKey.txt","r") as f:
    a=f.read()
    c=list(map(str,a.split()))
    l=c[1::2]

with open("John_1357.txt","r") as f1:
    b=f1.read()
    d=list(map(str,b.split()))
    l1=d[1::2]

with open("Ram_1211.txt","r") as f2:
    m=f2.read()
    n=list(map(str,m.split()))
    l2=n[1::2]
 
with open("Brock_1000.txt","r") as f3:
    m=f3.read()
    n=list(map(str,m.split()))
    l3=n[1::2]
with open("Misty_372.txt","r") as f4:
    m=f4.read()
    n=list(map(str,m.split()))
    l4=n[1::2]

with open("Ash_12.txt","r") as f5:
    m=f5.read()
    n=list(map(str,m.split()))
    l5=n[1::2]


fin=[l1,l2,l3,l4,l5]
ans = []
for i in fin:
    count=0
    for j in range(len(i)):
        if(i[j]==l[j]):
            count=count+4
        elif(i[j]=="-"):
            count=count
        else:
            count=count-1
    ans.append(count)
print(ans)
kl=open("RegisteredStudents.txt","r")
mm=kl.read()
l=mm.split()
abc=l[0::2]
de=l[1::2]
kl.close()
t=open("FinalReport.txt","w")
for i in range(len(fin)):
    t.write(f'{abc[i]}  {de[i]} {ans[i]} \n ')
t.close()


    