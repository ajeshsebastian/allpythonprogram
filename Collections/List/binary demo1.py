#lst=[1,2,3,4,5,6]
#6 pair (2,4)
#7 pair (3,4)

#pair output

def pair(lst,element):
    res=[]
    while lst:
        num=lst.pop()
        diff=element-num
        if diff in lst:
            res.append((diff,num))
    res.reverse()
    return res
lst=[1,2,3,4,5,6]
element=int(input("enter the element"))
print(pair(lst,element))