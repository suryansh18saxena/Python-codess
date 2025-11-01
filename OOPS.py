# class programmer():
#     companey=" JALALABAD COLD STORAGE"
#     def __init__(self,name,salary,age):
#         self.name=name
#         self.salary=salary
#         self.age=age

# n=programmer("nitin kumar saxena","2cr",57)
# print(n.name,n.age,n.salary,n.companey)

class calculator():
    def __init__(self,n):
        self.n=n

    def square(self):
        print(f"the square of the number{self.n*self.n}")
    def cube(self):
        print(f"the cube of the number{self.n*self.n*self.n}")
    def squareroot(self):
        print(f"the square root of thee number{self.n**0.5}")


n=calculator(4)
n.square()
n.cube()
n.squareroot()