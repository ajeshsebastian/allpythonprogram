# to string method
# __str__(self) only returns string values
#we can use the + sign to print two or more values
#we can use str method to convert an integer to string

class Book:
    def setval(self,boname,aname,page):

        self.boname=boname
        self.aname = aname
        self.page=page
        print(self.boname,self.aname,self.page)
    def __str__(self):
        return self.boname+self.aname +str (self .page )

bo=Book ()
bo.setval("abc","wjwj",287)
print(bo )




# class Book:
#     def __init__(self,boname,aname,page,price):
#
#         self.boname=boname
#         self.aname = aname
#         self.page=page
#         self.price=price
#     def getval(self):
#
#         print("Book Name : ",self.boname )
#         print("Author Name : ", self.aname)
#         print("Pages : ", self.page )
#         print("Price : ",self.price )
# bu=input("Enter Book")
# au=input("Enter author name")
# pa=int(input("Enter page count"))
# pr=int(input("Enter book price"))
#
# bo=Book (au,bu,pa,pr)
# bo.getval()



