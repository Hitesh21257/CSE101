a=int(input("Please tell me price of item 1:"))
b=int(input("Please tell me price of item 2:"))
c=int(input("Please tell me price of item 3:"))

print("-----------------------------------------------------------------------------------")
print("-----------------------------------------------------------------------------------")
print("Discount details")

d=int(input("Provide discout(in percentage) for the 1st saver combo :"))
e=int(input("Provide discout(in percentage) for the 2nd saver combo :"))
f=int(input("Provide discout(in percentage) for the 3rd saver combo :"))

print("----------------------------------------------------------------------------------------------")
m=int(input("Provide your 10 digit mobie no.:"))
print("The resulting catalogue is :")
print("-----------------------------------------------------------------------------------------------")
print("------------------------------------------------------------------------------------------------")

print("Delhi Days")
print("f-block,Model town -3")
print("New delhi:1230212")

print("-------------------------------------------------------------------------------------------------")

print("Item 1          :",a)
print("Item 2          :",b)
print("Item 3          :",c)
print("Combo pack 1    :",(a+b)*((100-d)/100))
print("Combo pack 2    :",(a+c)*((100-e)/100))
print("Combo pack 3    :",(b+c)*((100-f)/100))

print("Supersaver pack :",(a+b+c)*(72/100))


print("----------------------------------------------------------------------------")
print("------------------------------------------------------------------")
(print("For home delivery, contact this number:",9813575994))