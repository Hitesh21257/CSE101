class LaundryService:
    def __init__(self,name,contact,email,type,branded,season,Id):
        self.ID=Id
        self.name_of_customer=name
        self.contact_of_customer=contact
        self.email=email
        self.type_of_cloth=type
        self.branded=branded
        self.season=season
    def customerDetail(self):
        print()
        print("-------The customer specific details--------------")
        print()
        print("Customer Id     :",self.ID)
        print("Customer Name   :",self.name_of_customer)
        print("Contact         :",self.contact_of_customer)
        print("Email           :",self.email)
        print("Type of Cloth   :",self.type_of_cloth)
        print("Branded         :",bool(self.branded))
        

    def calculateCharge(self):
        charge=0
        if self.type_of_cloth=="Cotton":
            charge=charge+50
        if self.type_of_cloth=="Silk":
            charge=charge+30
        if self.type_of_cloth=="Woolen":
            charge=charge+90
        if self.type_of_cloth=="Polyester":
            charge=charge+20
        if self.branded==True:
            charge=(1.5)*charge
        if self.season=="Winter":
            charge=charge/2
        if self.season=="Summer":
            charge=2*charge
        return charge
    def finalDetail(self,m):
        if m>200:
            print("To be returned in 4 days!")
        else:
            print("To be returned in 7 days!")

n=int(input("Tell the no. of customer:"))
nn=1
for i in range(n):

    a=input("Name of the customer:")
    b=int(input("Enter the contact no.:"))
    c=input("Email:")
    d=input("Type of cloth(Cotton/Silk/Woolen/Polyester):")
    e=int(input("Branded or not?(1/0):"))
    f=input("Tell the Season(Winter/Summer):")
    obj=LaundryService(a,b,c,d,e,f,nn)
    obj.customerDetail()
    m=obj.calculateCharge()
    print("Total Charge    :",m)
    obj.finalDetail(m)
    nn+=1