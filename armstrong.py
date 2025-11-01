n = int(input("Enter a number you want to check: "))
s = str(n)
o = len(s)
p = 0#1+64+125
for i in s:
    p += int(i) ** o
    print(p)
if p == n:
    print(f"{n} is an Armstrong number.")
else:
    print(f"{n} is not an Armstrong number.")