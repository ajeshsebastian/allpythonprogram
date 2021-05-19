que=[]
size=int(input("Enter the size of queue"))
rear=0
front=0
n=0

def insert():
    global front,rear,size,que
    if rear>=size:
        print("queue is full")
    else:
        p=int(input("Enter the element want to insert"))
        que.insert(rear,p)
        rear+=1
        for i in range(front,rear):
            print(que[i])
def delete():
    global front,rear,size,que
    if rear==front:
        print("queue is empty")
    else:
        front+=1
        for i in range(front,rear):
            print(que[i])
while n!=1:
    opt=int(input("press \n1)insert \n2)delete \n"))
    if opt==1:
        insert()
    elif opt==2:
        delete()
