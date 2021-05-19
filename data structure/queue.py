#data structures

# to store data

size=int(input("Enter the size of the Queue"))
lst=[]
top=0
n=0


def insert():
    global top,size
    if top>=size :
        print("Queue is full")
    else:
        add=int(input("Enter the element"))
        lst.append(add)
        top+=1
        print(lst)

def dele():
    global top,size
    if top<=0:
        print("Queue is empty")
    else:
        lst.pop(0)
        top-=1
        print(lst)

while n!=1:
    op = int(input("Enter 1 for insert or enter 2 for delete"))
    if op==1:
        insert()
    elif op==2:
        dele()


# if(size>0):
#     print()
#     for i in range(size):
#         print("Enter the elements")
#         lst.append(i)
# print(lst)

