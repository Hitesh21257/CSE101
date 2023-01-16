def majorNotes(a):
    l1=[]
    a1=a[0]
    l1.append(a1)
    a2=a[2]
    l1.append(a2)
    a3=a[4]
    l1.append(a3)
    a4=a[5]
    l1.append(a4)
    a5=a[7]
    l1.append(a5)
    a6=a[9]
    l1.append(a6)
    a7=a[11]
    l1.append(a7)
    a8=a[12]
    l1.append(a8)
    return " ".join(l1)
def minorNotes(b):
    l2=[]
    b1=b[0]
    l2.append(b1)
    b2=b[2]
    l2.append(b2)
    b3=b[3]
    l2.append(b3)
    b4=b[5]
    l2.append(b4)
    b5=b[7]
    l2.append(b5)
    b6=b[8]
    l2.append(b6)
    b7=b[10]
    l2.append(b7)
    b8=b[12]
    l2.append(b8)
    return " ".join(l2)


l=[['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', "C'"],
['C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', "C'", "C#'"],
['D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', "C'", "C#'", "D'"],
['D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', "C'", "C#'", "D'","D#'"],
['E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', "C'", "C#'", "D'","D#'","E'"],
['F', 'F#', 'G', 'G#', 'A', 'A#', 'B', "C'", "C#'", "D'","D#'","E'","F'"],
['F#', 'G', 'G#', 'A', 'A#', 'B', "C'", "C#'", "D'","D#'","E'","F'","F#'"],
['G', 'G#', 'A', 'A#', 'B', "C'", "C#'", "D'","D#'","E'","F'","F#'","G'"],
['G#', 'A', 'A#', 'B', "C'", "C#'", "D'","D#'","E'","F'","F#'","G'","G#'"],
['A', 'A#', 'B', "C'", "C#'", "D'","D#'","E'","F'","F#'","G'","G#'","A'"],
['A#', 'B', "C'", "C#'", "D'","D#'","E'","F'","F#'","G'","G#'","A'","A#'"],
['B', "C'", "C#'", "D'","D#'","E'","F'","F#'","G'","G#'","A'","A#'","B'"],]
lif=[]
for i in l:
    m=majorNotes(i)
    lif.append(m)

s=""
for i in lif:
    s=s+i+"\n"
with open ("majorNotes.txt","w") as f:
    f.write(s)

lif2=[]
for i in l:
    m=minorNotes(i)
    lif2.append(m)
s1=""
for i in lif2:
    s1=s1+i+"\n"
with open ("minorNotes.txt","w") as f2:
    f2.write(s1)

dict={"C":1,"C#":2,"D":3,"D#":4,"E":5,"F":6,"F#":7,"G":8,"G#":9,"A":10,"A#":11,"B":12}
m=(int(dict[input("Enter the word root:")]))
print("1)for major scale")
print("2)for minor scale")
c=int(input("Please Choose from the above options:"))
if(c==1):
    print("Major Scale of the above Key is :",lif[m-1])
if(c==2):
    print("Minor Scale of the above Key is :",lif2[m-1])


   

    
    