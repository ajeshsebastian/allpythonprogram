#data structures

# to store data

size=int(input("Enter the size of the stack"))
lst=[]
top=0
n=0


def push():
    global top,size
    if top>=size :
        print("stack is full")
    else:
        add=int(input("Enter the element"))
        lst.append(add)
        top+=1
        print(lst)

def pop():
    global top,size
    if top<=0:
        print("stack is empty")
    else:
        lst.pop()
        top-=1
        print(lst)

while n!=1:
    op = int(input("Enter 1 for push or 2 for pop"))
    if op==1:
        push()
    elif op==2:
        pop()
# if(size>0):
#     print()
#     for i in range(size):
#         print("Enter the elements")
#         lst.append(i)
# print(lst)

