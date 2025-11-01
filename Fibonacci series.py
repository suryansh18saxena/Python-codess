n=int(input(""))
a,b=0,1
print("Fibonacci series ",end="")
for _ in range (n):
    print(a,end="")
    a,b=b,a+b