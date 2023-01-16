#checking of the function to be satisfiable or Unsatisfiable 


for b2 in range(0,2):
    function=bool(b2 and not b2) 
    if function==False:
        print("Unsatisfiable")
        break

for b1 in range(0,2):
    for b2 in range(0,2):
        for b3 in range(0,2):
            function=((b1) or(b2))and((b2) or (not b3))
            if function==True:
                break
            
print("Satisfiable")
print(bool(b1),bool(b2),bool(b3))

            

            
    
