a=[]
i=0
x=float(input("Enter list_ "))
a.append(x)
while x != "b" :
    x=input("Enter list_ ")
    if x != "b":
        x = float(x)
        a.append(x)

f="n"
y=float(input("What value you wanna find?_"))
z=0
while z < len(a) :
    if a[z] == y:
        print ("value found at," + str(z+1))
        f = "y"
        break
    z += 1    

if f != "y" :
    print("value not found")
