
n=int(input("Please tell the no. of students:"))
for i in range(1,n+1):
    #choice between 2D or 3D shapes or you can exit
    print("1) for 2D")
    print("2) for 3D")
    print("3) for exit")
    x=int(input("choose between 2D or 3D or exit:"))
    #please put input 1 for 2D shapes
    #please put input 2 for 3D shapes
    if(x==1):
        print("You choose 2D shapes")
        print()
        print("1:Square")
        print("2:Rectangle")
        print("3:Rhombus")
        print("4:Parallelogram")
        print("5:Circle")
        c=int(input("Please choose any 1 from the above 2D shapes:"))
        if(c==1):
            print("You choose square")
            s=int(input("Tell the side of the square:"))
            par=4*s
            ar=s**2
            print("Parameter of square is :",par)
            print("Area of square is ",ar)
            print()
        elif(c==2):
            print("You choose rectangle")
            l=int(input("Tell me the length of rectangle:"))
            b=int(input("Tell me the breadth of rectangle:"))
            par=2*(l+b)
            ar=l*b
            print("Parameter of rectangle is :",par)
            print("Area of recatangle is:",ar)
            print()
        elif(c==3):
            print("You choose Rhombus")
            a=int(input("Tell the side of rhombus:"))
            d1=int(input("Tell the diagonal no.1 of rhombus:"))
            d2=int(input("Tell the diagonal no. 2 of rhombus:"))
            par=4*a 
            ar=(1/2)*d1*d2
            print("Parameter of rhombus is :",par)
            print("Area of rhombus is:",ar)
            print()
        elif(c==4):
            print("You choose parallelogram")
            l=int(input("Tell me the length of parallelogram:"))
            b=int(input("Tell me the breadth of parallelogram:"))
            h=int(input("Tell me the height of parallelogram:"))
            par=2*(l+b)
            ar=b*h
            print("Parameter of parallelogram is :",par)
            print("Area of parallelogram is:",ar)
            print()
        elif(c==5):
            print("You choose Circle")
            r=int(input("Tell me the radius of circle:"))
            par=2*(22/7)*r
            ar=2*(22/7)*(r**2)
            print("Parameter of circle is :",par)
            print("Area of circle is:",ar)
            print()

    elif(x==2):
        print("You choose 3D shapes")
        print()
        print("6:Cube")
        print("7:Cubiod")
        print("8:Right circular cone")
        print("9:Hemisphere")
        print("10:Sphere")
        print("11:Solid Sphere")
        print("12:Hollow Cylinder")
        c=int(input("Please choose any 1 from the above 3D shapes:"))
        if(c==6):
            print("You choose Cube")
            a=int(input("Tell me the side of cube:"))
            csa=4*(a**2)
            tsa=6*(a**2)
            vol=a**3
            print("CSA of cube is:",csa)
            print("TSA of cube is:",tsa)
            print("Volume of cube is:",vol)
            print()
        if(c==7):
            print("You choose Cubiod")
            l=int(input("Tell me length of cubiod:"))
            b=int(input("Tell me breadth of cubiod:"))
            h=int(input("Tell me height of cubiod:"))
            csa=2*(l+b)*h
            tsa=2*((l*b)+(b*h)+(h*l))
            vol=l*b*h
            print("CSA of cubiod is:",csa)
            print("TSA of cubiod is:",tsa)
            print("Volume of cubiod is:",vol)
            print()
        if(c==8):
            print("You choose Right Circular Cone")
            r=int(input("Tell me radius of base of cone:"))
            h=int(input("Tell me height of cone:"))
            l=int(input("Tell me slant height of cone:"))
            csa=(22/7)*r*l 
            tsa=(22/7)*r*(l+r)
            vol=(1/3)*(22/7)*(r**2)*h
            print("CSA of Right circular cone is:",csa)
            print("TSA of Right circular cone is:",tsa)
            print("Volume of Right circular cone is:",vol)
            print()
        if(c==9):
            print("You choose Hemisphere")
            r=int(input("Tell me radius of hemisphere:"))
            csa=(22/7)*2*(r**2)
            tsa=(22/7)*3*(r**2)
            vol=(2/3)*(22/7)*(r**3)
            print("CSA of Hemisphere is:",csa)
            print("TSA of Hemisphere is:",tsa)
            print("Volume of Hemisphere is:",vol)
            print()
        if(c==10):
            print("You choose Sphere")
            r=int(input("Tell me radius of Sphere:"))
            csa=(22/7)*4*(r**2)
            tsa=(22/7)*4*(r**2)
            vol=(4/3)*(22/7)*(r**3)
            print("CSA of Sphere is:",csa)
            print("TSA of Sphere is:",tsa)
            print("Volume of Sphere is:",vol)
            print()
        if(c==11):
            print("You choose Solid Cylinder ")
            r=int(input("Tell me radius of Solid Cylinder:"))
            h=int(input("Tell me height of Solid Cylinder:"))
            csa=(2)*(22/7)*r*h
            tsa=((2)*(22/7)*r*h)+(2*(22/7)*(r**2))
            vol=(22/7)*(r**2)*h
            print("CSA of Solid Cylinder is:",csa)
            print("TSA of Solid Cylinder is:",tsa)
            print("Volume of Solid Cylinder is:",vol)
            print()
        if(c==12):
            print("You choose Hollow  Cylinder ")
            r1=int(input("Tell me the outer radius of Hollow Cylinder:"))
            r2=int(input("Tell me the inner radius of hollow Cylinder:"))
            h=int(input("Tell me height of Hollow Cylinder:"))
            csa=2*(22/7)*h*(r1+r2)
            tsa=(2*(22/7)*h*(r1+r2))+((2*22/7)*((r1**2)-(r2**2)))
            vol=((22/7)*((r1**2)-(r2**2)))*h
            print("CSA of Hollow Cylinder is:",csa)
            print("TSA of  Hollow  Cylinder is:",tsa)
            print("Volume of Hollow Cylinder is:",vol)
            print()

    #for those students who donot choose any one of the shapes
    elif(x==3):
        print("Exit")

            









            




        
