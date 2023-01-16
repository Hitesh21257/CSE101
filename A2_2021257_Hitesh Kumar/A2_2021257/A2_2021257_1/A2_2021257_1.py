
a=open("question1_input.txt")
b=a.read()

c_c='-'
print(c_c*50)

for i in range(1,100):
    print("Choose your Choice:")
    print("1. Display specific Word Count")
    print("2. Display all unique Words")
    print("3. Display all word Count")
    print("4. Replace Word")
    print("5. Quit")

    w=int(input("Choose from the above choices:"))


    if(w==1):
        print("You Wanted to display the specific word count")
        c=b.split()
        d={}
        for i in c:
            if(i not in d):
                d[i]=0
            d[i]=d[i]+1
        y=(input("Tell me the word you wanted to count :"))
        print("Word count is:",d[y])
    

    elif(w==2):
        print("You wanted to display all unique words")
        a=set(b.split())
        l=list(a)
        for i in l:
            print(f'{i} ;',end=" ")
            
    elif(w==3):
        print("you wanted to display all word count")
        c=b.split()
        d={}
        for i in c:
            if(i not in d):
                d[i]=0
            d[i]=d[i]+1
        for i,j in d.items():
            print(f'{i} : {j}')
    elif(w==4):
        print("You wanted to replace the word")
        c=input("word you wanted to replace:")
        d=input("New word will be:")
        y=b.replace(c,d)
        a.close()

        y1=open("question1_input.txt","w")
        y2=y1.write(y)
        y1.close()
    
    elif(w==5):
        print("you wanted to close this program")
        break

a.close()


