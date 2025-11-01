def push(stk, item):
    stk.append(item)
    print("Element added to the stack")
def pop(stk):
    if not stk:
        print("Underflow")
    else:
        print("Element deleted:", stk.pop())
def display(stk):
    if not stk:
        print("Stack is empty")
    else:
        top = len(stk) - 1
        print("Top element:", stk[top])
        print("Elements in the stack:")
        for i in range(top, -1, -1):
            print(stk[i])
stack = []
while True:
    print("Stack operations:")
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        b_no = int(input("Enter book no: "))
        b_name = input("Enter book name: ")
        rec = [b_no, b_name]
        push(stack, rec)
    elif choice == 2:
        pop(stack)
    elif choice == 3:
        display(stack)
    elif choice == 4:
        break
    else:
        print("Invalid choice. Please enter a valid option.")
    print('\n')
