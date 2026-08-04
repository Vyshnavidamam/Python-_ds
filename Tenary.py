a,b=10,20
x=30 if a<b else 40
print(x)#30

#a=int(input("enter frist Number:"))
#b=int(input)("enter second Number:")
min=a if a<b else b
print("Minimum value:",min)


a=int(input("Enter the First Number:")) 
b=int(input("Enter  the Second Number:")) 
c=int(input("Enter Third Number:")) 
min=a if a<b and a<c else b if b<c else c 
print("Maximum Value:",max) 

a=int(input("Enter First Number:")) 
b=int(input("Enter Second Number:")) 
c=int(input("Enter Third Number:")) 
max=a if a>b and a>c else b if b>c else c 
print("Minimum Value:",min)