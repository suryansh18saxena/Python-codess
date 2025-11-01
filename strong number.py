b=int(input("enter the number "))#145
a=str(b)
c=0
for i in a:
    i=int(i)
    t=1
    for j in range(1,i+1):
        t=t*j
    c+=t
if c==b:
    print("f{b}is the strong number")
else:
    print("f{b}is not a strong number")
