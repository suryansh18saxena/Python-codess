# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

# n=5
# for i in range(n):
#     for j in range(n):
#         print("*",end=" ")
#     print()


# * * * * *
# *       *
# *       *
# *       *
# * * * * *

# n=5
# for i in range(n):
#     for j in range(n):
#         if (i==0 or i==n-1 or j==0 or j==n-1):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# *
# * *
# * * *
# * * * *
# * * * * *

# n=5
# for i in range(n+1):
#     for j in range(i):
#         print("*",end=" ")
#     print()

# * * * * *
# * * * *
# * * *
# * *
# *

# n=5
# for i in range(n,0):
#     for j in range(n-i):
#         print("*",end=" ")
#     print()

# it can be done as

# n=5
# for i in range(n,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()

# * * * * *
#   * * * *
#     * * *
#       * *
#         *

# n=5
# for i in range (n):
#     print(" "*i,"*"*(n-i))

#     *
#    * *
#   * * *
#  * * * *
# * * * * *

# n=5
# for i in range(n):
#     print(" "*(n-i-1),"* "*(i+1))

# * * * * *
#  * * * *
#   * * *
#    * *
#     *

# n=5
# for i in range(n):
#     print(" "*(i),"* "*(n-i))

#     *
#    * *
#   * * *
#  * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *

# n=5
# for i in range(n):
#     print(" "*(n-i-1),"* "*(i+1))
# for j in range(n):
#     print(" "*(j+ 1),"* "*(n-j-1))


    # *       *
    #   *   *
    #     *
    #   *   *
    # *       *

    
