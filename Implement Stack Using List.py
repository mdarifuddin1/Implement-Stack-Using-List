# Code by Md Arif Uddin 
# ID 193207042

stack = []
def push():
    element = input ("Enter the Element")
    stack.append(element)
    print(stack)

def pop_element():
    if not stack:
        print("stack is empty")
    else:
        e = stack.pop()
        print("Remeoved element: ",e)
        print(stack)

while True:
    print("select the operation 1.Push 2.POP.3 exit")
    choice = int(input ()) 
    if choice == 1:
        push()
    elif choice == 2:
        pop_element ()
    elif choice == 3:
        break
    else:
        print("Enter the choice operation ")
