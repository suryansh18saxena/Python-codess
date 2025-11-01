# # # all the fector of the user input number and there sum
# # num=int(input("enter the number= "))
# # sum=0
# # for i in range(1,num+1):
# #     if num % i==0:
# #          print(i,"is the factor of ",num)
# #          sum+=i
# # print("sum of all the factor of",num,"is",sum)
# #=====================================================

# # # ADD ALL THE FACTOR OF 50 IN THE LIST    
# # a=50
# # b=[]
# # for i in range (1,a+1):
# #     if a%i==0:
# #         print(i)
# #         b.append(i)
# # print(b)
# #======================================================
# ## WAPP TO PRINT THE SUM OF THE NUMBER FORM 1 TO 10 
# # n=int(input("enter the num "))
# # sum=0
# # for i in range(1,n+1):
# #     sum+=i
# # print(sum)
# #======================================================
# #WAPP TO PRINT THE SUM OF THE NUMBER FORM A TO B
# # a=int(input("enter the num "))
# # b=int(input("enter the num "))
# # sum=0
# # for i in range(a,b+1):
# #     sum+=i
# # print(sum)
# #======================================================
# #WAPP TO PRINT THE SUM OF THE EVEN NUMBER FORM 1 TO N 
# # n=int(input("enter the number "))
# # sum=1
# # for i in range(1,n+1):
# #     if i %2==0:
# #         sum+=i
# # print(sum)
# #========================================================
# #WAPP TO ADD SUM OF THE NUMBERS FROM 1 TO N 
# # n=int(input("enter the number "))
# # sum=0
# # a=[]
# # for i in range(1,n+1):
# #     if i %2==0:
# #         sum+=i
# # a.append(sum)
# # print(a)
# # ==========================================================
# # WAPP TO PRINT THE MULTIPLICATION OF THE EVEN NUMBER FROM 1 TO N 
# # n=int(input("enter the number "))
# # sum=1
# # for i in range(1,n+1):
# #     if i %2==0:
# #         sum*=i
# # print(sum)
# # i=int(input("enter the number"))
# # n=int(input("enter the number"))

# # while i<n+1:
# #     if i%2==0:
# #         print(i)
# #         i+=1
# ======================================================================================
#  1) print numbers from 1 to 10

# for i in range (1,11):
#     print(i)
# #===========================================================================
# 2) print numbers from 1 to n where n is given by user

# n=int(input("enter the number "))
# for i in range (1,n+1):
#     print(i)
# # ===========================================================================
# 3) print numbers from a to b where a and b are given by user

# a=int(input("enter the number "))
# b=int(input("enter the number "))
# for i in range (a,b+1):
#     print(i)
# #=============================================================================
# 4) print even from 1 to n where n is given by user

# n=int(input("enter the number "))
# for i in range (1,n+1):
#     if i%2==0:
#         print(i)
# #=============================================================================
# 5) print numbers divisible by 5 and 3 from 1 to n

# n=int(input("enter the number "))
# for i in range(1,n+1):
#     if i%5==0 and i%3==0:
#         print(i)
# #=============================================================================
# 6) print the sum of first n numbers from 1 to n.

# n=int(input("enter the number "))
# sum=0
# for i in range(1,n+1):
#     sum+=i
# print(i)
# #=============================================================================
# 7) print the multiplication of numbers from 1 to n.

# n=int(input("enter the number "))
# multiplication=1
# for i in range(1,n+1):
#     multiplication*=i
# print(multiplication)
# #==============================================================================
# n=int(input("enter the number "))
# x=1
# while x<=n:
#     if x%5==0 and x%3==0:
#         print(x)
#     x+=1
#================================================================================
# n=int(input("enter the age"))
# if n>=18:
#     print("can give vote")
# else:
#     print("bacche hai aap ")
# n=1
# while n<=50:
#     if n%2!=0:
#         print(n)
#     n+=1
# =======================================================================================
# u=input("enter the string")
# n = len(u) -1
# while n >= 0:
#     print(u[n],end="")
#     n -= 1  

# n=input("enter the name")
# for i in range(len(n)-1,-1,-1):
#     print(n[i],end="")


# data = ["1", "2", "3", "4", "5"]
# a = []
# for i in data:
#     a.append(int(i))
# print(a)
# print(sum(a))


# l=["hello",3,"byebye",7]
# a=[]
# for i in l:
#     if i not in [1,2,3,4,5,6,7,8,9,0]:
#         a.append(i)
# print(a)
# =================================================================================
n=int(input())
i=1
while i<=n:
    print(i)
    i+=1