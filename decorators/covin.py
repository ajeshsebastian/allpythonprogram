
#
# def vaccination_portal(**kwargs ):
#     age=kwargs ["age"]
#     health=kwargs ["health_issues"]
#     if age>60 or health ==True :
#         print("request id allowed location ekm")
#     else:
#         print("not allowed")
#     #print(kwargs )
#
# vaccination_portal(name="ram",age=20,address="address",health_issues=True   )


#age above > 65 or health issues =True

def validation(func):
    def wrapper(**kwargs):
        age=kwargs ["age"]
        health=kwargs ["health_issues"]
        if age>60 or health ==True :
            return func (**kwargs  )
        else:
            print("not allowed")
    return wrapper


@validation
def vaccination_portal(**kwargs  ):
    print("request id allowed location ekm")

vaccination_portal (name="ram",age=25,address="address",health_issues=True  )



