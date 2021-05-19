class Animal:
    def __init__(self,category,color,name):
        self.category=category
        self.color=color
        self.name=name

class Dog(Animal ):
    def printval(self):
        print("Details\n")
        print("Category: ",self.category  )
        print("Color: ",self.color)
        print("Name: ",self.name )

do=Dog ("Dog","Black","Tiger")
do.printval()