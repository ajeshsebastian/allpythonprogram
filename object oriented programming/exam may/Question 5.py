class Book:
    def properties(self,libname,name):
        self.libname=libname
        self.name=name
        print(self .libname ,self .name )


class Details(Book  ):
    def properties(self,aname,page):
        self.aname=aname
        self.page=page
        print("Child Class")
        print(self .aname ,self .page )
c=Details  ()

c.properties("jose",234)
