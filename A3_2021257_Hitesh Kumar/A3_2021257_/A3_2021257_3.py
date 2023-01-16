from datetime import datetime
class Bankaccount:
    def __init__(self,u, p,c):
        self.username=u
        self.password=p
        self.curr_balance=c
        self.aa=open(f'{self.username}.txt',"w")
        self.aa.close()

    def authenticate(self):
        self.m=input("Enter your secret password:")
        if self.m==self.password:
            return True
        else:
            return False
    def deposit(self,x):
        for i in range(1,4):
            a=self.authenticate()
            try:
                if a==True:
                    self.curr_balance=self.curr_balance+x
                    zz=open(f'{self.username}.txt',"a")
                    zz.write(f'{datetime.now()}'+f'The amount of Rupees {x} has been added Current Balance:>{self.curr_balance}:' "\n")
                    
                    zz.close()
                    break
                assert i<3
            except:
                print("To many failed attempts:")
                break
    def withdraw(self,y):
        for i in range(1,4):
            a=self.authenticate()
            try:
                if a==True:
                    self.curr_balance=self.curr_balance-y
                    if self.curr_balance<0:
                        self.curr_balance=self.curr_balance+y
                        print("Low balance!!Cannot be debited at this time!")
                    else:
                        zz=open(f'{self.username}.txt',"a")
                        zz.write(f'{datetime.now()} The amount of Rupees {y} has been withdrawn Current Balance->{self.curr_balance}:'"\n")
                        zz.close()
                    break
                assert i<3
            except:
                print("To many failed attempts:")
                break
                
    def bankStatement(self):
        for i in range(1,4):
            a=self.authenticate()
            try:
                assert i<3
                if a==True:
                    zz=open(f'{self.username}.txt',"r")
                    aa=zz.read()
                    zz.close()
                    return aa
            except:
                print("To many failed attempts:")
                break
print("------Welcome to the Bank of IIIT-D-------")

en=input("Enter the name:")
ep=input("Enter the password:")
sb=float(input("Staring balance for your account:"))
obj=Bankaccount(en,ep,sb)

A=True
while(A):
    print("Select your option")
    print("1.Deposit")
    print("2.Withdraw")
    print("3.Bank Statement")
    za=int(input("Enter your choice:"))
    if za==1:
        x=float(input("Provide the amount to be deposited:"))
        obj.deposit(x)
    if za==2:
        y=float(input("Provide the amount to be Withdraw:"))
        obj.withdraw(y)
    if za==3:
        aaa=obj.bankStatement()
        print(aaa)
    ss=input("You wanted to Continue(Yes/No):")
    if ss=="Yes":
        pass
    if ss=="No":
        break


    




            
        

            


        
        






