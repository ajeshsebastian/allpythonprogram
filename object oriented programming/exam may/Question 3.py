#Library_name, book_name, author, pages
class Book:
    def __init__(self,libname,boname,aname,page):
        self.libname=libname
        self.boname=boname
        self.aname = aname
        self.page=page
        print("Library_name",self .libname )
        print("Book name: ",self.boname)
        print("Author",self.aname)
        print("Pages",self.page)

bo=Book ("L1","abc","jose",123)
