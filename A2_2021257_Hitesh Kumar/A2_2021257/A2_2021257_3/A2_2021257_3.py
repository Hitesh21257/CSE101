def dtb(x):
    n=int(x)
    l=[]
    while(n>0):
        a=n%2
        l.append(a)
        n=n//2
    l.reverse()
    s=""
    for i in l:
        s=s+str(i)
    return s

def dto(x):
    n=int(x)
    l=[]
    while(n>0):
        a=n%8
        l.append(a)
        n=n//8
    l.reverse()
    s=""
    for i in l:
        s=s+str(i)
    return s

def dth(x):
    n=int(x)
    l=[]
    d={10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
    while(n>0):
        a=n%16
        l.append(a)
        n=n//16
    l.reverse()
    l2=[]
    for i in l:
        if(i in d):
            l2.append(d[i])
        else:
            l2.append(i)
    s=""
    for i in l2:
        s=s+str(i)
    return s 

def btd(n):
    a=list(map(int,n))
    a.reverse()
    s=0
    j=0
    for i in a:
        s=s+i*(2**j)
        j=j+1
    return s

def htd(n):
    a=list(map(str,n))
    d={"A":10,"B":11,"C":12,"D":13,"E":14,"F":15}
    l3=[]
    for i in a:
        if(i in d):
            l3.append(d[i])
        else:
            l3.append(int(i))
    l3.reverse()
    s=0
    j=0
    for i in l3:
        s=s+i*(16**j)
        j=j+1
    return s

def otd(n):
    a=list(map(int,n))
    a.reverse()
    s=0
    j=0
    for i in a:
        s=s+i*(8**j)
        j=j+1
    return s

def bth(n):
    a=list(map(int,n))
    a.reverse()
    s=0
    j=0
    for i in a:
        s=s+i*(2**j)
        j=j+1
    n=int(s)
    l=[]
    d={10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
    while(n>0):
        a=n%16
        l.append(a)
        n=n//16
    l.reverse()
    l2=[]
    for i in l:
        if(i in d):
            l2.append(d[i])
        else:
            l2.append(i)
    s=""
    for i in l2:
        s=s+str(i)
    return s 

def htb(n):
    a=list(map(str,n))
    d={"A":10,"B":11,"C":12,"D":13,"E":14,"F":15}
    l3=[]
    for i in a:
        if(i in d):
            l3.append(d[i])
        else:
            l3.append(int(i))
    l3.reverse()
    s=0
    j=0
    for i in l3:
        s=s+i*(16**j)
        j=j+1    
    l=[]
    s=int(s)
    while(s>0):
        a=s%2
        l.append(a)
        s=s//2
    l.reverse()
    s=""
    for i in l:
        s=s+str(i)
    return s

def bto(x):
    a=list(map(int,x))
    a.reverse()
    s=0
    j=0
    for i in a:
        s=s+i*(2**j)
        j=j+1
    n=int(s)
    l=[]
    while(n>0):
        b=n%8
        l.append(b)
        n=n//8
    l.reverse()
    m=""
    for i in l:
        m=m+str(i)
    return m

def otb(x):
    a=list(map(int,x))
    a.reverse()
    s=0
    j=0
    for i in a:
        s=s+i*(8**j)
        j=j+1
    n=int(s)
    l=[]
    while(n>0):
        a=n%2
        l.append(a)
        n=n//2
    l.reverse()
    s=""
    for i in l:
        s=s+str(i)
    return s

def hto(x):
    a=list(map(str,x))
    d={"A":10,"B":11,"C":12,"D":13,"E":14,"F":15}
    l3=[]
    for i in a:
        if(i in d):
            l3.append(d[i])
        else:
            l3.append(int(i))
    l3.reverse()
    s=0
    j=0
    for i in l3:
        s=s+i*(16**j)
        j=j+1
    n=int(s)
    l=[]
    while(n>0):
        a=n%8
        l.append(a)
        n=n//8
    l.reverse()
    s=""
    for i in l:
        s=s+str(i)
    return s

def oth(x):
    a=list(map(int,x))
    a.reverse()
    s=0
    j=0
    for i in a:
        s=s+i*(8**j)
        j=j+1
    n=int(s)
    l=[]
    d={10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
    while(n>0):
        a=n%16
        l.append(a)
        n=n//16
    l.reverse()
    l2=[]
    for i in l:
        if(i in d):
            l2.append(d[i])
        else:
            l2.append(i)
    s=""
    for i in l2:
        s=s+str(i)
    return s 

def atb(x):
    a=list(map(str,x))
    d={"A":10,"B":11,"C":12,"D":13,"E":14,"F":15,"G":16,"H":17,"I":18,"J":19,"K":20,"L":21,"M":22,"N":23,"O":24,"P":25,"Q":26,"R":27,"S":28,"T":29,"U":30,"V":31,"W":32,"X":33,"Y":34,"Z":35}
    M=int(input("Enter the radix M:"))
    l5=[]
    for i in a:
        if(i in d):
            l5.append(d[i])
        else:
            l5.append(int(i))
    l5.reverse()
    s=0
    j=0
    for i in l5:
        s=s+i*(M**j)
        j=j+1

    N=int(input("Enter the radix N:"))
    if(N==10):
        print(s)
    else:
        l7=[]
        while(s>0):
            a=s%N
            l7.append(a)
            s=s//N
        l7.reverse()
        l8=[]
        d={10:"A",11:"B",12:"C",13:"D",14:"E",15:"F",16:"G",17:"H",18:"I",19:"J",20:"K",21:"L",22:"M",23:"N",24:"O",25:"P",26:"Q",27:"R",28:"S",29:"T",30:"U",31:"V",32:"W",33:"X",34:"Y",35:"Z"}
        for i in l7:
            if(i in d):
                l8.append(d[i])
            else:
                l8.append(i)
        for i in l8:
            print(i,end='')

print("------------Choose from the below options-------------- ")
print("1)Convert decimal to binary")
print("2)Convert binary to decimal")
print("3)Convert decimal to hexadecimal")
print("4)Convert hexadecimal to decimal")
print("5)Convert decimal to octal")
print("6)Convert octal to decimal")
print("7)Convert binary to hexadecimal")
print("8)Convert hexadecimal to binary")
print("9)Convert binary to octal")
print("10)Convert octal to binary")
print("11)Convert hexadecimal to octal")
print("12)Convert octal to hexadecimal")
print("13)Convert number with radix A to radix B.")
c=int(input("Please select from the above options:"))
if c==1:
    x=input("Enter the input for which you wanted to convert decimal to binary:")
    print(dtb(x))
if c==2:
    x=input("Enter the input for which you wanted to convert binary to decimal:")
    print(btd(x))
if c==3:
    x=input("Enter the input for which you wanted to convert decimal to hexadecimal:")
    print(dth(x))
if c==4:
    x=input("Enter the input for which you wanted to convert hexadecimal to decimal:")
    print(htd(x))
if c==5:
    x=input("Enter the input for which you wanted to convert decimal to octal:")
    print(dto(x))
if c==6:
    x=input("Enter the input for which you wanted to convert octal to decimal:")
    print(otd(x))
if c==7:
    x=input("Enter the input for which you wanted to convert binary to hexadecimal:")
    print(bth(x))
if c==8:
    x=input("Enter the input for which you wanted to convert hexadecimal to binary:")
    print(htb(x))
if c==9:
    x=input("Enter the input for which you wanted to convert binary to octal:")
    print(bto(x))
if c==10:
    x=input("Enter the input for which you wanted to convert  octal to binary:")
    print(otb(x))
if c==11:
    x=input("Enter the input for which you wanted to convert hexadecimal to octal:")
    print(hto(x))
if c==12:
    x=input("Enter the input for which you wanted to convert octal to hexadecimal:")
    print(oth(x))
if c==13:
    x=input("Enter the input for which you wanted to convert number with radix A to radix B:")
    a=atb(x)