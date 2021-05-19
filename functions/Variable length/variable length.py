#variable length

#any number of arguments we can use  *args


def add(*args ):
    res=0
    for num in args :
        res+=num
    return res
    #print(args )
    #print(type (args ))

#add(10)
print(add(10,20))
print(add(10,20,30))


def print_employee(**kwargs ):
    for k,v in kwargs .items() :

        print(k,"=>",v)


print_employee(id=100,na_place="pala",w_palce="kottayam")

